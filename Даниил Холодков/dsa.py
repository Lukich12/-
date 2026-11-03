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
class bloka (QMainWindow): 
    def __init__(self):
        super().__init__()
        self.resize(500,350)
        self.Hbox = QHBoxLayout()
        self.Vbox2 = QVBoxLayout()
        self.central_widget = QWidget()

        self.setCentralWidget(self.central_widget)
        self.Hbox.addLayout(self.Vbox2)
        self.central_widget.setLayout(self.Hbox)
        self.Obekt()
    def Obekt(self):
        self.register = register(self)
        self.natpuc = QLabel('Выберите необходимые действие') 
        self.btn_register = QPushButton('Регистрация')
        self.btn_aftoregister = QPushButton('Авторезация')

        self.btn_register.clicked.connect(self.clik_btnRegister)
        self.btn_aftoregister.clicked.connect(self.clik_btnAftoregister)
        self.BoxLayout()
    def BoxLayout(self):
        self.Vbox2.addWidget(self.natpuc,alignment=Qt.AlignCenter | Qt.AlignTop)

        self.Vbox2.addStretch(1)
        self.Vbox2.addWidget(self.btn_register,alignment=Qt.AlignCenter)
        self.Vbox2.addWidget(self.btn_aftoregister,alignment=Qt.AlignCenter)
        self.Vbox2.addStretch(1)

        self.btn_register.setFixedSize(200,60)
        self.btn_aftoregister.setFixedSize(200,60)
        self.ColorBlokA()
    def ColorBlokA(self): 
        self.natpuc.setStyleSheet('color: #000000;')
        self.btn_register.setStyleSheet('color: #000000; background-color: #808080')
        self.btn_aftoregister.setStyleSheet('color: #000000;  background-color: #808080')
    def clik_btnRegister(self): 
        self.hide()
        self.register.show()
    def clik_btnAftoregister(self): 
        self.hide()
        self.aftoregister.show()
class register(QMainWindow): 
    def __init__(self,main_window):
        super().__init__()
        self.centrWidtett = QWidget()
        self.main_window = main_window
        self.resize(1000,700)
        self.BlokB()
    def BlokB(self): 
        self.setCentralWidget(self.centrWidtett)

        self.MainVbox = QVBoxLayout()
        self.Hbox = QHBoxLayout()

        self.Vbox_title = QVBoxLayout()
        self.Vbox_user = QVBoxLayout()
        self.Vbox_kamera = QVBoxLayout()
        self.Vbox_id = QVBoxLayout()

        self.MainVbox.addLayout(self.Vbox_title)
        self.MainVbox.addLayout(self.Hbox)

        self.Hbox.addLayout(self.Vbox_user, 1)
        self.Hbox.addLayout(self.Vbox_kamera, 1)
        self.Hbox.addLayout(self.Vbox_id, 1)

        self.cap = cv2.VideoCapture(0)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_camera)
        self.timer.start(30)

        self.centrWidtett.setLayout(self.MainVbox)
        self.Obekt_blokab()
    def Obekt_blokab(self): 
        self.name_programma = QLabel('НейроБодр')
        self.name_programma2 = QLabel('Программа для мониторинга состояния водителей')

        self.register_oper = QLabel('Регистрация оператора')

        self.name_oper = QLineEdit()
        self.name2_oper = QLineEdit()
        self.name3_oper = QLineEdit()
        self.age_oper = QLineEdit()
        self.btn_dalle = QPushButton('Далее')

        self.kamera = QLabel('Камера')
        self.btn_kamera = QPushButton('Инденицикация')

        self.nameInfo_blok = QLabel('Информационный блок ')
        self.oper = QLabel('Оператор')
        self.id_edit = QLineEdit()
        self.info_blok = QLabel('Для запуска программы нажмите "Далее"')
        self.btn_blokDallee = QPushButton('Далее')

        self.kamera.setFixedSize(300,400)
        self.kamera.setText('Загрузка камеры')
        self.blokBLayout()
    def blokBLayout(self): 
        self.Vbox_title.addStretch(1)
        self.Vbox_title.addWidget(self.name_programma,alignment=Qt.AlignCenter)
        self.Vbox_title.addWidget(self.name_programma2,alignment=Qt.AlignCenter)
        self.Vbox_title.addStretch(1)

        self.Vbox_user.addWidget(self.register_oper, alignment=Qt.AlignCenter)
        self.from_layot = QFormLayout()
        self.Vbox_user.addLayout(self.from_layot)

        self.name_oper.setFixedSize(200, 30)
        self.name2_oper.setFixedSize(200, 30)
        self.name3_oper.setFixedSize(200, 30)
        self.age_oper.setFixedSize(200, 30)
        self.btn_dalle.setFixedSize(200,30)
    
        self.from_layot.setVerticalSpacing(10)
        self.from_layot.addRow("Фамилия",self.name_oper)
        self.from_layot.addRow("Имя", self.name2_oper)
        self.from_layot.addRow("Отчество", self.name3_oper)
        self.from_layot.addRow('Возраст', self.age_oper)
        self.Vbox_user.addWidget(self.btn_dalle)
        self.Vbox_user.addStretch(1)

        self.Vbox_kamera.addWidget(self.kamera, alignment=Qt.AlignCenter)
        self.Vbox_kamera.addWidget(self.btn_kamera, alignment=Qt.AlignCenter)
        self.Vbox_kamera.addStretch(1)

        self.id_edit.setFixedSize(200,30)
        self.Vbox_id.addWidget(self.nameInfo_blok, alignment=Qt.AlignCenter)
        self.Vbox_id.addWidget(self.id_edit)
        self.Vbox_id.addWidget(self.info_blok)
        self.Vbox_id.addWidget(self.btn_blokDallee)
        self.Vbox_id.addStretch(1)
        self.colorBlokB()
    def update_camera(self): 
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            image = QImage(
                frame.data, w, h,
                bytes_per_line,
                QImage.Format_RGB888
            ).copy()
            pixmap = QPixmap.fromImage(image)
            self.kamera.setPixmap(
                pixmap.scaled(
                    self.kamera.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
            )
class BlokC(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.cetnrwidget = QWidget()
    def obektBlokaC(self):
        self.menu = QLabel('Меню управление')
        self.btn1 = QPushButton('Инструкция')
        self.btn2 = QPushButton('Анализ')
        self.btn3 = QPushButton('Управленте')
    def layout(self):
        self.GlobalHbox = QHBoxLayout()
        self.Vbox = QVBoxLayout()
        self.Vbox2 = QVBoxLayout()
        self.GlobalHbox.addLayout(self.Vbox)
        self.GlobalHbox.addLayout(self.Vbox2)
        self.setCentralWidget(self.cetnrwidget) 
        self.GlobalHbox.addLayout(self.Vbox)
        self.GlobalHbox.addLayout(self.Vbox2)
    def ObertAnaliz(self):
        self.Vbox.addWidget(self.menu, alignment=Qt.AlignLeft | Qt.AlignVCenter )
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = bloka()  
    window.show()
    sys.exit(app.exec_())

