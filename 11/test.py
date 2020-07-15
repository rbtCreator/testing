#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#add path with necessary files to python
import sys, os

path = os.path.abspath(__file__)
curdir = os.path.dirname(path)
curdir = os.path.split(curdir)[0]
sys.path.insert(0, os.path.join(curdir, "admin", 'testData'))
sys.path.insert(0, os.path.join(curdir, "admin", 'config'))


#import necessary libraries for initiating Qt_object
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QByteArray, QEvent

import csv

#design
import forms




class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.phr = None
        self.path = os.path.abspath(os.curdir)
        self.img = QtGui.QImage(os.path.join(os.path.split(self.path)[0], "admin", "testData", "img.jpeg"))
        self.resultWin = forms.ResultWin(self.setPhrases, self.img)
        self.questForm = forms.QuestForm(self.showResult, self.img)
        self.questForm.setPhrases(self.phr)
        self.startWindow = forms.StartWindow(self.testStart, self.setData, self.img)

        self.name = None
        self.number = None
        self.resultWin.setDocName(os.path.split(self.path)[1] + ".xlsx")

        self.startWindow.show()

    def testStart(self, name, number):
        self.startWindow.hide()
        self.name = name
        self.number = number
        self.questForm.timerStart()
        self.questForm.show()

    def setPhrases(self, phr):
        self.phr = phr

    def showResult(self, choice):
        self.questForm.hide()
        self.resultWin.setNameNumber(self.name, self.number)
        self.resultWin.setUserChoice(choice)
        self.resultWin.show()

    def setData(self, data):
        self.questForm.setData(data)
        self.resultWin.setData(data)

    def getData(self):
        return self.testData

    

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
