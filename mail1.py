import sys, csv, json, time, socket, threading, shutil
from pathlib import Path
from datetime import datetime, date
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton,
    QSpinBox, QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout, QTabWidget,
    QMessageBox, QGroupBox, QComboBox, QTextEdit, QSlider, QFileDialog
)
def file(): 
    with open('Login.json' , 'r', encoding='utf8') as a : 
        pass 

    with open('avto.json', 'r', encoding='etf8') as b : 
        pass 

class globall(QMainWindow): 
    def __init__(self):
        super().__init__() 
        
        self.button = QPushButton('Регистрация',self)
        layout = QVBoxLayout()
        self.button.resize(149,100)
        
        self.button2 = QPushButton('Авторегистрация',self)
        self.button2.move(150,0)
        self.button2.resize(150,100)

        def regicner(self) : 
            window = QMainWindow() 
            self.button.click(regicner)
       
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = globall()
    window.resize(1200,750)
    window.show()
    sys.exit(app.exec_())
