import os 
import csv
import cv2
import random
import sys 
import time,socket,threading,shutil
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
        self.next.clicked.connect(self.save)

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
                        if row.get('ID') == id_id:
                            self.hide()
                            self.Meep = biometr(row)
                            self.Meep.show()
                        else:
                            QMessageBox.warning(self, 'Ошибка', 'ID не найден')
class registration(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central = QWidget()
        self.resize(830, 310)
        self.object()
        self.camera =None 
        self.timer = QTimer(self)
        self.KameraStart()
        self.timer.timeout.connect(self.KameraUpdate)
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
                     #  self.next.setEnabled(True)
            else : 
               QMessageBox.warning(self, "Ошибка", "Возраст слишком маленький!")
    def KameraStart(self): 
        self.camera = cv2.VideoCapture(0)
    
        if not self.camera.isOpened(): 
            print('Камера не найдена')
            return
        self.timer.start(30)
    def KameraUpdate(self): 
        ret,frame = self.camera.read()
        if not ret : 
            print('Нету кадра')
            self.timer.stop()
            return
        rgv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h,w,ch = rgv.shape
        image = QImage(
            rgv.data,
            w,
            h,
            ch * w,
            QImage.Format_RGB888
        ).copy()
        pixel = QPixmap.fromImage(image)

        self.camm.setPixmap(
            pixel.scaled(300,300))  
class biometr(QMainWindow):
    def __init__(self, mlya=None):
        super().__init__()
        self.mlya = mlya or {}
        self.central = QWidget()
        self.resize(900,600)
        self.object()
    def object(self):
        self.name_program = QLabel('НейроБобр')

        self.bag = QLabel(f"ID: {self.mlya.get('ID', '')}")
        self.name1 = QLabel(f"Фамилия: {self.mlya.get('Фамилия', '')}")
        self.name2 = QLabel(f"Имя: {self.mlya.get('Имя', '')}")
        self.name3 = QLabel(f"Отчество: {self.mlya.get('Отчество', '')}")
        self.NameName = QLabel(f"Возраст: {self.mlya.get('Возраст', '')}")
        self.Po = QLabel('Время запуска ПО:')
        self.time = QLabel('Время в дороге:')
        self.ostatock = QLabel('Оставшееся время в дороге:')

        self.camm = QLabel('Камера')

        self.infoblock = QLabel('Информация об операторе')
        self.blockbast = QLabel('Информационный блок')
        self.ident = QLabel('Идентификация')

        self.photo = QPushButton('Записать фото')
        self.next = QPushButton('Далее')
        self.vvod = QLabel('После прохождения идентификации')
        self.vvod2 = QLabel('нажмите кнопку "Далее"')
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
        self.GlobalBox.addSpacing(40)
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
        self.InfoBox.addWidget(self.Po, alignment= Qt.AlignLeft)
        self.InfoBox.addWidget(self.time, alignment= Qt. AlignLeft)
        self.InfoBox.addWidget(self.ostatock, alignment= Qt.AlignLeft)

        self.CameraBox.addStretch(1)
        self.CameraBox.addWidget(self.camm, alignment= Qt.AlignCenter)

        self.IdBox.addWidget(self.bag, alignment= Qt.AlignRight) 
        self.IdBox.addWidget(self.vvod, alignment= Qt.AlignRight)  
        self.IdBox.addWidget(self.vvod2, alignment= Qt.AlignRight)

        self.BtnBox.addStretch(1)  
        self.BtnBox.addWidget(self.photo) 
        self.BtnBox.addStretch(1)   
        self.BtnBox.addWidget(self.next) 

        self.next.clicked.connect(self.flopa)
        self.colorBox()

    def colorBox(self):
        self.name_program.setStyleSheet("""color: #008000;
        font-size: 24px;
        """)
        self.infoblock.setStyleSheet('font-size: 15px;')
        self.blockbast.setStyleSheet('font-size: 15px;')
        self.ident.setStyleSheet('font-size: 15px;')
        self.camm.setStyleSheet('font-size: 16px;')

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

    def flopa(self):
        self.hide()
        self.doom = instruction(self.mlya)
        self.doom.show()

class instruction(QMainWindow):
    def __init__(self, mlya=None):
        super().__init__()
        self.mlya = mlya or {}
        self.central = QWidget()
        self.object()
    def object(self):
        self.name_program = QLabel('Нейробобр')
        self.menu = QLabel('Меню управления')
        self.ident = QLabel('Идентификация')
        self.instruction = QPushButton('Инструкция')
        self.analiz = QPushButton('Анализ')
        self.uprav = QPushButton('Управление')
        self.next = QPushButton('Далее')
        self.name1 = QLabel(f"Оператор {self.mlya.get('Фамилия', '')}")
        self.name2 = QLabel(f"определён: {self.mlya.get('Имя', '')}")
        self.vid = QLabel('Вид подключения')
        self.instruction2 = QLabel('Инструкция')
        self.green = QLabel('Зелёный индикатор обозначает хорошее состояние оператора.' \
        'Норма ЧСС. Оператор бодрствует')
        self.yellow = QLabel('Жёлтый индикатор означает состояние оператора немного выходит за пределы нормы.' \
        ' ЧСС чуть ниже или выше нормы. Наклон головы вбок или вперед/глаза закрыты дольше 4 секунд')
        self.red = QLabel('Красный индикатор означает критическое состояние оператора.' \
        ' ЧСС критически ниже или выше порога нормы. Наклон головы вбок или вперед/веки закрыты больше 7 секунд')
        self.map = QLabel('Наклеить электроды как показано на рисунке и подключить контакты')
        self.BoxBox()
    def BoxBox(self):
        self.GlobalBox = QVBoxLayout()
        self.NameBox = QVBoxLayout()
        self.BtnBox = QHBoxLayout()
        self.InfoBox = QVBoxLayout()
        self.HadpisiBox = QHBoxLayout()
        self.InstructionBox = QVBoxLayout()
        self.NadpiskiBox = QHBoxLayout()

        self.setCentralWidget(self.central)
        self.GlobalBox.addLayout(self.NameBox)
        self.GlobalBox.addLayout(self.HadpisiBox)
        self.GlobalBox.addLayout(self.InfoBox)
        self.GlobalBox.addLayout(self.BtnBox)
        self.GlobalBox.addLayout(self.NadpiskiBox)
        self.GlobalBox.addLayout(self.InstructionBox)
        self.central.setLayout(self.GlobalBox)

        self.NameBox.addWidget(self.name_program, alignment= Qt.AlignCenter)
        self.NameBox.addWidget(self.menu, alignment= Qt.AlignLeft)
        self.NameBox.addWidget(self.ident, alignment= Qt.AlignRight)

        self.BtnBox.addWidget(self.instruction, alignment= Qt.AlignLeft)
        self.BtnBox.addWidget(self.analiz, alignment= Qt.AlignCenter)
        self.BtnBox.addWidget(self.uprav, alignment= Qt.AlignRight)

        self.InfoBox.addWidget(self.name1, alignment= Qt.AlignRight)
        self.InfoBox.addWidget(self.name2, alignment= Qt.AlignRight)

        self.HadpisiBox.addWidget(self.instruction2, alignment= Qt.AlignLeft)
        self.HadpisiBox.addWidget(self.vid, alignment= Qt.AlignRight)
        
        self.InstructionBox.addWidget(self.green, alignment= Qt.AlignLeft)
        self.InstructionBox.addWidget(self.yellow, alignment= Qt.AlignLeft)
        self.InstructionBox.addWidget(self.red, alignment= Qt.AlignLeft)

        self.NadpiskiBox.addWidget(self.next, alignment= Qt.AlignRight)
        self.collor()

    def collor(self):
        self.name_program.setStyleSheet("""color: #008000;
        font-size: 25px;
        """)
        self.menu.setStyleSheet('font-size: 23px;')
        self.ident.setStyleSheet('font-size: 23px;')




                
        
                
if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    win = start()
    win.show()
    sys.exit(app.exec_())        