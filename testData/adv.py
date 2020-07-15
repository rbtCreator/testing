# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adv.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 370)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(700, 370))
        Form.setMaximumSize(QtCore.QSize(700, 370))
        Form.setMouseTracking(False)
        Form.setFocusPolicy(QtCore.Qt.StrongFocus)
        Form.setStyleSheet("background-color: rgb(85, 87, 83);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 10, 350, 60))
        font = QtGui.QFont()
        font.setFamily("Abyssinica SIL")
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(211, 215, 207);")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 10, 350, 60))
        font = QtGui.QFont()
        font.setFamily("Abyssinica SIL")
        font.setPointSize(13)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(87, 5, 5);")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(0, 70, 700, 250))
        font = QtGui.QFont()
        font.setFamily("Abyssinica SIL")
        font.setPointSize(13)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color: rgb(232, 227, 227);")
        self.textEdit.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.textEdit.setTabStopWidth(80)
        self.textEdit.setObjectName("textEdit")
        self.changeRight = QtWidgets.QPushButton(Form)
        self.changeRight.setGeometry(QtCore.QRect(350, 320, 350, 50))
        self.changeRight.setMinimumSize(QtCore.QSize(350, 50))
        self.changeRight.setMaximumSize(QtCore.QSize(350, 50))
        font = QtGui.QFont()
        font.setFamily("Abyssinica SIL")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.changeRight.setFont(font)
        self.changeRight.setStyleSheet("color: rgb(211, 215, 207);")
        self.changeRight.setFlat(True)
        self.changeRight.setObjectName("changeRight")
        self.changeLeft = QtWidgets.QPushButton(Form)
        self.changeLeft.setGeometry(QtCore.QRect(0, 320, 350, 50))
        self.changeLeft.setMinimumSize(QtCore.QSize(350, 50))
        self.changeLeft.setMaximumSize(QtCore.QSize(350, 50))
        font = QtGui.QFont()
        font.setFamily("Abyssinica SIL")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.changeLeft.setFont(font)
        self.changeLeft.setStyleSheet("color: rgb(211, 215, 207);")
        self.changeLeft.setFlat(True)
        self.changeLeft.setObjectName("changeLeft")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "фразы (1 из 12)"))
        self.pushButton_2.setText(_translate("Form", "советы (1 из 10)"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Abyssinica SIL\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit.setPlaceholderText(_translate("Form", "   для завершения ввода нажмите   ESC"))
        self.changeRight.setText(_translate("Form", ">"))
        self.changeLeft.setText(_translate("Form", "<"))

