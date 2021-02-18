from PyQt5 import QtGui, QtCore, uic
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow,QMessageBox,QAction,qApp


class HistoryDialog(QDialog):
    def __init__(self,his_txt, parent=None):
        super(HistoryDialog, self).__init__(his_txt)
        uic.loadUi('History.ui' , self)

        self.history_txt = his_txt

        self.setText()


    def setText(self):
        pass
        #self.txt_browser_history.setText(self.history_txt)

