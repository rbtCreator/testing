# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1110, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1110, 700))
        Form.setMaximumSize(QtCore.QSize(1110, 700))
        self.VAS = QtWidgets.QLabel(Form)
        self.VAS.setGeometry(QtCore.QRect(10, 60, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VAS.sizePolicy().hasHeightForWidth())
        self.VAS.setSizePolicy(sizePolicy)
        self.VAS.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.VAS.setFont(font)
        self.VAS.setMouseTracking(False)
        self.VAS.setAlignment(QtCore.Qt.AlignCenter)
        self.VAS.setObjectName("VAS")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(460, 200, 200, 320))
        self.pushButton.setMinimumSize(QtCore.QSize(200, 320))
        self.pushButton.setMaximumSize(QtCore.QSize(200, 320))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(74, 12, 12);")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(740, 200, 200, 320))
        self.pushButton_2.setMinimumSize(QtCore.QSize(200, 320))
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 320))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(74, 12, 12);")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(250, 90, 641, 71))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(74, 12, 12);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 200, 200, 320))
        self.pushButton_3.setMinimumSize(QtCore.QSize(200, 320))
        self.pushButton_3.setMaximumSize(QtCore.QSize(200, 320))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(74, 12, 12);")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.VAS.setText(_translate("Form", "TextLabel"))
        self.pushButton.setText(_translate("Form", "Создать новый\n"
"тест"))
        self.pushButton_2.setText(_translate("Form", "Отредактировать\n"
"тест"))
        self.label.setText(_translate("Form", "РЕДАКТОР ФОРМ ТЕСТИРОВАНИЯ"))
        self.pushButton_3.setText(_translate("Form", "редактировать\n"
"фразы"))

