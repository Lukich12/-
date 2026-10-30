import json
import serial
import cv2
import random
import csv 
import os 
#import face_recognition 
import csv
import sys, csv, json, time, socket, threading, shutil
from pathlib import Path
from datetime import datetime, date
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QPixmap,QPalette,QColor,QImage
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
        json.dump()
class stapt_okno(QMainWindow) : 
    def __init__(self):
        super().__init__()
        self.resize(800,500)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.regicter_window = regicter()
        self.aftoregistr = avtoregust()
        self.starp_okno()
    def starp_okno(self): 
        self.hbox = QVBoxLayout()
        self.Hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()

        self.hbox.addLayout(self.vbox) 
        self.hbox.addLayout(self.Hbox)
        self.central_widget.setLayout(self.hbox)

        self.text_okno = QLabel('Выберите необходимые действие')

        self.btn_register = QPushButton('Регистрация')
        self.btn_aftoregister = QPushButton('Авторизация')

        self.btn_register.clicked.connect(self.clik_register)
        self.btn_aftoregister.clicked.connect(self.clika_aftoregister)
        self.layout_okno()
    def layout_okno(self):
        self.vbox.addWidget(self.text_okno)
        self.text_okno.setAlignment(Qt.AlignCenter)

        self.Hbox.addStretch(1)
        self.Hbox.addWidget(self.btn_register, alignment=Qt.AlignCenter)
        self.Hbox.addWidget(self.btn_aftoregister,alignment=Qt.AlignCenter)
        self.Hbox.addStretch(1)

        self.btn_register.setFixedSize(200, 60)
        self.btn_aftoregister.setFixedSize(200, 60)

        self.text_okno.setStyleSheet("font-size: 20px;")
        self.color_okno()
    def color_okno(self): 
        self.btn_register.setStyleSheet('background-color : #2D2D2D;')
        self.btn_register.setStyleSheet("""
    QPushButton {
        background-color: #2D2D2D;
        color: white;
    }

    QPushButton:hover {
        background-color: #505050;
    }
    """)
        self.btn_aftoregister.setStyleSheet("""
    QPushButton {
       background-color: #2D2D2D;
       color: white;
   }   
    QPushButton:hover {
       background-color: #505050;
   }
   """)
    def clik_register(self): 
        self.hide()
        self.regicter_window.show()
    def clika_aftoregister(self):
        self.hide()
        self.aftoregistr.show()
