
from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_FirstWindow(QMainWindow):
    def __init__(self):
        super(Ui_FirstWindow,self).__init__()
        uic.loadUi('FirstWindow.ui' , self)
        self.result = 0
        self.result_str_all = ""
        self.last_operator = "+"
        self.startCall()



    def startCall(self):
        self.btn_1.clicked.connect(lambda: self.enterNum(1))
        self.btn_0.clicked.connect(lambda: self.enterNum(0))
        self.btn_2.clicked.connect(lambda: self.enterNum(2))
        self.btn_3.clicked.connect(lambda: self.enterNum(3))
        self.btn_4.clicked.connect(lambda: self.enterNum(4))
        self.btn_5.clicked.connect(lambda: self.enterNum(5))
        self.btn_6.clicked.connect(lambda: self.enterNum(6))
        self.btn_7.clicked.connect(lambda: self.enterNum(7))
        self.btn_8.clicked.connect(lambda: self.enterNum(8))
        self.btn_9.clicked.connect(lambda: self.enterNum(9))
        self.btn_plus.clicked.connect(lambda: self.enterOperator('+'))
        self.btn_mines.clicked.connect(lambda: self.enterOperator('-'))
        self.btn_drive.clicked.connect(lambda: self.enterOperator('/'))
        self.btn_mul.clicked.connect(lambda: self.enterOperator('*'))
        self.btn_del.clicked.connect(lambda: self.enterDel())
        self.btn_clear.clicked.connect(lambda: self.enterClear())
        self.btn_equal.clicked.connect(self.calResult)


    def enterDel(self):
        if self.led_show.text() == '':
            return
        self.led_show.backspace()
        self.led_show_all.backspace()
        self.result_str_all = self.result_str_all[:-1]

    def enterClear(self):
        self.result = 0
        self.result_str_all = ""
        self.last_operator = "+"
        self.led_show.clear()
        self.led_show_all.clear()
        self.dsb_result.setValue(0)


    def calResult(self):
        if self.led_show.text() == '':
            return

        input_float = float(self.led_show.text())
        if self.last_operator == '+':
            self.result += input_float
        elif self.last_operator == '-':
            self.result -= input_float
        elif self.last_operator == '/':
            self.result /= input_float
        elif self.last_operator == '*':
            self.result *= input_float
        else:
            pass

        self.dsb_result.setValue(self.result)
        self.led_show.clear()


    def enterNum(self , num):
        if self.result_str_all[-1:].isnumeric() and  self.led_show.text() == '':
               self.result_str_all += ' ' + self.last_operator + ' '
        self.result_str_all += str(num)
        self.led_show_all.setText(self.result_str_all)
        self.led_show.setText(self.led_show.text() + str(num))


    def enterOperator(self , op_str):
        if self.result_str_all[-2:-1] == '/' or self.result_str_all[-2:-1] == '*' or self.result_str_all[-2:-1] == '+' or self.result_str_all[-2:-1] == '-':
            self.result_str_all = self.result_str_all[:-3]

        if op_str == '+':
            if self.led_show.text() != '':
                self.calResult()

            self.last_operator = '+'
            self.result_str_all += ' ' + op_str + ' '
            self.led_show_all.setText(self.result_str_all)

        elif op_str == '-':
            if self.led_show.text() != '':
                self.calResult()

            self.last_operator = '-'
            self.result_str_all += ' ' + op_str + ' '
            self.led_show_all.setText(self.result_str_all)
        elif op_str == '/':
            if self.led_show.text() != '':
                self.calResult()

            self.last_operator = '/'
            self.result_str_all += ' ' + op_str + ' '
            self.led_show_all.setText(self.result_str_all)

        elif op_str == '*':
            if self.led_show.text() != '':
                self.calResult()

            self.last_operator= '*'
            self.result_str_all += ' ' + op_str + ' '
            self.led_show_all.setText(self.result_str_all)




''' def initUI(self):
       self.first_lbl = QtWidgets.QLabel(self)
       self.first_lbl.setText("Starting...")
       self.first_lbl.move(100,100)


       self.first_btn = QtWidgets.QPushButton(self)
       self.first_btn.setText("click me")
       self.first_btn.move(10 , 20)
       self.first_btn.clicked.connect(self.clicked)

    def clicked(self):
       self.first_lbl.setText("clicked")
'''
