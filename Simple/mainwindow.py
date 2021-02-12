# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from FirstWindow import *



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = Ui_FirstWindow()
    win.show()
    sys.exit(app.exec_())
