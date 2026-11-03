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
    QMessageBox, QGroupBox, QComboBox, QTextEdit, QSlider, QFileDialog,QDialog,QFrame,QLineEdit, QPlainTextEdit
)
class BlokC(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.cetnrwidget = QWidget()
        self.resize(1000,700)
        self.obektBlokaC()
        self.colorBlokC()
        self.layoutBlokC()
    def obektBlokaC(self):
        self.GlobalGridf = QGridLayout()
        self.name_proga = QLabel('НейроБодр')
        self.menu = QLabel('Меню управление')
        self.info = QLabel('Индефекация')
        
        self.btn1 = QPushButton('Инструкция')
        self.btn2 = QPushButton('Анализ')
        self.btn3 = QPushButton('Управленте')

        self.btn1.clicked.connect(self.showbtn1)
        self.btn2.clicked.connect(self.showbtn2)
        self.btn3.clicked.connect(self.showbtn3)
    def layoutBlokC(self):
        self.setCentralWidget(self.cetnrwidget)
        self.cetnrwidget.setLayout(self.GlobalGridf)

        self.GlobalGridf.addWidget(self.name_proga,0,0)
        self.GlobalGridf.addWidget(self.menu,0,1)
        self.GlobalGridf.addWidget(self.info,0,2)
        self.GlobalGridf.addWidget(self.btn1,2,0)
        self.GlobalGridf.addWidget(self.btn2,2,1)   
        self.GlobalGridf.addWidget(self.btn3,2,2)
        self.GlobalGridf.addWidget(self.    text_frame, 1, 0, 1, 3)       
        self.GlobalGridf.setRowStretch(1,1)
    def colorBlokC(self): 
        self.text_frame = QFrame()
        self.text_frame.setStyleSheet("""
        QFrame{
        border:2px solid gray;
        border-radius: 8px;
        background-color: white;
        }
         """)
        self.text_label = QLabel()
        self.text_label.setAlignment(Qt.AlignCenter)
        self.frams_label = QVBoxLayout(self.text_frame)
        self.frams_label.addWidget(self.text_label)
    def showbtn1(self):
        self.text_label.setText("""Зелный индикатор на видое означает, хоорошее состояние оператора
            Желтый индикатор на видео означает "Внимание" состояние оператора выходит за пределы нормы
            Красный индикатор на видео означает "Критическое" состояние""")
    def showbtn2(self): 
        self.
    def showbtn3(self): 
        pass 
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BlokC()  
    window.show()
    sys.exit(app.exec_())
