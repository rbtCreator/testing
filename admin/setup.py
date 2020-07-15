#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#add path with necessary files to python
import sys, os

path = os.path.abspath(__file__)
curdir = os.path.dirname(path)
sys.path.insert(0, os.path.join(curdir, 'setupData'))
PATH = os.path.split(curdir)[0]
sys.path.insert(0, os.path.join(curdir, 'testData', 'config'))


#import necessary libraries for initiating Qt_object
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QByteArray, QEvent, QTimer

import csv
import random
import math

#design
import test_create
import start
import popup
import adv




class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.startWindow = StartWindow(self.openTestForm, self.advWindowShow)
        self.testCreate = InitWindow(self.test_creation_finished)
        self.adviceWindow = None
        
        #self.width = QtWidgets.QApplication.instance().desktop().availableGeometry().width()
        #self.height = QtWidgets.QApplication.instance().desktop().availableGeometry().height()
        self.width = QtWidgets.QApplication.desktop().width()
        self.height = QtWidgets.QApplication.desktop().height()
        self.startWindow.move(self.width//2 -555, self.height//2 -350)
        self.startWindow.popup.move(self.width//2 -200, self.height//2 -75)
        self.testCreate.move(self.width//2 -555, self.height//2 -350)
        self.testCreate.popup.move(self.width//2 -200, self.height//2 -75)
        

        self.startWindow.show()


    def advWindowShow(self):
        self.startWindow.hide()
        self.adviceWindow = AdviceWindow()
        self.adviceWindow.move(self.width//2 -350, self.height//2 -160)
        self.adviceWindow.show()

    def openTestForm(self, fileName=None, count=None, time=None):
        self.startWindow.hide()
        if not fileName is None:
            self.testCreate.pull_in_data(fileName)
        else:
            self.testCreate.pitch_size = count
            self.testCreate.time = time
            
        self.testCreate.show()

    def test_creation_finished(self):
        self.testCreate.hide()
        self.close()




class AdviceWindow(QtWidgets.QWidget, adv.Ui_Form):
    def __init__(self):
        super(AdviceWindow, self).__init__()
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.pushButton.idn = 0
        self.pushButton_2.idn = 1
        self.pushButton.clicked.connect(self.btnHandler)
        self.pushButton_2.clicked.connect(self.btnHandler)

        self.changeLeft.idn = 0
        self.changeRight.idn = 1
        self.changeLeft.clicked.connect(self.flip)
        self.changeRight.clicked.connect(self.flip)

        self.select = ["color: rgb(211, 215, 207);", "color: rgb(87, 5, 5);"]
        self.switcher = False # False - phr
        self.pos_adv = 0
        self.pos_phr = 0
        self.adv, self.phr = [], []
        self.tm = [0, 0] #[0] - timer started, [1] - times pressed

        self.readData()
        self.guiUpdate()
        
    def btnHandler(self):
        btn = self.sender()
        self.saveChanges()
        self.switcher = btn.idn
        self.guiUpdate()

    def flip(self):
        self.saveChanges()
        
        btn = self.sender()
        if btn.idn:
            if self.switcher:
                if self.pos_adv < 9: self.pos_adv += 1
            else:
                self.pos_phr += 1
                if self.pos_phr == len(self.phr):
                    self.phr.append("")
        else:
            if self.switcher:
                if self.pos_adv > 0: self.pos_adv -= 1
            else:
                if self.pos_phr > 0: self.pos_phr -= 1
                
        self.guiUpdate()

    def correctFilled(self):
        return True

    def saveChanges(self):
        text = self.textEdit.toPlainText()
        print(text)
        if self.switcher:
            self.adv[self.pos_adv] = text
        else:
            self.phr[self.pos_phr] = text

    def readData(self):
        with open(os.path.join(PATH, "testData", "adv.csv"), newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["adv"] != "-":
                    st = row["adv"]
                    st = st.replace("/", ",")
                    self.adv.append(st)
                if row["phr"] != "-":
                    st = row["phr"]
                    st = st.replace("/", ",")
                    self.phr.append(row["phr"])
        
    
    def writeData(self):
        with open(os.path.join(PATH, "testData", "adv.csv"), 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["adv", "phr"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            steps = len(self.adv)
            if steps < len(self.phr): steps = len(self.phr)

            writer.writeheader()
            for step in range(steps):
                if step < len(self.adv):
                    adv = self.adv[step]
                    adv = adv.replace(",", "/")
                else: adv = "-"

                if step < len(self.phr):
                    phr = self.phr[step]
                    adv = adv.replace(",", "/")
                else: phr = "-"
                writer.writerow({"adv": adv,
                                 "phr": phr})

    def dataCorretion(self):
        while True:
            if "" in self.phr:
                self.phr.remove("")
            else: break

        for i, el in enumerate(self.adv):
            if el == "": self.adv[i] = "????????????????"
            
                

    def guiUpdate(self):
        if self.switcher:
            self.textEdit.setPlainText(self.adv[self.pos_adv])
        else:
            self.textEdit.setPlainText(self.phr[self.pos_phr])

        self.pushButton.setText("фразы ({} из {})".format(self.pos_phr+1, len(self.phr)))
        self.pushButton_2.setText("cоветы ({} из 10)".format(self.pos_adv+1))
        self.pushButton.setStyleSheet(self.select[self.switcher])
        self.pushButton_2.setStyleSheet(self.select[not self.switcher])

        if self.pos_phr == 0 and not self.switcher :
            self.changeLeft.setStyleSheet("color: rgb(87, 5, 5);")
        elif self.pos_adv == 0 and self.switcher :
            self.changeLeft.setStyleSheet("color: rgb(87, 5, 5);")
        elif self.pos_adv == 9:
            self.changeRight.setStyleSheet("color: rgb(87, 5, 5);")
        else:
            self.changeLeft.setStyleSheet("color: rgb(211, 215, 207);")
            self.changeRight.setStyleSheet("color: rgb(211, 215, 207);")

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Message', "Закончить редактирование?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.saveChanges()
            self.dataCorretion()
            self.writeData()
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.modifiers() == Qt.ControlModifier:
            if event.key() == Qt.Key_S:
                self.close()
                 


class StartWindow(QtWidgets.QWidget, start.Ui_Form):
    def __init__(self, nextStepFunc=None, advStep=None):
        super(StartWindow, self).__init__()
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.advStep = advStep
        self.nextStepFunc = nextStepFunc

        self.pushButton.clicked.connect(self.createNew)
        self.pushButton_2.clicked.connect(self.editOne)
        self.pushButton_3.clicked.connect(self.advStep)

        self.img = QtGui.QImage(os.path.join(os.path.abspath(os.curdir), "setupData", "img.jpeg"))
        self.palette = QtGui.QPalette()
        self.palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(self.img))
        self.setPalette(self.palette)

        self.VAS.setText("")

        self.popup = InitPopup(self.get_count, isdigit=True)
        self.popup.label.setText("Количество вопросов")


    def createNew(self):
        self.popup.show()

    def get_count(self, count, time):
        self.popup.hide()
        self.nextStepFunc(count=count, time=time)

    def editOne(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Open File",
                                                     os.path.join(PATH, "testData", "configOld"),
                                                     "(*.csv)")
        if not file[0] == "":
            self.nextStepFunc(file[0])

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Message', "Прервать создание теста?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.popup.hide()
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()



class InitPopup(QtWidgets.QWidget, popup.Ui_Form):
    def __init__(self, step_func, isdigit=False):
        super(InitPopup, self).__init__()
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.lineEdit.setFocusPolicy(Qt.ClickFocus)

        self.step_func = step_func
        self.digit_mode = isdigit
        self.main_str = ""

        self.count = None

        self.flag = False

    def set_str_and_mode(self, st):
        self.main_str = st

    def get_name(self):
        if not self.flag:
            self.count = self.lineEdit.text()
            if self.count.isdigit():
                self.flag = not self.flag
                self.label.setText("Время выполнения в мин")
                self.lineEdit.setText("")
                self.count = int(self.count)
            else:
                self.lineEdit.setText("")
                self.lineEdit.setPlaceholderText("Введите число")
        else:
            time = self.lineEdit.text()
            if time == "":
                time = -1
                self.step_func(self.count, time)
            elif time.isdigit():
                self.step_func(self.count, int(time))
            else:
                self.lineEdit.setText("")
                self.lineEdit.setPlaceholderText("Введите число")

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Enter or e.key() == Qt.Key_Return:
            self.get_name()


            


class Popup(QtWidgets.QWidget, popup.Ui_Form):
    def __init__(self, step_func, isdigit=False):
        super(Popup, self).__init__()
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.lineEdit.setFocusPolicy(Qt.ClickFocus)

        self.step_func = step_func
        self.digit_mode = isdigit
        self.main_str = ""

    def set_str_and_mode(self, st):
        self.main_str = st

    def get_name(self):
        data = self.lineEdit.text()
        if self.digit_mode:
            if data.isdigit():
                self.step_func(int(data))
            else:
                self.lineEdit.setText("")
                self.lineEdit.setPlaceholderText("Введите число")
        else:
            self.step_func(data)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Enter or e.key() == Qt.Key_Return:
            self.get_name()

            
        

class InitWindow(QtWidgets.QWidget, test_create.Ui_Form):
    def __init__(self, finishFunc=None):
        super(InitWindow, self).__init__()
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        
        self.finishFunc = finishFunc
            
        self.pushButton.clicked.connect(self.next_step)
        self.pushButton_2.clicked.connect(self.prev_step)

        self.first_ans.toggled.connect(self.onSelect)
        self.first_ans.name = 0 #"first_ans"
        self.second_ans.toggled.connect(self.onSelect)
        self.second_ans.name = 1 #"second_ans"
        self.third_ans.toggled.connect(self.onSelect)
        self.third_ans.name = 2 #"third_ans"
        self.fourth_ans.toggled.connect(self.onSelect)
        self.fourth_ans.name = 3 #"fourth_ans"

        self.btn_group = QtWidgets.QButtonGroup()
        self.btn_group.addButton(self.first_ans)
        self.btn_group.addButton(self.second_ans)
        self.btn_group.addButton(self.third_ans)
        self.btn_group.addButton(self.fourth_ans)
        self.ans_add = False

        #test
        #self.name_edit.setAttribute(Qt.WA_TranslucentBackground) rgba(255, 255, 255, 20);
        self.name_edit.setStyleSheet("background-color: rgba(85, 70, 70, 85); color: rgb(226, 227, 245);")
        self.quest_text.setStyleSheet("background-color: rgba(85, 70, 70, 85); color: rgb(226, 227, 245);")
        self.q_one.setStyleSheet("background-color: rgba(85, 70, 70, 85); color: rgb(226, 227, 245);")
        self.q_two.setStyleSheet("background-color: rgba(85, 70, 70, 85); color: rgb(226, 227, 245);")
        self.q_three.setStyleSheet("background-color: rgba(85, 70, 70, 85); color: rgb(226, 227, 245);")
        self.q_four.setStyleSheet("background-color: rgba(85, 70, 70, 85); color: rgb(226, 227, 245);")
        self.pushButton.setStyleSheet("background-color: rgba(85, 70, 70, 85); color: rgb(226, 227, 245);")
        self.pushButton_2.setStyleSheet("background-color: rgba(85, 70, 70, 85); color: rgb(226, 227, 245);")
        self.error.setText("")

        self.popup = Popup(self.catch_popup)
        self.popup.label.setText("Название теста")

        self.finish_msg = "Закончить создание теста?"
        self.file_name = ""

        self.img = QtGui.QImage(os.path.join(os.path.abspath(os.curdir), "setupData", "img.jpeg"))
        self.palette = QtGui.QPalette()
        self.palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(self.img))
        self.setPalette(self.palette)

        self.VAS.setText("")

        self.step = 0
        self.pitch_size = 2
        self.time = None

        self.dataForm = DataForm()
        self.update(self.step)
        
    def next_step(self):
        if self.step < self.dataForm.get_last_step():
            self.step += 1
            data = self.dataForm.get_data(self.step)
            if self.step == self.pitch_size-1: self.step += 1 
            self.fields_update(data=data)
            self.update(self.step)
            
        elif self.ans_add:
            if self.pushButton.text() == "завершить":
                reply = QtWidgets.QMessageBox.question(self, 'Message', self.finish_msg, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
                if reply == QtWidgets.QMessageBox.Yes:
                    #self.popup.show()
                    self.data_output()
            else:       
                name = self.name_edit.text()
                ans_one = self.q_one.text()
                ans_two = self.q_two.text()
                ans_three = self.q_three.text()
                ans_four = self.q_four.text()
                q_text = self.quest_text.toPlainText()
                
                if name == "": self.error.setText("Введите название теста")
                elif ans_one == "": self.error.setText("Введите первый вариант ответа")
                elif ans_two == "": self.error.setText("Введите второй вариант ответа")
                elif ans_three == "": self.error.setText("Введите третий вариант ответа")
                elif ans_four == "": self.error.setText("Введите четвертый вариант ответа")
                elif q_text == "": self.error.setText("Содержание вопроса не должно быть пустым")
                else:   
                    self.step += 1
                    
                    self.dataForm.last_step_update()
                    self.dataForm.set_name(name)
                    self.dataForm.set_var_ans([ans_one, ans_two, ans_three, ans_four], self.step)
                    self.dataForm.set_quest_text(q_text, self.step)
                    #self.dataForm.data_output(self.step)

                    self.fields_update()
                    self.update(self.step)
        else:
            self.error.setText("Выберите правильный ответ")

    def catch_popup(self, name):
        self.popup.hide()
        self.file_name = name
        self.data_output()

    def fields_update(self, data=None):
        if data is None:
            if self.step != self.pitch_size:
                self.error.setText("")
        
                self.q_one.setText("")
                self.q_two.setText("")
                self.q_three.setText("")
                self.q_four.setText("")
                self.quest_text.setText("")
                self.btn_group.setExclusive(False) # переводим группу из екслюзивного ржима, в нем возможен множественный выбор/не выбрать ни одной
                for radio in self.btn_group.buttons():
                    radio.setChecked(False)  # снимаем отметки
                self.btn_group.setExclusive(True)
            
            
        else:
            self.error.setText("")
            self.q_one.setText(data["q_1"])
            self.q_two.setText(data["q_2"])
            self.q_three.setText(data["q_3"])
            self.q_four.setText(data["q_4"])
            self.quest_text.setText(data["text"])
            if   data["ans"] == 0: self.first_ans.setChecked(True)
            elif data["ans"] == 1: self.second_ans.setChecked(True)
            elif data["ans"] == 2: self.third_ans.setChecked(True)
            elif data["ans"] == 3: self.fourth_ans.setChecked(True)

    def update(self, step):
        text = self.quest_numb.text()[:8]
        self.pushButton_2.setEnabled(True)
        
        if self.step == self.pitch_size:
            self.pushButton.setText("завершить")
            text += str(step)

        elif self.step < self.pitch_size:
            self.pushButton.setText("добавить")
            if self.step == 0:
                self.pushButton_2.setEnabled(False)
            text += str(step + 1)

        self.quest_numb.setText(text)

    def prev_step(self):
        if self.step == self.pitch_size: self.step -= 1
        if self.step > 0:
            self.step -= 1
            data = self.dataForm.get_data(self.step)
            self.fields_update(data=data)
            self.update(self.step)
            

    def onSelect(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.dataForm.set_correct_ans(radioBtn.name, self.step)
            self.ans_add = True

    def pull_in_data(self, fileName):
        #print("open input stream...")
        self.finish_msg = "Закончить редактирование теста?" #"Закончить создание теста?"
        name = fileName.split("/")[-1]
        self.file_name = name[:-4]
        self.popup.lineEdit.setText(self.file_name)
        

        with open(fileName, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
            ex = rows[0]
            self.time = ex["time"]
            self.pitch_size = len(rows)
            for step, row in enumerate(rows):
                self.dataForm.set_name(row["name"])
                self.dataForm.set_var_ans([row["q_1"], row["q_2"], row["q_3"], row["q_4"]], step)
                self.dataForm.set_correct_ans(int(row["ans"]), step)
                self.dataForm.set_quest_text(row["text"], step)
                self.dataForm.last_step_update()
                
        self.dataForm.decryptChoice()
        self.step = 1
        self.name_edit.setText(self.dataForm.get_name())
        self.prev_step()
                  
                

    def data_output(self):
        #print("open output stream...")
        
        with open(os.path.join(PATH, "testData", "source.csv"), 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name", "text", "q_1", "q_2", "q_3", "q_4", "ans", "time"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            self.dataForm.encryptChoice()
            writer.writeheader()
            for step in range(self.pitch_size):
                data = self.dataForm.get_data(step, full=True)
                writer.writerow({"name": data["name"],
                                 "text": data["text"],
                                 "q_1" : data["q_1"],
                                 "q_2" : data["q_2"],
                                 "q_3" : data["q_3"],
                                 "q_4" : data["q_4"],
                                 "ans" : data["ans"],
                                 "time": self.time})
                
        self.finishFunc()
        
            
            

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Message', "Прервать создание теста?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.popup.hide()
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.next_step()
        

class DataForm():
    def __init__(self):
        self.test_name   = ""
        self.quest       = []
        self.correct_one = []
        self.q_text      = []
        self.last_step = 0

    def set_name(self, name):
        self.test_name = name

    def get_name(self):
        return self.test_name

    def get_last_step(self):
        return self.last_step

    def last_step_update(self):
        self.last_step += 1

    def encryptChoice(self):
        '''
        кодируем ответы используя интовую апроксимцию степенной функции y = sqrt(x + 121) - 11
        где:
            y = 0: x[0, 22]
            y = 1: x[23, 47]
            y = 2: x[48, 74]
            y = 3: x[75, 104]
        '''
        print(self.correct_one)
        for i, el in enumerate(self.correct_one):
            if el == 0:
                self.correct_one[i] = random.randint(0, 22)
            elif el == 1:
                self.correct_one[i] = random.randint(23, 47)
            elif el == 2:
                self.correct_one[i] = random.randint(48, 74)
            elif el == 3:
                self.correct_one[i] = random.randint(75, 104)
        print(self.correct_one)

    def decryptChoice(self):
        print(self.correct_one)
        for i, el in enumerate(self.correct_one):
            self.correct_one[i] = int(math.sqrt(el + 121) - 11)
        print(self.correct_one)
        
        
    def set_var_ans(self, ans, step):
        if len(self.quest)-1 < step: 
            self.quest.append(ans)
        else:
            self.quest[step] = ans

    def set_correct_ans(self, ans, step):
        if len(self.correct_one)-1 < step:
            self.correct_one.append(ans)
        else:
            self.correct_one[step] = ans

    def get_correct_ans(self, step):
        return self.correct_one[step]

    def set_quest_text(self, text, step):
        if len(self.q_text)-1 < step:
            self.q_text.append(text)
        else:
            self.q_text[step] = text

    def get_data(self, step, full=False):
        data = {}
        data.update({"text" : self.q_text[step]})
        data.update({"q_1" : self.quest[step][0]})
        data.update({"q_2" : self.quest[step][1]})
        data.update({"q_3" : self.quest[step][2]})
        data.update({"q_4" : self.quest[step][3]})
        data.update({"ans" : self.correct_one[step]})
        if full: data.update({"name" : self.get_name()})
        
        return data

    

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
