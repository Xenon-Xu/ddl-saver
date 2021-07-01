# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trayQuestionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_trayQuestionDialog(object):
    def setupUi(self, trayQuestionDialog):
        trayQuestionDialog.setObjectName("trayQuestionDialog")
        trayQuestionDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        trayQuestionDialog.resize(318, 195)
        trayQuestionDialog.setSizeIncrement(QtCore.QSize(305, 190))
        trayQuestionDialog.setBaseSize(QtCore.QSize(305, 190))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/图标/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        trayQuestionDialog.setWindowIcon(icon)
        trayQuestionDialog.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.verticalLayout = QtWidgets.QVBoxLayout(trayQuestionDialog)
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 3, 1, 1)
        self.label = QtWidgets.QLabel(trayQuestionDialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.exitRadioButton = QtWidgets.QRadioButton(trayQuestionDialog)
        self.exitRadioButton.setObjectName("exitRadioButton")
        self.gridLayout.addWidget(self.exitRadioButton, 3, 1, 1, 2)
        self.trayRadioButton = QtWidgets.QRadioButton(trayQuestionDialog)
        self.trayRadioButton.setChecked(True)
        self.trayRadioButton.setObjectName("trayRadioButton")
        self.gridLayout.addWidget(self.trayRadioButton, 2, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.widget = QtWidgets.QWidget(trayQuestionDialog)
        self.widget.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"")
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.remCheckBox = QtWidgets.QCheckBox(self.widget)
        self.remCheckBox.setObjectName("remCheckBox")
        self.gridLayout_4.addWidget(self.remCheckBox, 2, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_4.addWidget(self.buttonBox, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(trayQuestionDialog)
        self.buttonBox.accepted.connect(trayQuestionDialog.accept)
        self.buttonBox.rejected.connect(trayQuestionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(trayQuestionDialog)

    def retranslateUi(self, trayQuestionDialog):
        _translate = QtCore.QCoreApplication.translate
        trayQuestionDialog.setWindowTitle(_translate("trayQuestionDialog", "关闭提示"))
        self.label.setText(_translate("trayQuestionDialog", "选择关闭按钮动作："))
        self.exitRadioButton.setText(_translate("trayQuestionDialog", "退出程序"))
        self.trayRadioButton.setText(_translate("trayQuestionDialog", "最小化到托盘"))
        self.remCheckBox.setText(_translate("trayQuestionDialog", "记住我的选项"))
import source_rc
