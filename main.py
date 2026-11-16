import os 
import csv
import sys,time,socket,threading,shutil
from datetime import datetime, date
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QPixmap,QPalette,QColor,QImage
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton,
    QSpinBox, QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout, QTabWidget,
    QMessageBox, QGroupBox, QComboBox, QTextEdit, QSlider, QFileDialog,QDialog
)

class Start(QMainWindow):
    def __init__(self):
        super(). __init__()
        self.central = QWidget()
        self.Block1Object()
        self.resize(700, 400)
    def Block1Object(self):
        self.name_program = QLabel("Нейробобр")
        self.btn_registration = QPushButton("Регистрация")
        self.btn_autorisation = QPushButton("Авторизация")
        #self.btn_registration.clicked.connect(self.ClickRegistration)
        #self.btn_autorisation.clicked.connect(self.ClickedAutorisation)
        self.layoutBlock1()
    def layoutBlock1(self):
        self.setCentralWidget(self.central)
        self.HBox = QHBoxLayout()
        self.GridBox = QGridLayout()
        self.HBox.addLayout(self.GridBox)
        self.central.setLayout(self.HBox)

        self.GridBox.addWidget(self.name_program, 1, 1, 2, 2, alignment=Qt.AlignCenter)
        self.Big_text = QFont('Arial',10, QFont.Bold)
        self.name_program.setFont(self.Big_text)
        self.GridBox.addWidget(self.btn_autorisation, 2, 1)
        self.GridBox.addWidget(self.btn_registration, 2, 2)
    def colorStart(self)
        self.btn_registration.setStyleSheet()
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Start()
    window.show()
    sys.exit(app.exec_())