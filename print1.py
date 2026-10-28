import json
import serial
#import face_recognition
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
class regicter(QMainWindow):
    def __init__(self):
        super().__init__()   
        self.central_widget = QWidget(self)
        self.regict()
    def regict(self): 
        self.Hbox = QHBoxLayout()
        self.Vbox = QVBoxLayout()
        self.Hbox.addLayout(self.Vbox)

        self.regicter_blok = QLabel('Регистрация оператора')
        self.id_blok = QLabel('Идентифцикаия')
        self.info_blok = QLabel('Информационный блок')

        # Regist_blok  
        self.name_1 = QLabel('Фамилия')
        self.name_2 = QLabel('Имя')
        self.name_3 = QLabel('oтчество')
        self.age = QLabel('Возраст')

        self.full_name = QLabel()

        self.name1 = QLineEdit()
        self.name1Text = self.name1.QLineEdit()
        self.name2 = QLineEdit()
        self.name3 = QLineEdit()
        self.age_ = QLineEdit()

        self.btn_regiser = QPushButton('Записать')

        #id_blok
        self.kakera = QLabel()
        #info_blok
        self.oper = QLabel()
        self.id_name = QLineEdit()
        self.info = QLabel('Для запуска программы нажмите далее')
        self.btn_info = QPushButton('Далее')

        self.btn_regiser.clicked.connect(self.clik_btn_register)
        self.btn_info.clicked.connect(self.clik_btn_info)

        self.Boxlayout()
    def Boxlayout(self):
        self.Hbox.addWidget(self.name_1)
        self.Hbox.addWidget(self.name_2)
        self.Hbox.addWidget(self.name_3)
        self.Hbox.addWidget(self.age)

        self.Hbox.addWidget(self.name1)
        self.Hbox.addWidget(self.name2)
        self.Hbox.addWidget(self.name3)
        self.Hbox.addWidget(self.age_)

        self.Vbox.addWidget(self.btn_regiser)

        self.Hbox.addWidget(self.kakera)

        self.Hbox.addWidget(self.oper)
        self.Hbox.addWidget(self.id_name)

        self.Hbox.addWidget(self.info)
        self.Vbox.addWidget(self.btn_info)

        self.color_regitr()
    def color_regitr(self): 
        pass 
    def clik_btn_register(self):
        btn_text = self.btn_regiser.text() 
        with open('Login_password', 'r', encoding='utf-8') as file_registr : 
            data = json.load(file_registr)
            if data in btn_text : 
                pass  
    def clik_btn_info(self):
        btn_info = self.btn_info.text()
        with open('Login_password.json', 'r', encoding='utf-8') as file_info : 
            data = json.load(file_info) 
            if data in btn_info : 
                self.hide()
                pylcometr.show()  
class avtoregust(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.regicter()
    def regicter(self): 
        self.Xbox = QHBoxLayout()
        self.Vbox = QVBoxLayout()
        self.Xbox.addLayout(self.Vbox)

        self.id_oper = QLabel('Авторезация оператора')
        self.id_name = QLabel('Введите ID')

        self.id_Edit = QLineEdit()

        self.btn_id = QPushButton('Авторезация')
        self.layout_id()
    def layout_id(self):
        self.setCentralWidget(self.centralwidget)
        
        self.Xbox.addWidget(self.id_oper)
        self.Vbox.addWidget(self.id_name)

        self.Xbox.addStretch(1)
        self.Xbox.addWidget(self.id_Edit)
        self.Xbox.addStretch(1)

        self.Xbox.addStretch(1)
        self.Vbox.addWidget(self.btn_id)

        self.btn_id.clicked.connect(self.clik_btn_id)
        self.color_id()
    def color_id(self): 
        self.id_oper.setStyleSheet('color: #FFFFFF')
        self.id_name.setStyleSheet('color: #FFFFFF')
    
        self.id_Edit.setStyleSheet('background-color: #000000 ; color: #FFFFFF')
        self.btn_id.setStyleSheet('background-color : #000000 ; color: #FFFFFF')
    def clik_btn_id(self): 
        text_id = self.id_Edit.text()
        with open ('login_password.json','r',encoding='utf-8') as file1 :    
            data = json.load(file1)
            if text_id in data: 
                self.hide()
                pylcometr.show()
class pylcometr(QMainWindow) :
    def __init__(self):
        super().__init__()
    def create_widgets(self):
        self.centralwidget = QWidget()

        self.xbox = QHBoxLayout()
        self.Vbox =  QVBoxLayout()

        self.meny = QLabel('Меню управление')

        self.btn_info = QPushButton('Инструкция')
        self.btn_analiz = QPushButton('Анализ')
        self.btn_ynp = QPushButton('Управление')

        self.analiz = QLabel('Анализ оператора')

        self.pylsMax_name = QLabel('Укажите порог вашего пульса')
        self.pylsMin_name = QLabel('Укажите норму вашего пульса')

        self.pylsMax = QLineEdit()
        self.pylsMin = QLineEdit()

        self.btn_zapicn = QPushButton('Записать')

        self.tepmenal = QLabel('Терминал блока информации')

        self.info_user = QLabel('Индефекация')

        self.user_ = QLabel('Оператор определен :')
        self.user = QLabel('')
        self.btn_pylcDalue = QPushButton('Далее')
    def layoutBox(self):
        pass 
    def color_pycometr(self) : 
        pass 
    def builging_button(self): 
        self.btn_pylcDalue.clicked.connect(self.Button_Dalue)
        self.btn_zapicn.clicked.connect(self.button_zapich)
    def button_zapich(self): 
        pass
    def Button_Dalue(self):
            self.hide()
            self.info_user.show()               
    def port_pylc(self):
            self.port = serial.Serial('COM10', 115200, timeout=0)
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.read_pulse)
            self.timer.start(100)
    def read_pulse(self): 
        if self.port.in_waiting:
            line = self.port.readline().decode('utf-8', errors='ignore').strip()
            if 'BPM:' in line:
                bpm = line.split('BPM:')[1].strip()
                self.puls.setText(f'{bpm} BPM')  
class lnfo_user(QMainWindow):
    def __init__(self):
        super().__init__() 
    def info(self): 
        self.info_oper = QLabel('Информация оператора')
        self.kamera_user = QLabel()

        self.time = QLabel(time)
        self.time_po = QLabel('Время запуска ПО')
        self.time_goroga = QLabel('Время в дороге')
        self.timeMax = QLabel('Оставшееся время')
        self.cocto = QLabel('Состояние:')

        self.tepminal_blok = QLabel('Терминальный блок')

        self.blok_undefeka = QLabel('Блок индефекации')

        self.pyls = QLabel('---')

        self.stop = QPushButton('Стоп программа')

        self.stop.clicked.connect(self.stop_programa)
    def stop_programa(self): 
           self.hide()
           exit() 
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = regicter()  
    window.resize(800,550)
    window.show()
    sys.exit(app.exec_())
