from PyQt5 import QtGui, QtCore, uic
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow,QMessageBox,QAction,qApp


class HistoryDialog(QDialog):
    def __init__(self,main_w, parent=None):
        super(HistoryDialog, self).__init__(main_w)
        uic.loadUi('History.ui' , self)
        self.setWindowTitle('History')

        self.history_list = main_w.history['history']
        print(type(self.history_list))
        self.setText()


    def setText(self):
        #self.lst_Widget_History.addItem('first\n\nsecond')
        for i in self.history_list:
            sub_str = 'time : ' + i['time'] + '\n'+ 'term : '+ i['data'] + '\n' +'result : ' + str(i['res']) + '\n\n'
            self.lst_Widget_History.addItem(sub_str)


