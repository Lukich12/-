import json
import os  
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
        self.setWindowTitle('Приложение')     
        central_widget = QWidget(self)
    
        layout = QVBoxLayout()
        hbox = QHBoxLayout()

        btn = QPushButton('Регистрация', self)
        btn2 = QPushButton('Авторизация', self) 

        self.mail = QLineEdit(self)
        a = QLabel('Логин')
        b = QLabel('пароль')
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)   

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
        btn.clicked.connect(self.clik_register)   
        btn2.clicked.connect(self.clik_aftoregister)
        self.login_window = self.clik_register 
    def clik_register(self):
        self.register_window = Regust(self)
        self.hide()
        self.register_window.resize(1250,750)
        self.register_window.show()
    def clik_aftoregister(self):
        Textlogin = self.mail.text()
        Textpassword = self.password.text()
        users = file1() 
        if Textlogin in users :
            if users[Textlogin] == Textpassword  : 
                print('Вход успешный !')
                self.hide() 
                self.afroregister.resize(1250,750)
                self.afroregister.show()
            else : 
                print('Пароль не правельный')
        else :
            print('Такой логин или паролья нету !')
class Regust(QMainWindow): 
    def __init__(self,clik_register):
        super().__init__()
        self.login_window = clik_register
        centr_widet = QWidget()
        Qbox = QVBoxLayout()
        Xbox = QHBoxLayout()

        login_name = QLabel('логин')
        password_name = QLabel('пароль')
        password2_name = QLabel('Подвердите пароль')

        self.login = QLineEdit(self)

        self.password = QLineEdit()

        self.password.setEchoMode(QLineEdit.Password)
        self.password2 = QLineEdit(self)    
        self.password2.setEchoMode(QLineEdit.Password)

        btn = QPushButton('Регистрация')
        btn2 = QPushButton('Выход')
        btn3 = QPushButton('Назад')

        Qbox.addWidget(login_name)
        Qbox.addWidget(self.login)

        Qbox.addWidget(password_name)
        Qbox.addWidget(self.password)
        Qbox.addWidget(password2_name)
        Qbox.addWidget(self.password2)

        Xbox.addWidget(btn)
        Xbox.addWidget(btn2)
        Xbox.addWidget(btn3)

        Qbox.addLayout(Xbox)
        centr_widet.setLayout(Qbox)
        self.setCentralWidget(centr_widet)

        btn.clicked.connect(self.registerr)
        btn2.clicked.connect(self.exitt)
        btn3.clicked.connect(self.nazat)
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
    def nazat(self):
        self.login_window.show()
        self.hide()
    def exitt(self): 
        self.hide()
class pylcometr(QMainWindow) :
    def __init__(self):
        super().__init__()
        centralwidget = QWidget ()
        xbox = QHBoxLayout()
        Vbox =  QVBoxLayout()
        btn_exit = QPushButton('Выход')

        puls = QLabel('---') 
        Vbox.addWidget(btn_exit)

        btn_exit.clicked.connect(self.exitt)
        xbox.addWidget(puls)
        Vbox.addLayout(xbox)
        centralwidget.setLayout(Vbox)
        self.setCentralWidget(centralwidget)
    def exitt(self): 
        self.close() 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = globall()  
    window.resize(1200, 750)
    window.show()
    sys.exit(app.exec_())
