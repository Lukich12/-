import sys, csv, json, time, socket, threading, shutil
from pathlib import Path
from datetime import datetime, date
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QPixmap,QPalette,QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton,
    QSpinBox, QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout, QTabWidget,
    QMessageBox, QGroupBox, QComboBox, QTextEdit, QSlider, QFileDialog
)

with open ('login_password.json','r',encoding='utf8') as file: 
    pass 
with open ('regict','w',encoding='utf8' ) as file2 : 
    pass 
class globall(QMainWindow): 
    def __init__(self):
        super().__init__() 
        self.setWindowTitle('Приложение')    
        central_widget = QWidget(self)
    
        layout = QVBoxLayout()
        hbox = QHBoxLayout()
        
        btn = QPushButton('Регистрация', self)
        btn2 = QPushButton('Авторизация', self) 

        self.mail = QLineEdit(self)
        a = QLabel('Логин')
        b = QLabel('Пароль')
        self.password = QLineEdit(self)
        self.password.EchoMode(QLineEdit.Password)   

        layout.addWidget(a)
        layout.addWidget(self.mail)
        layout.addWidget(b)
        layout.addWidget(self.password)

        hbox.addWidget(btn)
        hbox.addWidget(btn2)

        layout.addLayout(hbox)
        central_widget.setLayout(layout)
        layout.setSpacing(15)
        layout.setContentsMargins(30,30,30,30)
        self.setCentralWidget(central_widget)
        btn.clicked.connect(clik_login)
        btn.clicked.connect(clik_regicntr)
        def clik_login(self): 
            print('Работает')
        def clik_regicntr(self): 
            print('Работает')
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = globall()
    window.resize(1200, 750)
    window.show()
    sys.exit(app.exec_())
