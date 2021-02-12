
from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_FirstWindow(QMainWindow):
    def __init__(self):
        super(Ui_FirstWindow,self).__init__()
        uic.loadUi('FirstWindow.ui' , self)
        self.result=0
        self.result_str_all=""

        self.btn_1.clicked.connect(lambda :self.enterNum(1))
        self.btn_0.clicked.connect(lambda :self.enterNum(0))
        self.btn_2.clicked.connect(lambda :self.enterNum(2))
        self.btn_3.clicked.connect(lambda :self.enterNum(3))
        self.btn_4.clicked.connect(lambda :self.enterNum(4))
        self.btn_5.clicked.connect(lambda :self.enterNum(5))
        self.btn_6.clicked.connect(lambda :self.enterNum(6))
        self.btn_7.clicked.connect(lambda :self.enterNum(7))
        self.btn_8.clicked.connect(lambda :self.enterNum(8))
        self.btn_9.clicked.connect(lambda :self.enterNum(9))





    def enterNum(self , num):
        self.result_str_all+=str(num)
        str_now = self.led_show.text()
        self.led_show.setText(str_now + str(num))


    def enterOperantor(self , op_str):
        pass






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
