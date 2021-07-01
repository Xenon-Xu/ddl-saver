import sys
from PyQt5.QtWidgets import QApplication, QMenu, QSystemTrayIcon, QAction, qApp
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal


class TrayIcon(QSystemTrayIcon):

    exitSignal = pyqtSignal()
    openSignal = pyqtSignal()
    traySignal = pyqtSignal()

    def __init__(self, parent=None):
        super(TrayIcon, self).__init__(parent)
        self.menu = QMenu(QApplication.desktop())
        self.openAction = QAction('打开主界面', self, triggered=self.open)
        self.trayAction = QAction('最小化到托盘', self, triggered=self.to_tray)
        self.quitAction = QAction('退出', self, triggered=self.quit)

        self.menu.addAction(self.openAction)
        self.menu.addAction(self.trayAction)
        self.menu.addSeparator()
        self.menu.addAction(self.quitAction)
        self.setContextMenu(self.menu)

        self.activated.connect(self.iconClickedAction)  # 把鼠标点击图标的信号和槽连接
        self.setIcon(QIcon("icon.ico"))
        self.icon = self.MessageIcon()

    def iconClickedAction(self, reason):
        if reason in [2, 3]:  # 2->double clicked 3->left clicked
            self.open()

    def open(self):
        self.openSignal.emit()

    def to_tray(self):
        self.traySignal.emit()

    def quit(self):
        """completely quit"""
        self.exitSignal.emit()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ti = TrayIcon()
#     ti.show()
#     sys.exit(app.exec_())
