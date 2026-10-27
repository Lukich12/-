import json
import serial
import face_recognition
import os  
import sys, csv, json, time, socket, threading, shutil
from pathlib import Path
from datetime import datetime, date
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QPixmap,QPalette,QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton,
    QSpinBox, QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout, QTabWidget,
    QMessageBox, QGroupBox, QComboBox, QTextEdit, QSlider, QFileDialog,QDialog
)
def file1():  
    if os.path.exists('login_password.json'): 
        with open ('login_password.json', 'r', encoding='utf-8') as f : 
            data = json.load(f)
            return data  
    else : 
        return {} 
def file2(users):
    with open('login_password.json','w',encoding='utf-8') as b :
        json.dump(users, b, ensure_ascii=False, indent=4)
class globall(QMainWindow):
    def __init__(self):
        super().__init__()   
        self.central_widget = QWidget(self)
        self.create_widgets()
        self.setup_layout()
        self.metruka_global()
    def create_widgets(self): 
        self.layout = QVBoxLayout()
        self.hbox = QHBoxLayout()

        self.btn = QPushButton('Регистрация', self)
        self.btn2 = QPushButton('Авторизация', self) 
        self.btn3 = QPushButton('Вход по лицу', self)
        self.hbox.setSpacing(10)

        self.mail = QLineEdit(self)
        self.a = QLabel('Логин')
        self.b = QLabel('пароль')
        self.password = QLineEdit(self)

        self.central_widget.setObjectName("mainBackground")
    def setup_layout(self):  
        self.password.setEchoMode(QLineEdit.Password)   
        
        self.layout.addStretch(1)
        self.layout.addWidget(self.a)
        self.layout.addWidget(self.mail)
        self.layout.addWidget(self.b)
        self.layout.addWidget(self.password)

        self.hbox.addStretch(1)
        self.hbox.addWidget(self.btn)
        self.hbox.addWidget(self.btn2)
        self.hbox.addStretch(1)

        self.layout.addLayout(self.hbox)
        self.central_widget.setLayout(self.layout)
        self.layout.setSpacing(15)
        self.layout.setContentsMargins(30,30,30,30)
        self.setCentralWidget(self.central_widget)
        self.layout.addStretch(1)

        self.btn.clicked.connect(self.clik_register)   
        self.btn2.clicked.connect(self.clik_aftoregister)
        self.login_window = self.clik_register

        self.layout.addWidget(self.btn3)
        self.btn3.clicked.connect(self.clik_face)
        self.color_globall()
    def color_globall(self):
        self.central_widget.setStyleSheet('QWidget#mainBackground { background-color: #111827; }')

        self.btn.setStyleSheet('background-color: #374151; color: #FFFFFF; border-radius: 10px;')
        self.btn2.setStyleSheet('background-color: #374151; color: #FFFFFF; border-radius: 10px;')

        self.a.setStyleSheet('color: #E5E7EB;')
        self.b.setStyleSheet('color: #E5E7EB;')

        self.btn.setFixedSize(145,40)
        self.btn2.setFixedSize(145,40)
        self.mail.setFixedSize(300,40)
        self.password.setFixedSize(300,40)
    def metruka_global(self): 
        self.layout.setAlignment(self.mail,Qt.AlignHCenter)
        self.layout.setAlignment(self.password,Qt.AlignHCenter)
        self.layout.setAlignment(self.a,Qt.AlignHCenter)
        self.layout.setAlignment(self.b,Qt.AlignHCenter)
    def clik_face(self):
        dialog = FaceLogin()
        dialog.exec_()
    def clik_register(self):
        self.register_window = Regust(self)
        self.hide()
        self.register_window.resize(800,550)
        self.register_window.show()
        self.afroregister = pylcometr()
    def clik_aftoregister(self):
        Textlogin = self.mail.text()
        Textpassword = self.password.text()
        users = file1() 
        if Textlogin in users :
            if users[Textlogin] == Textpassword  : 
                print('Вход успешный !')
                self.afroregister = pylcometr()
                self.hide()
                self.afroregister.resize(800, 550)
                self.afroregister.show()
            else : 
                print('Пароль не правельный')
        else :
            print('Такой логин или паролья нету !')
class FaceLogin(QDialog): 
    def __init__(self) : 
        super().__init__()
        centr_widet = QWidget()

        Kamera_face()
        self.Kamera1()
        self.calor_Facelogin()
        self.metruka_face()

    def Kamera_face(self): 
        self.zagalovok = Qlabel('Биометрическая авторезация')
        self.Kamera = QLabel('Ожидание камеры') 
        self.resize(500,400)  

    def calor_Facelogin(self):
        self.zagalovok.QFileDialog('calor : ')
        self.Kamera.QFiledialog('calor')

    def metruka_face(self):
        self.Xbox = QHBoxLayout()
        self.Vbox = QVBoxLayout()

        xbox.addWidget(self.zagalovok)
        Xbox.addWidget(self.Kamera)
    def vozrat_okna(self):
        self.globall.show()
        self.hide()
