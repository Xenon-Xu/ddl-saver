import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QDialog, QMessageBox
from PyQt5.QtGui import QPainter, QPixmap, QColor, QBrush, QTextCharFormat, QMouseEvent
from PyQt5.QtCore import Qt, QPoint, QTime, QDate, pyqtSignal, QTimer, QEvent
from mainWin import *
from addDdlWin import *
from setWin import *
from trayIcon import *
from trayQuestionDialog import *
import os
import datetime
import csv
import pickle
import threading
from functools import cmp_to_key
from math import inf
from constants import *
from functions import *

if IS_WIN10_SYS and SHOW_WIN10_NOTIFICATION:
    from win10toast import ToastNotifier


class MainWin(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)
        self.setupUi(self)

        self.statistics = {
            'earliest ddl': '', 'earliest count down': '', 'number': 0, 'invalid': 0, 'emergent': 0,
            'important': 0, 'latest count down': '', 'remain': 0
        }
        self.settings = {
            'sort rule': IMPORTANCE_PRIORITY,
            'count down warning time': [1, 0, 0],
            'count down warning win': True,
            'show toast': SHOW_WIN10_NOTIFICATION and IS_WIN10_SYS,
            'minimize': True,
            'remember close action': False
        }

        self.trayicon = TrayIcon(self)
        self.trayicon.show()

        self.ddlModified = False  # whether ddl list has been modified

        self.ddlList = []  # maintain DDLs
        self.ddlSet = set()  # identify same name ddl
        self.settingInit()  # setting init must set before ddlTable init
        self.ddlTableInit()

        self.componentInit()

        self.addDdlWin = addDdlWin()
        self.setWin = setWin()
        self.trayQuestionDialog = trayQuestionDialog()

        self.addDdlWin.addDdlWinSignal.connect(self.addDDlAction)  # signal connected
        self.addDdlWin.modDdlWinSignal.connect(self.modDDlAction)
        self.setWin.setSortRuleSignal.connect(self.setSortRuleAction)
        self.setWin.setWarnSignal.connect(self.setWarnAction)
        self.setWin.remTrayCheckedSignal.connect(self.setRemTrayAction)
        self.setWin.showWarnWinButtonPressSignal.connect(self.showWarnCountTimeWinManually)
        self.setWin.setFinishedSignal.connect(self.settingSaveAction)  # update signal
        self.trayicon.exitSignal.connect(self.ask_before_close)
        self.trayicon.openSignal.connect(self.recover_from_tray)
        self.trayicon.traySignal.connect(self.minimize_to_tray)
        self.trayQuestionDialog.minimizeToTraySignal.connect(self.minimize_to_tray)
        self.trayQuestionDialog.rememberTrayChoiceSignal.connect(self.setRemTrayAction)
        self.trayQuestionDialog.exitSignal.connect(self.ask_before_close)
        self.trayQuestionDialog.setCloseActionSignal.connect(self.setCloseAction)
        self.trayQuestionDialog.settingSaveActionSignal.connect(self.settingSaveAction)

        main_update_timer = QTimer(self)  # set update timer
        main_update_timer.timeout.connect(self.main_update)
        main_update_timer.start(30000)  # update main UI every 30 seconds

    def _thread_it(self, func, *args):
        t = threading.Thread(target=func, args=args)
        t.setDaemon(True)
        t.start()

    def _ddlCmp_importance(self, ddl1: dict, ddl2: dict):
        if (not ddl1['effect'] and ddl2['effect']) or (ddl1['effect'] and not ddl2['effect']):
            return_value = not ddl2['effect']
        elif ddl1['complete'] != ddl2['complete']:
            return_value = ddl2['complete']
        elif ddl1['importance'] != ddl2['importance']:
            return_value = ddl1['importance'] < ddl2['importance']
        elif ddl1['date'] != ddl2['date']:
            return_value = ddl1['date'] < ddl2['date']
        elif ddl1['timespan'] != ddl2['timespan']:
            return_value = ddl1['timespan'][0:2] < ddl2['timespan'][0:2]
        else:
            return_value = ddl1['name'] < ddl2['name']
        if return_value:
            return -1
        else:
            return 1

    def _ddlCmp_timeremain(self, ddl1: dict, ddl2: dict):
        if (not ddl1['effect'] and ddl2['effect']) or (ddl1['effect'] and not ddl2['effect']):
            return_value = not ddl2['effect']
        elif ddl1['complete'] != ddl2['complete']:
            return_value = ddl2['complete']
        elif ddl1['date'] != ddl2['date']:
            return_value = ddl1['date'] < ddl2['date']
        elif ddl1['timespan'] != ddl2['timespan']:
            return_value = ddl1['timespan'][0:2] < ddl2['timespan'][0:2]
        elif ddl1['importance'] != ddl2['importance']:
            return_value = ddl1['importance'] < ddl2['importance']
        else:
            return_value = ddl1['name'] < ddl2['name']
        if return_value:
            return -1
        else:
            return 1

    @staticmethod
    def _date_now():
        return datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day

    @staticmethod
    def _time_now():
        return datetime.datetime.now().hour, datetime.datetime.now().minute

    def _datetime_now(self):
        date_now_t = self._date_now()
        time_now_t = self._time_now()
        return datetime.datetime(date_now_t[0], date_now_t[1], date_now_t[2], time_now_t[0], time_now_t[1])

    def _draw_color_calendar(self, q_date: QDate, color: QColor):
        todayFormat = QTextCharFormat()
        todayFormat.setBackground(color)
        self.calendarWidget.setDateTextFormat(q_date, todayFormat)

    def _remove_color_calendar(self, q_date: QDate):
        self.calendarWidget.setDateTextFormat(q_date, NULL_TEXTCHARFORMAT)

    def _date_tuple2QDate(self, date: (int, int, int)):
        return QDate(date[0], date[1], date[2])

    def _date_not_colored(self, q_date: QDate):
        for textDate, textFormat in self.calendarWidget.dateTextFormat().items():
            if textDate == q_date:
                if textFormat == NULL_TEXTCHARFORMAT:
                    continue
                else:
                    return False
        return True

    def main_update(self, showWarnTip=False):
        self.remove_color_calendar()
        self.ddlStateShowUpdate(showWarnTip=showWarnTip)
        self.selectDdlAction()
        self.noticeUpdate()

    def componentInit(self):
        pass

    def showWarnCountTimeWin(self, info=False):
        warningText = ''
        for ddl in self.ddlList:
            if ddl['effect']:
                if ddl['count down time'] < self.settings['count down warning time']:
                    warningText += '{} 剩余 {} 天 {} 小时 {} 分\n'.format(
                        ddl['name'], ddl['count down time'][0], ddl['count down time'][1], ddl['count down time'][2])
        if warningText != '':
            if 'win10toast' in sys.modules and SHOW_WIN10_NOTIFICATION and self.settings['show toast'] and IS_WIN10_SYS:
                def showToaster():
                    try:
                        ToastNotifier().show_toast(
                            '倒计时预警', '{}\n即将到期'.format(warningText)
                            , duration=10, icon_path='icon.ico')
                    except AttributeError:
                        pass
                self._thread_it(showToaster)
            qApp.setQuitOnLastWindowClosed(False)
            QMessageBox.warning(self, '倒计时预警', '{}\n即将到期'.format(warningText))
        else:
            if info:
                QMessageBox.information(self, '提示', '无倒计时预警\n(启动时不会弹窗)')

    def showWarnCountTimeWinManually(self):
        self.showWarnCountTimeWin(info=True)

    def showSetWin(self):
        self.setWin.sortRuleComboBox.setCurrentIndex(self.settings['sort rule'])
        self.setWin.countDownDaySpinBox.setValue(self.settings['count down warning time'][0])
        self.setWin.countDownHourSpinBox.setValue(self.settings['count down warning time'][1])
        self.setWin.countDownMinuteSpinBox.setValue(self.settings['count down warning time'][2])
        self.setWin.warningWinCheckBox.setChecked(self.settings['count down warning win'])
        if IS_WIN10_SYS and SHOW_WIN10_NOTIFICATION:
            self.setWin.warningToastCheckBox.setChecked(self.settings['show toast'])
        self.setWin.remTrayCheckBox.setChecked(self.settings['remember close action'])

        self.setWin.show()

    def showAddDdlWin(self):
        self.addDdlWin.nameLineEdit.setText('')
        self.addDdlWin.locationLineEdit.setText('')

        self.addDdlWin.timeEdit1.setTime(QTime.currentTime())
        self.addDdlWin.timeEdit2.setTime(QTime.currentTime())
        self.addDdlWin.timeEdit1.setEnabled(False)
        self.addDdlWin.timeEdit2.setEnabled(False)
        self.addDdlWin.dateEdit.setDate(QDate.currentDate())
        self.addDdlWin.wholeDayCheckBox.setChecked(True)
        self.addDdlWin.importanceComboBox.setCurrentIndex(0)

        self.addDdlWin.modify = False
        self.addDdlWin.setWindowTitle('添加DDL')

        self.addDdlWin.update_ddlSet(self.ddlSet)
        self.addDdlWin.show()

    def showAddDdlWin_mod(self):
        row_index = self.ddlTableWidget.currentRow()
        if row_index == -1:
            return

        name = self.ddlList[row_index]['name']
        location = self.ddlList[row_index]['location']
        timespan = self.ddlList[row_index]['timespan']
        date = self.ddlList[row_index]['date']

        self.addDdlWin.nameLineEdit.setText(name)
        self.addDdlWin.locationLineEdit.setText(location)

        self.addDdlWin.timeEdit1.setTime(QTime(timespan[0], timespan[1]))
        self.addDdlWin.timeEdit2.setTime(QTime(timespan[2], timespan[3]))
        self.addDdlWin.timeEdit1.setEnabled(True if timespan != ALL_DAY_TUPLE else False)
        self.addDdlWin.timeEdit2.setEnabled(True if timespan != ALL_DAY_TUPLE else False)
        self.addDdlWin.dateEdit.setDate(QDate(date[0], date[1], date[2]))
        self.addDdlWin.wholeDayCheckBox.setChecked(True if timespan == ALL_DAY_TUPLE else False)
        self.addDdlWin.importanceComboBox.setCurrentIndex(self.ddlList[row_index]['importance'])

        self.addDdlWin.modify = True
        self.addDdlWin.setWindowTitle('修改DDL')

        self.addDdlWin.update_ddlSet(self.ddlSet)
        self.addDdlWin.show()

    def selectDdlRow(self, date: QDate):
        for i, ddl in enumerate(self.ddlList):
            if self._date_tuple2QDate(ddl['date']) == date:
                self.ddlTableWidget.selectRow(i)
                self.ddlTableWidget.setFocus()
                return

    def addDDlAction(self, name, date_y, date_m, date_d, time1_h, time1_m, time2_h, time2_m, location, importance):
        self.ddlTableAddRow(name, (date_y, date_m, date_d), (time1_h, time1_m, time2_h, time2_m), location, importance, complete=False)
        self.ddlSet.add(name)
        self.main_update()
        self.ddlModified = True

    def modDDlAction(self, name, date_y, date_m, date_d, time1_h, time1_m, time2_h, time2_m, location, importance):
        row_index = self.ddlTableWidget.currentRow()
        self._remove_color_calendar(self._date_tuple2QDate(self.ddlList[row_index]['date']))
        complete_t = self.ddlList[row_index]['complete']
        self.ddlSet.remove(self.ddlList[row_index]['name'])
        self.ddlList.remove(self.ddlList[row_index])
        self.ddlTableAddRow(name, (date_y, date_m, date_d), (time1_h, time1_m, time2_h, time2_m), location, importance, complete_t)
        self.ddlSet.add(name)
        self.main_update()
        self.ddlModified = True

    def delDdlAction(self):
        row_index = self.ddlTableWidget.currentRow()
        if row_index == -1:
            return

        judgment = QMessageBox.question(self, '删除', '确定删除 DDL: {} 吗？'.format(self.ddlList[row_index]['name']))
        if judgment == QMessageBox.Yes:

            self._remove_color_calendar(self._date_tuple2QDate(self.ddlList[row_index]['date']))

            self.ddlSet.remove(self.ddlList[row_index]['name'])
            self.ddlList.remove(self.ddlList[row_index])
            self.main_update()
            self.ddlModified = True

    def selectDdlAction(self):
        row_index = self.ddlTableWidget.currentRow()
        if row_index == -1:
            self.selectLineEdit.setEnabled(True)
            self.selectLineEdit.setReadOnly(False)
            self.selectLineEdit.setText('DDL 名称')
            self.selectLineEdit.setReadOnly(True)
            self.selectLineEdit.setEnabled(False)

            self.modPushButton.setEnabled(False)
            self.delPushButton.setEnabled(False)
            self.completePushButton.setEnabled(False)
            return
        else:
            self.selectLineEdit.setEnabled(True)
            self.selectLineEdit.setReadOnly(False)
            self.selectLineEdit.setText(self.ddlList[row_index]['name'])
            self.selectLineEdit.setReadOnly(True)

            self.modPushButton.setEnabled(True)
            self.delPushButton.setEnabled(True)
            self.completePushButton.setEnabled(True)

            if self.ddlList[row_index]['complete']:
                self.completePushButton.setText('标记为未完成')
            else:
                self.completePushButton.setText('标记为已完成')

    def saveDdlAction(self):
        judgment = QMessageBox.question(self, '保存DDL', '确定保存当前DDL设置？')
        if judgment == QMessageBox.Yes:
            with open('ddl.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                for ddl in self.ddlList:
                    writer.writerow(
                        iter([ddl['name'], ddl['date'], ddl['timespan'], ddl['location'], ddl['importance'], ddl['complete']]))
            self.ddlModified = False

    def settingSaveAction(self):
        with open('config', 'wb') as f:
            pickle.dump(self.settings, f)
        self.main_update()

    def remove_color_calendar(self):  # remove all color format of calendar (replace the origin to NULL_TEXTCHARFORMAT)
        for textDate, textFormat in self.calendarWidget.dateTextFormat().items():
            self._remove_color_calendar(textDate)

    def ddlTableAddRow(self, name: str, date: (int, int, int), timespan: (int, int, int, int), location, importance, complete):
        self.ddlList.append({
            'name': name, 'date': date, 'timespan': timespan, 'location': location,
            'importance': importance, 'complete': complete
        })

    def ddlStateShowUpdate(self, showWarnTip=False):
        self._draw_color_calendar(QDate.currentDate(), QCOLOR_FAINTBLUE)

        self.ddlTableWidget.setRowCount(len(self.ddlList))
        self.statistics['number'] = len(self.ddlList)

        latest_count_down = '无'
        latest_count_down_seconds = 0
        latest_count_down_days = 0
        earliest_count_down = '无'
        earliest_count_down_name = '无'
        earliest_count_down_seconds = +inf
        earliest_count_down_days = +inf
        emergent_num = 0
        important_num = 0
        invalid_num = 0
        remain_num = 0
        for i, ddl in enumerate(self.ddlList):
            if 'turn warning' not in ddl:
                ddl['turn warning'] = False

            if ddl['timespan'] == ALL_DAY_TUPLE:
                if self._date_now() < ddl['date']:
                    ddl['effect'] = True
                else:
                    ddl['effect'] = False
            else:
                if self._date_now() < ddl['date']:
                    ddl['effect'] = True
                elif self._date_now() > ddl['date']:
                    ddl['effect'] = False
                else:
                    if self._time_now() < (ddl['timespan'][0], ddl['timespan'][1]):
                        ddl['effect'] = True
                    else:
                        ddl['effect'] = False
        if self.settings['sort rule'] == IMPORTANCE_PRIORITY:  # chose a sort tule
            ddlCmp = self._ddlCmp_importance
        elif self.settings['sort rule'] == TIME_REMAIN_PRIORITY:
            ddlCmp = self._ddlCmp_timeremain
        self.ddlList.sort(key=cmp_to_key(ddlCmp))
        turn_warning_flag = False  # mark turn warning ddl
        for i, ddl in enumerate(self.ddlList):
            self.ddlTableWidget.setItem(i, 0, QTableWidgetItem(ddl['name']))
            self.ddlTableWidget.setItem(i, 1, QTableWidgetItem('{:04d}-{:02d}-{:02d}'.format(ddl['date'][0], ddl['date'][1], ddl['date'][2])))
            self.ddlTableWidget.setItem(i, 2, QTableWidgetItem('{:02d}:{:02d}-{:02d}:{:02d}'.format(ddl['timespan'][0], ddl['timespan'][1], ddl['timespan'][2], ddl['timespan'][3]) if ddl['timespan'] != ALL_DAY_TUPLE else '全天'))
            self.ddlTableWidget.setItem(i, 3, QTableWidgetItem(ddl['location']))
            if ddl['importance'] == 0:
                emergent_num += 1
                self.ddlTableWidget.setItem(i, 4, QTableWidgetItem('紧急'))
                self.ddlTableWidget.item(i, 4).setBackground(QBrush(QCOLOR_RED))
                if self._date_not_colored(self._date_tuple2QDate(ddl['date'])):
                    self._draw_color_calendar(self._date_tuple2QDate(ddl['date']), QCOLOR_RED)
            elif ddl['importance'] == 1:
                important_num += 1
                self.ddlTableWidget.setItem(i, 4, QTableWidgetItem('重要'))
                self.ddlTableWidget.item(i, 4).setBackground(QBrush(QCOLOR_ORANGE))
                if self._date_not_colored(self._date_tuple2QDate(ddl['date'])):
                    self._draw_color_calendar(self._date_tuple2QDate(ddl['date']), QCOLOR_ORANGE)
            elif ddl['importance'] == 2:
                self.ddlTableWidget.setItem(i, 4, QTableWidgetItem('普通'))
                self.ddlTableWidget.item(i, 4).setBackground(QBrush(QCOLOR_BLUEGREEN))
                if self._date_not_colored(self._date_tuple2QDate(ddl['date'])):
                    self._draw_color_calendar(self._date_tuple2QDate(ddl['date']), QCOLOR_BLUEGREEN)
            else:
                raise Exception('Illegal importance={} !'.format(ddl['importance']))

            if ddl['effect']:
                if ddl['timespan'] != ALL_DAY_TUPLE:
                    ddl_datetime = datetime.datetime(ddl['date'][0], ddl['date'][1], ddl['date'][2], ddl['timespan'][0], ddl['timespan'][1])
                else:
                    ddl_datetime = datetime.datetime(ddl['date'][0], ddl['date'][1], ddl['date'][2], 0, 0)
                datetime_delta = ddl_datetime - self._datetime_now()
                if datetime_delta.seconds + datetime_delta.days * 3600 * 24 < earliest_count_down_seconds + earliest_count_down_days * 3600 * 24:  # update earliest and latest count down seconds
                    earliest_count_down_seconds = datetime_delta.seconds
                    earliest_count_down_days = datetime_delta.days
                    earliest_count_down_name = ddl['name']
                if datetime_delta.seconds + datetime_delta.days * 3600 * 24 > latest_count_down_seconds + latest_count_down_days * 3600 * 24:
                    latest_count_down_seconds = datetime_delta.seconds
                    latest_count_down_days = datetime_delta.days
                count_down_time = [datetime_delta.days, datetime_delta.seconds//3600, (datetime_delta.seconds-datetime_delta.seconds//3600*3600)//60]
                self.ddlTableWidget.setItem(i, 5, QTableWidgetItem('{} 天 {} 小时 {} 分'.format(
                    count_down_time[0], count_down_time[1], count_down_time[2])))
                self.ddlTableWidget.item(i, 5).setBackground(QBrush(
                    QCOLOR_YELLOWGREEN if count_down_time >= self.settings['count down warning time'] else QCOLOR_YELLOW
                ))
                ddl['count down time'] = count_down_time

                if count_down_time < self.settings['count down warning time']:
                    if not ddl['turn warning']:
                        ddl['turn warning'] = True
                        turn_warning_flag = True
            else:
                invalid_num += 1
                self.ddlTableWidget.setItem(i, 5, QTableWidgetItem('过期'))
                self.ddlTableWidget.item(i, 5).setBackground(QBrush(QCOLOR_GREY))
                self._draw_color_calendar(self._date_tuple2QDate(ddl['date']), QCOLOR_GREY)

            self.ddlTableWidget.setItem(i, 6, QTableWidgetItem('未完成' if not ddl['complete'] else '已完成'))
            self.ddlTableWidget.item(i, 6).setBackground(QBrush(QCOLOR_LIGHTGREEN if ddl['complete'] else QCOLOR_LIGHTORANGE))

        if earliest_count_down_seconds != +inf:
            earliest_count_down = '{} 天 {} 小时 {} 分'.format(
                earliest_count_down_days, earliest_count_down_seconds // 3600,
                                     (earliest_count_down_seconds - earliest_count_down_seconds // 3600 * 3600) // 60)
        self.statistics['earliest ddl'] = earliest_count_down_name
        self.statistics['earliest count down'] = earliest_count_down
        if latest_count_down_seconds != 0:
            latest_count_down = '{} 天 {} 小时 {} 分'.format(
                latest_count_down_days, latest_count_down_seconds // 3600,
                                     (latest_count_down_seconds - latest_count_down_seconds // 3600 * 3600) // 60)
        self.statistics['latest count down'] = latest_count_down

        self.statistics['invalid'] = invalid_num
        self.statistics['emergent'] = emergent_num
        self.statistics['important'] = important_num
        self.statistics['remain'] = self.statistics['number'] - self.statistics['invalid']

        if self.settings['count down warning win'] and turn_warning_flag and not showWarnTip:
            self.showWarnCountTimeWin()


    def noticeUpdate(self):
        self.ddlNumLineEdit.setReadOnly(False)
        self.ddlTimeLineEdit.setReadOnly(False)
        self.ddlNameLineEdit.setReadOnly(False)
        self.ddlOldLineEdit.setReadOnly(False)
        self.emNumLineEdit.setReadOnly(False)
        self.imNumLineEdit.setReadOnly(False)
        self.lateTimeLineEdit.setReadOnly(False)
        self.remNumLineEdit.setReadOnly(False)

        self.ddlNumLineEdit.setText('{}'.format(self.statistics['number']))
        self.ddlTimeLineEdit.setText('{}'.format(self.statistics['earliest count down']))
        self.ddlNameLineEdit.setText('{}'.format(self.statistics['earliest ddl']))
        self.ddlOldLineEdit.setText('{}'.format(self.statistics['invalid']))
        self.emNumLineEdit.setText('{}'.format(self.statistics['emergent']))
        self.imNumLineEdit.setText('{}'.format(self.statistics['important']))
        self.lateTimeLineEdit.setText('{}'.format(self.statistics['latest count down']))
        self.remNumLineEdit.setText('{}'.format(self.statistics['remain']))

        self.ddlNumLineEdit.setReadOnly(True)
        self.ddlTimeLineEdit.setReadOnly(True)
        self.ddlNameLineEdit.setReadOnly(True)
        self.ddlOldLineEdit.setReadOnly(True)
        self.emNumLineEdit.setReadOnly(True)
        self.imNumLineEdit.setReadOnly(True)
        self.lateTimeLineEdit.setReadOnly(True)
        self.remNumLineEdit.setReadOnly(True)

    def ddlTableInit(self):
        if os.path.exists('ddl.csv'):
            with open('ddl.csv', 'r') as f:
                ddl_list_t = csv.reader(f)
                for ddl_item_t in ddl_list_t:
                    self.ddlTableAddRow(ddl_item_t[0], eval(ddl_item_t[1]), eval(ddl_item_t[2]), ddl_item_t[3], eval(ddl_item_t[4]), eval(ddl_item_t[5]))
                    self.ddlSet.add(ddl_item_t[0])
        self.ddlTableWidget.setRowCount(len(self.ddlList))
        self.main_update(showWarnTip=True)

    def settingInit(self):
        if os.path.exists('config'):
            with open('config', 'rb') as f:
                self.settings = pickle.load(f)

    def setSortRuleAction(self, sortRule):
        self.settings['sort rule'] = sortRule

    def setWarnAction(self, wday, whour, wminute, wshow, tshow):
        self.settings['count down warning time'] = [wday, whour, wminute]
        self.settings['count down warning win'] = wshow
        self.settings['show toast'] = IS_WIN10_SYS and tshow

    def setRemTrayAction(self, is_remembered):
        self.settings['remember close action'] = is_remembered

    def setCloseAction(self, action: int):
        if action == CLOSE_ACTION:
            self.settings['minimize'] = False
        elif action == MINIMIZE_ACTION:
            self.settings['minimize'] = True

    def alterCompleteAction(self):
        row_index = self.ddlTableWidget.currentRow()
        if self.ddlList[row_index]['complete']:
            judgment = QMessageBox.question(self, '更改确定', '是否更改为未完成？')
            if judgment == QMessageBox.Yes:
                self.ddlList[row_index]['complete'] = False
                self.ddlModified = True
                self.completePushButton.setText('标记为已完成')
                self.main_update()
        else:
            judgment = QMessageBox.question(self, '更改确定', '是否更改为已完成？')
            if judgment == QMessageBox.Yes:
                self.ddlList[row_index]['complete'] = True
                self.ddlModified = True
                self.completePushButton.setText('标记为未完成')
                self.main_update()

    def showInfo(self):
        QMessageBox.information(self, '关于本软件', 'ddl拯救者 (版本 v0.1.2)\n作者：徐大仙\nE-mail: xenon_xu@qq.com')

    def minimize_to_tray(self):
        self.hide()
        # self.trayicon.show()

    def recover_from_tray(self):
        self.show()
        # self.trayicon.hide()

    def ask_before_close(self):
        if self.ddlModified:
            judgment = QMessageBox.question(self, '退出', 'DDL修改未经保存，是否确认退出？')
            if judgment == QMessageBox.Yes:
                self.trayicon.hide()
                qApp.quit()
        else:
            self.trayicon.hide()
            qApp.quit()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        if not self.settings['remember close action']:
            a0.ignore()
            self.trayQuestionDialog.trayRadioButton.setChecked(True)
            self.trayQuestionDialog.show()
        else:
            if self.settings['minimize']:
                a0.ignore()
                self.minimize_to_tray()
            else:
                self.ask_before_close()


class addDdlWin(QDialog, Ui_addDdlDialog):

    addDdlWinSignal = pyqtSignal(str, int, int, int, int, int, int, int, str, int)
    modDdlWinSignal = pyqtSignal(str, int, int, int, int, int, int, int, str, int)
    # name date time location importance

    def __init__(self, parent=None):
        super(addDdlWin, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(Qt.WindowTitleHint)

        self.modify = False
        self.modify_index = 0

        self.ddlSet = set()

    def update_ddlSet(self, new_ddlSet):
        self.ddlSet = new_ddlSet

    def enable_time_set(self):
        if self.wholeDayCheckBox.isChecked():
            self.timeEdit1.setEnabled(False)
            self.timeEdit2.setEnabled(False)
        else:
            self.timeEdit1.setEnabled(True)
            self.timeEdit2.setEnabled(True)


    def accept(self) -> None:
        name = self.nameLineEdit.text()
        date = (self.dateEdit.date().year(), self.dateEdit.date().month(), self.dateEdit.date().day())
        if self.wholeDayCheckBox.isChecked():
            timespan = ALL_DAY_TUPLE
        else:
            timespan = (self.timeEdit1.time().hour(), self.timeEdit1.time().minute(), self.timeEdit2.time().hour(), self.timeEdit2.time().minute())
        location = self.locationLineEdit.text()
        importance = self.importanceComboBox.currentIndex()

        if name == '':
            QMessageBox.critical(self, '错误', '名称不能为空！')
        elif not self.modify and name in self.ddlSet:
            QMessageBox.critical(self, '错误', '名称不能重复！')
        elif timespan[0:2] > timespan[2:4]:
            QMessageBox.critical(self, '错误', '时间段范围错误！')
        else:
            if not self.modify:
                self.addDdlWinSignal.emit(
                    name, date[0], date[1], date[2], timespan[0], timespan[1], timespan[2], timespan[3], location, importance)
            else:
                self.modDdlWinSignal.emit(
                    name, date[0], date[1], date[2], timespan[0], timespan[1], timespan[2], timespan[3], location, importance)
            self.hide()


class setWin(QDialog, Ui_setWin):

    setSortRuleSignal = pyqtSignal(int)
    setWarnSignal = pyqtSignal(int, int, int, bool, bool)
    showWarnWinButtonPressSignal = pyqtSignal()
    remTrayCheckedSignal = pyqtSignal(bool)
    setFinishedSignal = pyqtSignal()

    def __init__(self, parent=None):
        super(setWin, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(Qt.WindowTitleHint)
        if not IS_WIN10_SYS:
            self.warningWinCheckBox.setChecked(False)
            self.warningWinCheckBox.setEnabled(False)

    def showWarnWinButtonPressAction(self):
        self.showWarnWinButtonPressSignal.emit()

    def setWarnSignalEmit(self):
        self.setWarnSignal.emit(
            self.countDownDaySpinBox.value(), self.countDownHourSpinBox.value(),
            self.countDownMinuteSpinBox.value(), self.warningWinCheckBox.isChecked(),
            self.warningToastCheckBox.isChecked())

    def accept(self) -> None:
        self.setSortRuleSignal.emit(self.sortRuleComboBox.currentIndex())
        self.setWarnSignalEmit()
        self.remTrayCheckedSignal.emit(self.remTrayCheckBox.isChecked())

        self.setFinishedSignal.emit()
        self.hide()


class trayQuestionDialog(QDialog, Ui_trayQuestionDialog):

    rememberTrayChoiceSignal = pyqtSignal(bool)
    setCloseActionSignal = pyqtSignal(int)
    minimizeToTraySignal = pyqtSignal()
    exitSignal = pyqtSignal()
    settingSaveActionSignal = pyqtSignal()

    def __init__(self, parent=None):
        super(trayQuestionDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowTitleHint)

    def accept(self) -> None:
        if self.trayRadioButton.isChecked():  # main window to tray
            self.setCloseActionSignal.emit(MINIMIZE_ACTION)
            self.minimizeToTraySignal.emit()
        elif self.exitRadioButton.isChecked():  # exit main window
            self.setCloseActionSignal.emit(CLOSE_ACTION)
            self.exitSignal.emit()
        self.rememberTrayChoiceSignal.emit(self.remCheckBox.isChecked())  # remember choice
        self.settingSaveActionSignal.emit()
        self.hide()

    def reject(self) -> None:
        self.hide()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MainWin()
    myWin.show()
    if myWin.settings['count down warning win']:
        myWin.showWarnCountTimeWin()
    sys.exit(app.exec_())
