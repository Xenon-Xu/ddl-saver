# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWin.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1284, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/图标/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.cldGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.cldGroupBox.sizePolicy().hasHeightForWidth())
        self.cldGroupBox.setSizePolicy(sizePolicy)
        self.cldGroupBox.setMouseTracking(True)
        self.cldGroupBox.setObjectName("cldGroupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.cldGroupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.cldGroupBox)
        self.calendarWidget.setMouseTracking(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_5.addWidget(self.calendarWidget, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.cldGroupBox, 0, 2, 1, 1)
        self.noticeGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.noticeGroupBox.sizePolicy().hasHeightForWidth())
        self.noticeGroupBox.setSizePolicy(sizePolicy)
        self.noticeGroupBox.setObjectName("noticeGroupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.noticeGroupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ddlNumLineEdit = QtWidgets.QLineEdit(self.noticeGroupBox)
        self.ddlNumLineEdit.setReadOnly(True)
        self.ddlNumLineEdit.setObjectName("ddlNumLineEdit")
        self.gridLayout_2.addWidget(self.ddlNumLineEdit, 3, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.noticeGroupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 4, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.noticeGroupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.ddlOldLineEdit = QtWidgets.QLineEdit(self.noticeGroupBox)
        self.ddlOldLineEdit.setReadOnly(True)
        self.ddlOldLineEdit.setObjectName("ddlOldLineEdit")
        self.gridLayout_2.addWidget(self.ddlOldLineEdit, 4, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.noticeGroupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 3, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.noticeGroupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 4, 1, 1)
        self.emNumLineEdit = QtWidgets.QLineEdit(self.noticeGroupBox)
        self.emNumLineEdit.setReadOnly(True)
        self.emNumLineEdit.setObjectName("emNumLineEdit")
        self.gridLayout_2.addWidget(self.emNumLineEdit, 0, 6, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.noticeGroupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.noticeGroupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 5, 1, 1)
        self.lateTimeLineEdit = QtWidgets.QLineEdit(self.noticeGroupBox)
        self.lateTimeLineEdit.setReadOnly(True)
        self.lateTimeLineEdit.setObjectName("lateTimeLineEdit")
        self.gridLayout_2.addWidget(self.lateTimeLineEdit, 3, 6, 1, 1)
        self.imNumLineEdit = QtWidgets.QLineEdit(self.noticeGroupBox)
        self.imNumLineEdit.setReadOnly(True)
        self.imNumLineEdit.setObjectName("imNumLineEdit")
        self.gridLayout_2.addWidget(self.imNumLineEdit, 2, 6, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 3, 4, 1, 1)
        self.ddlTimeLineEdit = QtWidgets.QLineEdit(self.noticeGroupBox)
        self.ddlTimeLineEdit.setReadOnly(True)
        self.ddlTimeLineEdit.setObjectName("ddlTimeLineEdit")
        self.gridLayout_2.addWidget(self.ddlTimeLineEdit, 2, 3, 1, 1)
        self.ddlNameLineEdit = QtWidgets.QLineEdit(self.noticeGroupBox)
        self.ddlNameLineEdit.setReadOnly(True)
        self.ddlNameLineEdit.setObjectName("ddlNameLineEdit")
        self.gridLayout_2.addWidget(self.ddlNameLineEdit, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.noticeGroupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.noticeGroupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 1, 1, 1)
        self.remNumLineEdit = QtWidgets.QLineEdit(self.noticeGroupBox)
        self.remNumLineEdit.setReadOnly(True)
        self.remNumLineEdit.setObjectName("remNumLineEdit")
        self.gridLayout_2.addWidget(self.remNumLineEdit, 4, 6, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 7, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 2, 7, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 3, 7, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 4, 7, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.noticeGroupBox, 1, 0, 1, 1)
        self.ddlGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.ddlGroupBox.sizePolicy().hasHeightForWidth())
        self.ddlGroupBox.setSizePolicy(sizePolicy)
        self.ddlGroupBox.setObjectName("ddlGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.ddlGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.ddlTableWidget = QtWidgets.QTableWidget(self.ddlGroupBox)
        self.ddlTableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.ddlTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ddlTableWidget.setAlternatingRowColors(True)
        self.ddlTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.ddlTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ddlTableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.ddlTableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.ddlTableWidget.setObjectName("ddlTableWidget")
        self.ddlTableWidget.setColumnCount(6)
        self.ddlTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ddlTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ddlTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ddlTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ddlTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ddlTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.ddlTableWidget.setHorizontalHeaderItem(5, item)
        self.ddlTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.ddlTableWidget.horizontalHeader().setDefaultSectionSize(135)
        self.ddlTableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.ddlTableWidget, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.ddlGroupBox, 0, 0, 1, 1)
        self.ctrlGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ctrlGroupBox.sizePolicy().hasHeightForWidth())
        self.ctrlGroupBox.setSizePolicy(sizePolicy)
        self.ctrlGroupBox.setObjectName("ctrlGroupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.ctrlGroupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.setPushButton = QtWidgets.QPushButton(self.ctrlGroupBox)
        self.setPushButton.setObjectName("setPushButton")
        self.gridLayout_3.addWidget(self.setPushButton, 3, 1, 1, 2)
        self.delPushButton = QtWidgets.QPushButton(self.ctrlGroupBox)
        self.delPushButton.setEnabled(False)
        self.delPushButton.setObjectName("delPushButton")
        self.gridLayout_3.addWidget(self.delPushButton, 2, 2, 1, 1)
        self.addPushButton = QtWidgets.QPushButton(self.ctrlGroupBox)
        self.addPushButton.setObjectName("addPushButton")
        self.gridLayout_3.addWidget(self.addPushButton, 1, 1, 1, 1)
        self.savePushButton = QtWidgets.QPushButton(self.ctrlGroupBox)
        self.savePushButton.setObjectName("savePushButton")
        self.gridLayout_3.addWidget(self.savePushButton, 2, 1, 1, 1)
        self.modPushButton = QtWidgets.QPushButton(self.ctrlGroupBox)
        self.modPushButton.setEnabled(False)
        self.modPushButton.setObjectName("modPushButton")
        self.gridLayout_3.addWidget(self.modPushButton, 1, 2, 1, 1)
        self.selectLineEdit = QtWidgets.QLineEdit(self.ctrlGroupBox)
        self.selectLineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectLineEdit.sizePolicy().hasHeightForWidth())
        self.selectLineEdit.setSizePolicy(sizePolicy)
        self.selectLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.selectLineEdit.setObjectName("selectLineEdit")
        self.gridLayout_3.addWidget(self.selectLineEdit, 0, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.ctrlGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 1, 1, 1)
        self.gridLayout_7.addWidget(self.ctrlGroupBox, 1, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_7.addWidget(self.line, 0, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_7.addWidget(self.line_2, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1284, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.showInfoAction = QtWidgets.QAction(MainWindow)
        self.showInfoAction.setObjectName("showInfoAction")
        self.menu.addAction(self.showInfoAction)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.addPushButton.clicked.connect(MainWindow.showAddDdlWin)
        self.modPushButton.clicked.connect(MainWindow.showAddDdlWin_mod)
        self.delPushButton.clicked.connect(MainWindow.delDdlAction)
        self.ddlTableWidget.currentItemChanged['QTableWidgetItem*','QTableWidgetItem*'].connect(MainWindow.selectDdlAction)
        self.savePushButton.clicked.connect(MainWindow.saveDdlAction)
        self.calendarWidget.clicked['QDate'].connect(MainWindow.selectDdlRow)
        self.setPushButton.clicked.connect(MainWindow.showSetWin)
        self.showInfoAction.triggered.connect(MainWindow.showInfo)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DDL拯救者"))
        self.cldGroupBox.setTitle(_translate("MainWindow", "日历"))
        self.noticeGroupBox.setTitle(_translate("MainWindow", "公告板"))
        self.label_6.setText(_translate("MainWindow", "重要DDL个数"))
        self.label.setText(_translate("MainWindow", "最早DDL名称"))
        self.label_8.setText(_translate("MainWindow", "最晚DDL倒计时"))
        self.label_2.setText(_translate("MainWindow", "DDL总数"))
        self.label_5.setText(_translate("MainWindow", "剩余DDL个数"))
        self.label_7.setText(_translate("MainWindow", "紧急DDL个数"))
        self.label_4.setText(_translate("MainWindow", "最早DDL倒计时"))
        self.label_3.setText(_translate("MainWindow", "过期DDL个数"))
        self.ddlGroupBox.setTitle(_translate("MainWindow", "DDL查看"))
        item = self.ddlTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "名称"))
        item = self.ddlTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "日期"))
        item = self.ddlTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "时间"))
        item = self.ddlTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "地点"))
        item = self.ddlTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "重要性"))
        item = self.ddlTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "倒计时"))
        self.ctrlGroupBox.setTitle(_translate("MainWindow", "控制台"))
        self.setPushButton.setText(_translate("MainWindow", "设置"))
        self.delPushButton.setText(_translate("MainWindow", "删除"))
        self.addPushButton.setText(_translate("MainWindow", "添加"))
        self.savePushButton.setText(_translate("MainWindow", "保存"))
        self.modPushButton.setText(_translate("MainWindow", "修改"))
        self.selectLineEdit.setText(_translate("MainWindow", "DDL 名称"))
        self.label_9.setText(_translate("MainWindow", "当前选择→"))
        self.menu.setTitle(_translate("MainWindow", "帮助"))
        self.action.setText(_translate("MainWindow", "设置"))
        self.action_3.setText(_translate("MainWindow", "退出"))
        self.showInfoAction.setText(_translate("MainWindow", "关于本软件"))
import source_rc