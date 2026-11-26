import os 
import csv
import random
import sys,time,socket,threading,shutil
from datetime import datetime, date
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QPixmap,QPalette,QColor,QImage
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton,
    QSpinBox, QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout, QTabWidget,
    QMessageBox, QGroupBox, QComboBox, QTextEdit, QSlider, QFileDialog,QDialog
)

class start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central = QWidget()
        self.object()
    def object(self):
        self.name_program = QLabel('НейроБобр')
        self.deystvie = QLabel('Выберите действие:')
        self.registration = QPushButton('Регистрация')
        self.autorisation = QPushButton('Авторизация')
        self.BoxBox()
    def BoxBox(self):
        self.GlobalBox = QVBoxLayout()
        self.NameBox = QVBoxLayout()
        self.BtnBox = QHBoxLayout()

        self.setCentralWidget(self.central)
        self.GlobalBox.addLayout(self.NameBox)
        self.GlobalBox.addLayout(self.BtnBox)
        self.central.setLayout(self.GlobalBox)

        self.NameBox.addWidget(self.name_program, alignment= Qt.AlignCenter)
        self.NameBox.addWidget(self.deystvie, alignment= Qt.AlignCenter)
        self.BtnBox.addWidget(self.autorisation, alignment= Qt.AlignRight)
        self.BtnBox.addWidget(self.registration, alignment= Qt.AlignLeft)

        self.registration.clicked.connect(self.flopa)
        self.autorisation.clicked.connect(self.pelmen)

        self.color()
    def color(self):
        self.name_program.setStyleSheet('color: #008000;')
        self.registration.setStyleSheet("""
        QPushButton{
        background-color: #000000;
        color: #ffffff;
        }
        QPushButton:hover{
        background-color: #008000;
        color: #000000;
        }
        """)
        self.autorisation.setStyleSheet("""
        QPushButton{
        background-color: #000000;
        color: #ffffff;
        }
        QPushButton:hover{
        background-color: #008000;
        color: #000000;
        }
        """)
    def flopa(self):
        self.hide()
        self.doom = registration()
        self.doom.show()
    def pelmen(self):
        self.hide()
        self.damn = autorisation()
        self.damn.show()
class autorisation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central = QWidget()
        self.object()
    def object(self):
        self.name_program = QLabel('НейроБобр')
        self.vvod = QLabel('Введите ID в строку')
        self.id = QLineEdit()
        self.next = QPushButton('Далее')
        self.exit = QPushButton('Выход')
        self.BoxBox()
    def BoxBox(self):
        self.GlobalBox = QVBoxLayout()
        self.NameBox = QVBoxLayout()
        self.BlockBox = QFormLayout()
        self.BtnBox = QHBoxLayout()

        self.setCentralWidget(self.central)
        self.GlobalBox.addLayout(self.NameBox)
        self.GlobalBox.addLayout(self.BlockBox)
        self.GlobalBox.addLayout(self.BtnBox)
        self.central.setLayout(self.GlobalBox)

        self.NameBox.addWidget(self.name_program, alignment= Qt.AlignCenter)
        self.NameBox.addWidget(self.vvod, alignment= Qt.AlignCenter)
        self.BlockBox.addRow('введите ID', self.id)
        self.setFixedWidth(200)
        self.BtnBox.addWidget(self.next, alignment= Qt.AlignRight)
        self.BtnBox.addWidget(self.exit, alignment= Qt.AlignLeft)

        self.exit.clicked.connect(self.flopa)
        self.next.clicked.connect(self.pelmen)

        self.color()
    def color(self):
        self.name_program.setStyleSheet('color: #008000; font-size: 24px;')
        self.next.setStyleSheet("""
        QPushButton{
        background-color: #000000;
        color: #ffffff;
        }
        QPushButton:hover{
        background-color: #008000;
        color: #000000;
        }
        """)
        self.exit.setStyleSheet("""
        QPushButton{
        background-color: #000000;
        color: #ffffff;
        }
        QPushButton:hover{
        background-color: #008000;
        color: #000000;
        }
        """)
    def flopa(self):
        app.exit()
    def pelmen(self):
        self.hide()
        self.damn = biometr()
        self.damn.show()
    def save(self):
        id_text = self.id.text()
        file = 'operator/operator1.csv'
        if id_text != '' :
            try :
                id_id = str(id_text)
            except ValueError:
                print('перепиши')
                return
            os.makedirs('operator', exist_ok=True)
            if os.path.exists(file) :
                with open(file,'r', newline='', encoding='utf-8') as f:
                    cat = csv.DictReader(f)
                    for row in cat:
                        if row.get('id') == id_id:
                            self.hide()
                            self.Meep = self.emg()
                            self.Meep.show()