class regicter(QMainWindow):
    def __init__(self):
        super().__init__()   
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.resize(1000,550)
        self.regict()
        self.cap = cv2.VideoCapture(0)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_camera)

        if self.cap.isOpened():
            self.timer.start(30)
        else:
            self.kakera.setText('Камера не подключена')
            self.kakera.setStyleSheet(
            'background-color: white; color: black;'
        )
    def regict(self): 
        self.Hbox = QHBoxLayout()
        self.NeobobpVbox = QVBoxLayout() # Шапка 
        self.glavnVbox = QVBoxLayout() # Главный Vbox
        self.Vbox = QVBoxLayout() # Регистрация
        self.Vbox2 = QVBoxLayout() #Инефекация
        self.Vbox3 = QVBoxLayout() # Информация 

        self.glavnVbox.addLayout(self.NeobobpVbox)
        self.glavnVbox.addLayout(self.Hbox)
        self.Hbox.addLayout(self.Vbox)
        self.Hbox.addLayout(self.Vbox2)
        self.Hbox.addLayout(self.Vbox3)
        self.central_widget.setLayout(self.glavnVbox)
        
        self.Neobobp = QLabel('НейроБобр')
        self.programa = QLabel('Программа для мониторинга состояния водителей')

        self.regicter_blok = QLabel('Регистрация оператора')
        self.id_blok = QLabel('Идентифцикаия')
        self.info_blok = QLabel('Информационный блок')

        self.Text_name1 = self.nameEdit1 = QLineEdit()
        self.Text_name1 = self.nameEdit2 = QLineEdit()
        self.Text_name1 = self.nameEdit3 = QLineEdit()
        self.TextAge = self.ageEdit = QLineEdit()


        self.btn_regiser = QPushButton('Записать')

        #id_blok
        self.kakera = QLabel('Камера')
        #info_blok
        self.oper = QLabel()
        self.id_name = QLineEdit()
        self.info = QLabel('Для запуска программы нажмите далее')
        self.btn_info = QPushButton('Далее')

        self.btn_regiser.clicked.connect(self.clik_btn_register)
        self.btn_info.clicked.connect(self.clik_btn_info)
        self.Boxlayout()  
    def fileSCV(self):
        os.makedirs('Operator', exist_ok=True)

        file_path = Path('Operator/operators.csv')

        if not file_path.is_file():
            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['ID', 'Фамилия', 'Имя', 'Отчество', 'Возраст'])
            
    def clik_btn_register(self): 

        self.familiya = self.nameEdit1.text()
        self.name= self.nameEdit2.text()
        self.otchestvo = self.nameEdit3.text()
        self.age = self.ageEdit.text()

        if self.familiya != '' and self.name != '' and self.otchestvo != '' and self.age != '': 
            self.operator_id = random.randint(10000, 99999)
            self.widow_fill = fullPegister(self.operator_id)
            self.ceivfile()
            self.widow_fill.show()
    def ceivfile(self): 
        self.fileSCV()
        file = Path('Operator/operators.csv')
        with open ( file, 'a' ,newline="", encoding='utf-8') as fileseif: 
            writer = csv.writer(fileseif)
            writer.writerow([
                self.operator_id,
                self.familiya,
                self.name,
                self.otchestvo,
                self.age
            ])
        
    def clik_btn_info(self): 
        pass 
    def Boxlayout(self): 
        self.Hbox.setStretch(0, 1)
        self.Hbox.setStretch(1, 1)
        self.Hbox.setStretch(2, 1)
         
        self.Vbox.addWidget(self.regicter_blok)
        self.regicter_blok.setStyleSheet("font-size: 20px;")
        self.programa.setStyleSheet('font-size: 16px;')
        self.Neobobp.setStyleSheet('font-size: 32px;')

        self.from_layout = QFormLayout()
        self.Vbox.addLayout(self.from_layout)

        self.NeobobpVbox.addWidget(self.Neobobp)
        self.NeobobpVbox.addWidget(self.programa)

        self.from_layout.addRow('Фамилия',self.nameEdit1)
        self.from_layout.addRow('Имя', self.nameEdit2)
        self.from_layout.addRow('Отчество', self.nameEdit3)
        self.from_layout.addRow('Возраст', self.ageEdit)
        self.Vbox.addWidget(self.btn_regiser)

        self.Vbox2.addWidget(self.id_blok)
        self.kakera.setAlignment(Qt.AlignCenter)
        self.Vbox2.addWidget(self.kakera)
        self.kakera.setFixedHeight(300)

        self.Vbox3.addWidget(self.info_blok)
        self.Vbox3.addWidget(self.oper)
        self.Vbox3.addWidget(self.id_name)
        self.Vbox3.addWidget(self.info)
        self.Vbox3.addWidget(self.btn_info)

        self.Hbox.setSpacing(20)
        
        self.Neobobp.setAlignment(Qt.AlignCenter)
        self.programa.setAlignment(Qt.AlignCenter)
        self.regicter_blok.setAlignment(Qt.AlignCenter)
        self.id_blok.setAlignment(Qt.AlignCenter)
        self.info_blok.setAlignment(Qt.AlignCenter)
        self.color_register()

        self.btn_regiser.setMinimumSize(120,40)
        self.btn_info.setMinimumSize(120,40)

        self.nameEdit1.setMinimumSize(180,30)
        self.nameEdit2.setMinimumSize(180,30)
        self.nameEdit3.setMinimumSize(180,30)
        self.ageEdit.setMinimumSize(180,30)
    def color_register(self): 
        self.regicter_blok.setStyleSheet(
            "border: 2px solid #808080;"
            "border-radius: 8px;"
        )
        self.id_blok.setStyleSheet(
            'border: 2px solid #808080;'
            'border-radius: 8px;'
        )
        self.info_blok.setStyleSheet(
            'border : 2px solid #808080;'
            'border-radius: 8px;'
        )
        self.setStyleSheet('background-color: #f0f0f0')

        self.btn_info.setStyleSheet(
            'background-color: #0000FF;'
            'color: #FFFFFF;'
            'border: 8px solid #808080;'
            'border-radisus: 8px;'
        )
        self.btn_regiser.setStyleSheet(
            'background-color: #0000FF;'
            'color #FFFFFF;'
            'border : 8px solid #808080;'
            'border-redisus : 8px; ' 
        )
    def update_camera(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            image = QImage(
                frame.data,
                w,
                h,
                bytes_per_line,
                QImage.Format_RGB888
            )
            pixmap = QPixmap.fromImage(image)
            self.kakera.setPixmap(
                pixmap.scaled(
                    self.kakera.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
            )
    def closeEvent(self, event):
        self.timer.stop()
        self.cap.release()
        event.accept()
class fullPegister(QMainWindow): 
    def __init__(self,operator_id):
        super().__init__()
        self.operator_id = operator_id
        self.centralwidget = QWidget()
        self.resize(400,250)
        self.fullReguster()
    def fullReguster(self): 
        self.Vbox = QVBoxLayout()
        self.setCentralWidget(self.centralwidget)
        self.centralwidget.setLayout(self.Vbox) 

        self.RegisterTrue = QLabel('Регистрация прошла успешно !')
        self.operatorOpregelen = QLabel('Оператор успешно зарегистрирован.')

        self.ynukId = QLabel('Ваш уникальный id номер: ')
        self.id_nomer = QLabel()
        self.id_nomer.setText(str(self.operator_id))

        self.btn_ok = QPushButton('Ок')
        self.btn_ok.clicked.connect(self.clik_btnOk)

        self.layoutBtnOk()
    def layoutBtnOk(self):
        self.Vbox.addStretch(1)
        self.Vbox.addWidget(self.RegisterTrue)
        self.Vbox.addStretch(1)

        self.Vbox.addWidget(self.operatorOpregelen)
    
        self.Vbox.addWidget(self.ynukId)
        self.Vbox.addWidget(self.id_nomer)
        self.Vbox.addWidget(self.btn_ok)
    def clik_btnOk(self): 
        self.close()
class avtoregust(QMainWindow): 
    def __init__(self):
        super().__init__()        
        self.centralwidget = QWidget()
        self.resize(400,250)
        self.aftoregister()
    def aftoregister(self): 
        self.Vbox = QVBoxLayout()
        self.setCentralWidget(self.centralwidget)

        self.Xbox = QHBoxLayout()
        self.centralwidget.setLayout(self.Vbox) 

        self.id_oper = QLabel('Авторезация оператора')
        self.id_name = QLabel('Введите ID')

        self.id_Edit = QLineEdit()

        self.btn_id = QPushButton('Авторезация')
        self.layout_id()
    def layout_id(self):
        self.setCentralWidget(self.centralwidget)
        
        self.Vbox.addWidget(self.id_oper)
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
        self.centralwidget.setLayout(self.centralWidget)
    def obekt(self): 
        self.xbox = QHBoxLayout()
        self.Vbox_plaxa =  QVBoxLayout()

        self.xbox.addLayout(self.Vbox)

        self.info = QPushButton('Инструкция ')
        self.analiz = QPushButton('Анализ')
        self.ypavlenue = QPushButton('Управление')

        self.fUO = QLabel('ФИО')
        self.timer_pytu = QLabel('Время в пути')
        self.timer = QLabel('Время')
        self.pylc = QLabel('Ваш пулс')
        self.pyls_izm = QLabel('---')

        self.kamera = QLabel('Камера')

    def Pylclayout(self):
        self.Vbox_plaxa.addWidget(self.info)
        self.Vbox_plaxa.addWidget(self.analiz)
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
    window = stapt_okno()  
    window.show()
    sys.exit(app.exec_())