class Regust(QMainWindow): 
    def __init__(self,clik_register):
        super().__init__()
        self.login_window = clik_register
        self.centr_widet = QWidget()
        self.create_widgets()
        self.setup_layout()
        self.centr_widet.setObjectName("mainBackground")
        self.calor_rugust()
    def create_widgets(self):
        self.Qbox = QVBoxLayout()
        self.Xbox = QHBoxLayout()

        self.login_name = QLabel('логин')
        self.password_name = QLabel('пароль')
        self.password2_name = QLabel('Подвердите пароль')

        self.login = QLineEdit(self)

        self.password = QLineEdit(self)

        self.password.setEchoMode(QLineEdit.Password)
        self.password2 = QLineEdit(self)    
        self.password2.setEchoMode(QLineEdit.Password)

        self.btn = QPushButton('Регистрация')
        self.btn2 = QPushButton('Выход')
        self.btn3 = QPushButton('Назад')
    def setup_layout(self): 

        self.login.setFixedSize(300, 40)
        self.password.setFixedSize(300, 40)
        self.password2.setFixedSize(300, 40)
                
        self.btn.setFixedSize(120, 40)
        self.btn2.setFixedSize(120, 40)
        self.btn3.setFixedSize(120, 40)
        
        self.Qbox.addStretch(1)
        self.Qbox.addWidget(self.login_name)
        self.Qbox.addWidget(self.login)

        self.Qbox.addWidget(self.password_name)
        self.Qbox.addWidget(self.password)
        self.Qbox.addWidget(self.password2_name)
        self.Qbox.addWidget(self.password2)

        self.Xbox.addStretch(1)
        self.Xbox.addWidget(self.btn)
        self.Xbox.addWidget(self.btn2)
        self.Xbox.addWidget(self.btn3)
        self.Xbox.addStretch(1)
        self.Xbox.setSpacing(10)

        self.Qbox.addLayout(self.Xbox)
        self.Qbox.addStretch(1)
        self.Qbox.setSpacing(10)
        self.Qbox.setContentsMargins(30, 30, 30, 30)
        self.centr_widet.setLayout(self.Qbox)
        self.setCentralWidget(self.centr_widet)

        self.btn.clicked.connect(self.registerr)
        self.btn2.clicked.connect(self.exitt)
        self.btn3.clicked.connect(self.nazat)

        self.Qbox.setAlignment(self.login, Qt.AlignHCenter)
        self.Qbox.setAlignment(self.password, Qt.AlignHCenter)
        self.Qbox.setAlignment(self.password2, Qt.AlignHCenter)

        self.Qbox.setAlignment(self.password_name, Qt.AlignHCenter)
        self.Qbox.setAlignment(self.password2_name, Qt.AlignHCenter)
        self.Qbox.setAlignment(self.login_name, Qt.AlignHCenter)
    def calor_rugust(self): 
        self.centr_widet.setStyleSheet('QWidget#mainBackground {  background-color: #111827; }')

        self.btn.setStyleSheet('background-color: #374151; color: #FFFFFF; border-radius: 10px; ')
        self.btn2.setStyleSheet('background-color: #374151; color: #FFFFFF; border-radius: 10px;')
        self.btn3.setStyleSheet('background-color: #374151; color: #FFFFFF; border-radius: 10px;')

        self.login_name.setStyleSheet('color: #E5E7EB;')
        self.password_name.setStyleSheet('color: #E5E7EB ')
        self.password2_name.setStyleSheet('color: #E5E7EB')

        self.login.setStyleSheet("background-color: white; color: black; border-radius: 6px;")
        self.password.setStyleSheet("background-color: white; color: black; border-radius: 6px;")
        self.password2.setStyleSheet("background-color: white; color: black; border-radius: 6px;")
    def proverka(self,text_login,text_password) : 
        if not text_login: 
            print('работает') 
        if not text_password : 
             print('работает')  
    def registerr(self): 
        text_login = self.login.text()
        text_password = self.password.text()  
        text_password2 = self.password2.text() 
        if not text_login : 
            print('Ошибка логина')
            return
        if not text_password : 
            print('Ошибка пароль')
            return 
        if not text_password2 : 
            print('Ошибка пароль 2')
            return   
        if text_password != text_password2 : 
            print('Пароль не совподает')
            return
        
        users = file1()
        if text_login in users:  
            print('Такой логина уже существует ')
            return
        else: 
            users[text_login] = text_password
            file2(users)
            print('Регистрация прошла успешно !')
            self.nazat()
    def nazat(self):
        self.login_window.show()
        self.hide()
    def exitt(self): 
        self.hide()
class pylcometr(QMainWindow) :
    def __init__(self):
        super().__init__()
        self.centralwidget = QWidget()
        self.create_widgets()
        self.color_pulse()

        self.port = serial.Serial('COM10', 115200, timeout=0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.read_pulse)
        self.timer.start(100)
    def create_widgets(self):
        self.xbox = QHBoxLayout()
        self.Vbox =  QVBoxLayout()
        self.btn_exit = QPushButton('Выход')

        self.tek_pulse = QLabel('Текущий пулс') 
        self.puls = QLabel('---') 
        self.pulse_name = QLabel('ВРМ')

        self.Vbox.addWidget(self.btn_exit)

        self.btn_exit.clicked.connect(self.exitt)

        self.xbox.addWidget(self.tek_pulse)
        self.xbox.addWidget(self.puls)
        self.Vbox.addLayout(self.xbox)

        self.centralwidget.setLayout(self.Vbox)
        self.setCentralWidget(self.centralwidget)
    def color_pulse(self):
        self.centralwidget.setObjectName("pulseBackground")
        self.centralwidget.setStyleSheet(
        "QWidget#pulseBackground { background-color: #111827; }"
        )

        self.puls.setStyleSheet("color: #F87171;")
        self.puls.setAlignment(Qt.AlignCenter)

        self.tek_pulse.setStyleSheet('Color: #F87171 ')
    def read_pulse(self): 
        if self.port.in_waiting:
            line = self.port.readline().decode('utf-8', errors='ignore').strip()
            if 'BPM:' in line:
                bpm = line.split('BPM:')[1].strip()
                self.puls.setText(f'{bpm} BPM')  
    def exitt(self): 
        self.close() 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = globall()  
    window.resize(800,550)
    window.show()
    sys.exit(app.exec_())
