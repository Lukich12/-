import json
import serial
import cv2
import uuid 
#import face_recognition
import os  
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

        self.Vbox.addLayout(self.Xbox)

        self.id_oper = QLabel('Авторезация оператора')

        self.id_Edit = QLineEdit()

        self.btn_id = QPushButton('Авторезация')
        self.layout_id()
    def layout_id(self):

        self.from_layoter = QFormLayout()
        self.Vbox.addLayout(self.from_layoter)

        self.Xbox.addWidget(self.id_oper)

        self.from_layoter.addRow('Введите ID',self.id_Edit)
        
        self.Vbox.addWidget(self.btn_id)


        self.btn_id.clicked.connect(self.clik_btn_id)
        self.color_id()
    def color_id(self): 
        self.id_oper.setStyleSheet('color: #000000')
        self.id_Edit.setStyleSheet('background-color: #FFFFFF ; color: #FFFFFF')
        self.btn_id.setStyleSheet('background-color : #0000FF  ; color: #FFFFFF')
    def clik_btn_id(self): 
        self.hide()
        self.avtoregust.show()
    def proverka(self): 
        proverka = self.id_Edit.text()
        with open ('Operator/operators', 'r', encoding="utf-8") as file1: 
            for file1 in proverka : 
                 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = avtoregust()  
    window.show()
    sys.exit(app.exec_())
