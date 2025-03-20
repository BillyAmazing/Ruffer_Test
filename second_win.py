# write a code for the second screen of app
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton,
    QPushButton,QLabel, QListWidget,QLineEdit)

from instr import *
from second_win import *

class TestWin(QWidget):
    def __init__(self):
        '''the window in which the survey is being conducted'''
        super().__init__()

    