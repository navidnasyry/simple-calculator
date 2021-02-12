
from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_FirstWindow(QMainWindow):
   def __init__(self):
       super(Ui_FirstWindow,self).__init__()
       fWindow = uic.loadUi('FirstWindow.ui' , self)
       self.btn_1.setText("dd")








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