class registration(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central = QWidget()
        self,self.resize(830, 310)
        self.object()
    def object(self):
        self.name_program = QLabel('НейроБобр')
        self.next = QPushButton('Далее')
        self.exit = QPushButton('Выход')

        self.name1 = QLineEdit()
        self.name2 = QLineEdit()
        self.name3 = QLineEdit()
        self.age = QLineEdit()

        self.zapic = QPushButton('Записать')
        self.photo = QPushButton('Записать фото')

        self.info = QLabel('Информация об операторе')
        self.ident = QLabel('Идентификация')
        self.infoblock = QLabel('Блок информации')
        self.camm = QLabel('Камера')
        self.BoxBox()
    def BoxBox(self):
        self.GlobalBox = QVBoxLayout()
        self.NameBox = QVBoxLayout()
        self.BlockBox = QFormLayout()
        self.CameraBox = QVBoxLayout()
        self.NameBlockBox = QHBoxLayout()
        self.BtnBox = QHBoxLayout()

        self.GlobalBox.addLayout(self.NameBox)
        self.GlobalBox.addLayout(self.NameBlockBox)
        self.GlobalBox.addLayout(self.BlockBox)
        self.GlobalBox.addLayout(self.CameraBox)
        self.GlobalBox.addLayout(self.BtnBox)
        self.central.setLayout(self.GlobalBox)
        self.setCentralWidget(self.central)

        self.NameBox.addWidget(self.name_program, alignment= Qt.AlignCenter)
        self.NameBlockBox.addWidget(self.info, alignment= Qt.AlignLeft)
        self.NameBlockBox.addWidget(self.ident, alignment= Qt.AlignCenter)
        self.NameBlockBox.addWidget(self.infoblock, alignment= Qt.AlignRight)

        self.BlockBox.addRow('Фамилия', self.name1)
        self.BlockBox.addRow('Имя', self.name2)
        self.BlockBox.addRow('Отчество', self.name3)
        self.BlockBox.addRow('Возраст', self.age)

        self.CameraBox.addWidget(self.camm, alignment= Qt.AlignCenter)

        self.BtnBox.addWidget(self.zapic,alignment=Qt.AlignLeft)
        self.BtnBox.addWidget(self.photo, alignment=Qt.AlignCenter)
        self.BtnBox.addWidget(self.next, alignment=Qt.AlignRight)

        self.name1.setFixedWidth(200)
        self.name2.setFixedWidth(200)
        self.name3.setFixedWidth(200)
        self.age.setFixedWidth(200)

        self.photo.setEnabled(False)
     #   self.next.setEnabled(False)
        self.zapic.clicked.connect(self.proverka)
     # self.photo.clicked.connect(self.SavePhoto)

        self.color()

    def color(self):
        self.name_program.setStyleSheet("""color: #008000;
        font-size: 24px;
        """)
        self.zapic.setStyleSheet("""
        QPushButton{
            background-color: #000000;
            color: white;
        }
        QPushButton:hover{
            background-color: #008000;
            color: #000000;
        }
        """)
        self.photo.setStyleSheet("""
        QPushButton{
            background-color: #000000;
            color: white;
            }
        QPushButton:hover{
            background-color: #008000;
            color: #000000
        }
        """)
        self.next.setStyleSheet("""
        QPushButton{
            background-color: #000000;
            color: white;
            }
        QPushButton:hover{
            background-color: #008000;
            color: #000000
        }
        """)
    def proverka(self):
        name1 = self.name1.text()
        name2 = self.name2.text()
        name3 = self.name3.text()
        age = self.age.text()
        file = 'operator/operator1.csv'  

        bag = random.randint(1, 10000000)
        if name1 != '' and name2 != '' and age != '' :
            try:
                NameName = int(age)
            except ValueError:
                QMessageBox.warning(self, 'Ошибка!', 'Введите возраст корректно')
                return
            if NameName >= 18 :
                os.makedirs('operator', exist_ok=True)
                if not os.path.exists(file):
                    with open(file, 'w', newline='', encoding='utf-8') as f:
                        dog = csv.writer(f)
                        dog.writerow(['ID', 'Фамилия', 'Имя', 'Отчество', 'Возраст'])
                        dog.writerow([bag, name1, name2, name3, NameName])
                        self.hide()
                else:
                    with open(file, 'a', newline='', encoding='utf-8' ) as f:
                        god = csv.writer(f)
                        god.writerow([bag, name1, name2, name3, NameName])
                        self.photo.setEnabled(True)
                     #   self.next.setEnabled(True)
            else : 
               QMessageBox.warning(self, "Ошибка", "Возраст слишком маленький!")
class biometr(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central = QWidget()
        self.object()
    def object(self):
        self.name_program = QLabel('НейроБобр')

        self.bag = QLabel('ID')
        self.name1 = QLabel('Фамилия')
        self.name2 = QLabel('Имя')
        self.name3 = QLabel('Отчество')
        self.NameName = QLabel('Возраст:')
        self.Po = QLabel('Время запуска ПО:')
        self.time = QLabel('Время в дороге:')
        self.ostatock = QLabel('Оставшееся время в дороге:')

        self.camm = QLabel('Камера')

        self.infoblock = QLabel('Информация об операторе')
        self.blockbast = QLabel('Информационный блок')
        self.ident = QLabel('Идентификация')

        self.photo = QPushButton('Записать фото')
        self.next = QPushButton('Далее')
        self.vvod = QLabel('После прохождения идентификации нажмите кнопку далее')
        self.BoxBox()
    def BoxBox(self):
        self.GlobalBox = QVBoxLayout()
        self.NameBox = QVBoxLayout()
        self.InfoBox = QVBoxLayout()
        self.CameraBox = QVBoxLayout()
        self.IdBox = QVBoxLayout()
        self.HadpisiBox = QHBoxLayout()
        self.BtnBox = QHBoxLayout()

        self.setCentralWidget(self.central)
        self.GlobalBox.addLayout(self.NameBox)
        self.GlobalBox.addLayout(self.HadpisiBox)
        self.GlobalBox.addLayout(self.InfoBox)
        self.GlobalBox.addLayout(self.CameraBox)
        self.GlobalBox.addLayout(self.IdBox)
        self.GlobalBox.addLayout(self.BtnBox)
        self.central.setLayout(self.GlobalBox)

        self.NameBox.addWidget(self.name_program, alignment= Qt.AlignCenter)

        self.HadpisiBox.addWidget(self.infoblock, alignment= Qt.AlignLeft)
        self.HadpisiBox.addWidget(self.ident, alignment= Qt.AlignCenter)
        self.HadpisiBox.addWidget(self.blockbast, alignment= Qt.AlignRight)

        self.InfoBox.addWidget(self.name1, alignment= Qt.AlignLeft)
        self.InfoBox.addWidget(self.name2, alignment= Qt.AlignLeft)
        self.InfoBox.addWidget(self.name3, alignment= Qt.AlignLeft)
        self.InfoBox.addWidget(self.NameName, alignment= Qt.AlignLeft)

        self.CameraBox.addWidget(self.camm, alignment= Qt.AlignCenter)

        self.IdBox.addWidget(self.bag, alignment= Qt.AlignRight)
        self.IdBox.addWidget(self.vvod, alignment= Qt.AlignRight)

        self.BtnBox.addWidget(self.photo, alignment= Qt.AlignCenter)
        self.BtnBox.addWidget(self.next, alignment= Qt.AlignRight)
        self.colorBox()

    def colorBox(self):
        self.name_program.setStyleSheet("""color: #008000;
        font-size: 24px;
        """)
        self.infoblock.setStyleSheet('font-size: 20px;')
        self.blockbast.setStyleSheet('font-size: 20px;')
        self.ident.setStyleSheet('font-size: 20px;')

        self.photo.setStyleSheet("""
        QPushButton{
            background-color: #000000;
            color: white;
            }
        QPushButton:hover{
            background-color: #008000;
            color: #000000
        }
        """)
        self.next.setStyleSheet("""
        QPushButton{
            background-color: #000000;
            color: white;
            }
        QPushButton:hover{
            background-color: #008000;
            color: #000000
        }
        """)
                
        
                
if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    win = start()
    win.show()
    sys.exit(app.exec_())        
