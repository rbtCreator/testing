# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
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
        font = QtGui.QFont()
        font.setFamily("Sans")
        Form.setFont(font)
        self.test_name = QtWidgets.QLabel(Form)
        self.test_name.setGeometry(QtCore.QRect(110, 90, 921, 55))
        font = QtGui.QFont()
        font.setFamily("Lohit Tamil")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.test_name.setFont(font)
        self.test_name.setTextFormat(QtCore.Qt.AutoText)
        self.test_name.setAlignment(QtCore.Qt.AlignCenter)
        self.test_name.setObjectName("test_name")
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
        self.result = QtWidgets.QLabel(Form)
        self.result.setGeometry(QtCore.QRect(390, 230, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans Condensed")
        font.setPointSize(20)
        self.result.setFont(font)
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.result.setObjectName("result")
        self.res_per = QtWidgets.QLabel(Form)
        self.res_per.setGeometry(QtCore.QRect(360, 340, 381, 31))
        self.res_per.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.res_per.setObjectName("res_per")
        self.butt = QtWidgets.QPushButton(Form)
        self.butt.setGeometry(QtCore.QRect(470, 560, 170, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butt.sizePolicy().hasHeightForWidth())
        self.butt.setSizePolicy(sizePolicy)
        self.butt.setMinimumSize(QtCore.QSize(170, 0))
        self.butt.setMaximumSize(QtCore.QSize(170, 16777215))
        self.butt.setObjectName("butt")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(350, 440, 67, 17))
        self.label.setObjectName("label")
        self.advice = QtWidgets.QLabel(Form)
        self.advice.setGeometry(QtCore.QRect(420, 390, 411, 111))
        self.advice.setObjectName("advice")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.test_name.setText(_translate("Form", "Тестирование  по Истории войск связи"))
        self.VAS.setText(_translate("Form", "TextLabel"))
        self.result.setText(_translate("Form", "Результат тестирования"))
        self.res_per.setText(_translate("Form", "Решено: 33%  (12 из 15)"))
        self.butt.setText(_translate("Form", "завершить"))
        self.label.setText(_translate("Form", "СОВЕТ:"))
        self.advice.setText(_translate("Form", "Очень серьезный совет, совет способный \n"
"переврнуть все понимание бытия\n"
"with man who really care for his life"))

