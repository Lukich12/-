# -*- coding: utf-8 -*-
"""Удалённый монитор диспетчера. Запуск: python remote_monitor.py [IP_водительского_ПК]"""
import sys, socket, json, os
from pathlib import Path
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

PORT = 50555
class RemoteWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NeuroMonitor — удалённый монитор диспетчера")
        self.resize(650, 520)
        self.sock = None
        self.buffer = b""
        self.data = {}
        self.setStyleSheet("""
            QMainWindow,QWidget{background:#101820;color:#eaf2f8;font-size:14px}
            QLineEdit{background:#192833;border:1px solid #3b5668;border-radius:6px;padding:8px;color:white}
            QPushButton{background:#263d4d;border:1px solid #426176;border-radius:8px;padding:9px 14px;font-weight:bold}
            QPushButton:hover{background:#1c8b5d}
        """)
        root=QWidget(); lay=QVBoxLayout(root)
        title=QLabel("ДИСПЕТЧЕРСКИЙ МОНИТОР"); title.setFont(QFont("Arial",18,QFont.Bold)); title.setStyleSheet("color:#5ee0a0")
        lay.addWidget(title)
        row=QHBoxLayout(); self.host=QLineEdit(sys.argv[1] if len(sys.argv)>1 else "127.0.0.1"); self.host.setPlaceholderText("IP компьютера водителя")
        self.connect_btn=QPushButton("Подключиться"); self.connect_btn.clicked.connect(self.connect_server)
        row.addWidget(QLabel("IP:")); row.addWidget(self.host,1); row.addWidget(self.connect_btn); lay.addLayout(row)
        self.id_label=QLabel("ID: —"); self.id_label.setStyleSheet("color:#9bb0bf")
        self.name=QLabel("Оператор не подключён"); self.name.setFont(QFont("Arial",15,QFont.Bold))
        self.age=QLabel("Возраст: —")
        self.pulse=QLabel("—"); self.pulse.setAlignment(Qt.AlignCenter); self.pulse.setFont(QFont("Arial",34,QFont.Bold))
        self.status=QLabel("НЕТ СВЯЗИ"); self.status.setAlignment(Qt.AlignCenter); self.status.setMinimumHeight(75); self.status.setFont(QFont("Arial",22,QFont.Bold))
        self.duration=QLabel("Время в пути: —")
        self.message=QLabel("Введите IP компьютера с основной программой и нажмите «Подключиться»."); self.message.setWordWrap(True)
        for x in [self.id_label,self.name,self.age,self.pulse,self.status,self.duration,self.message]: lay.addWidget(x)
        self.setCentralWidget(root)
        self.timer=QTimer(self); self.timer.timeout.connect(self.poll); self.timer.start(500)

    def connect_server(self):
        self.disconnect_server()
        try:
            self.sock=socket.create_connection((self.host.text().strip(),PORT),timeout=3)
            self.sock.settimeout(0.2)
            self.message.setText("Подключено. Ожидание данных...")
        except OSError as e:
            self.sock=None
            QMessageBox.warning(self,"Нет подключения",f"Не удалось подключиться: {e}\nПроверьте IP, брандмауэр и запуск основной программы.")
    def disconnect_server(self):
        if self.sock:
            try:self.sock.close()
            except OSError:pass
        self.sock=None; self.buffer=b""
    def poll(self):
        if not self.sock:return
        try:
            chunk=self.sock.recv(65536)
            if not chunk:
                self.disconnect_server(); self.message.setText("Соединение закрыто."); return
            self.buffer+=chunk
            while b"\n" in self.buffer:
                line,self.buffer=self.buffer.split(b"\n",1)
                if line:
                    try:self.render(json.loads(line.decode("utf-8")))
                    except (ValueError,UnicodeDecodeError):pass
        except socket.timeout: pass
        except OSError:
            self.disconnect_server(); self.message.setText("Соединение потеряно.")
    def render(self,d):
        self.data=d
        full=" ".join(x for x in [d.get("last_name",""),d.get("first_name",""),d.get("middle_name","")] if x).strip()
        self.id_label.setText("ID: "+str(d.get("id") or "—"))
        self.name.setText(full or "Оператор не выбран")
        self.age.setText("Возраст: "+str(d.get("age") or "—"))
        self.pulse.setText(f"{d.get('pulse','—')} уд/мин")
        self.duration.setText("Время в пути: "+str(d.get("drive_duration","00:00:00")))
        code=d.get("status","")
        color={"NORMAL":"#26c281","WARNING":"#f5c542","CRITICAL":"#ff5c62"}.get(code,"#657786")
        label=d.get("status_label","НЕТ ДАННЫХ")
        self.status.setText(label); self.status.setStyleSheet(f"background:{color};color:#101820;border-radius:10px;padding:10px")
        self.pulse.setStyleSheet(f"color:{color}")
        if code=="CRITICAL":
            self.message.setText("Требуется немедленное вмешательство! Свяжитесь с водителем.")
        elif code=="WARNING":
            self.message.setText("Состояние выходит за пределы нормы. Необходимо связаться с водителем.")
        elif d.get("id"):
            self.message.setText("Мониторинг активен · обновлено "+str(d.get("updated_at","")))
        else:
            self.message.setText("Ожидание авторизации оператора на основной программе.")
    def closeEvent(self,event):
        self.disconnect_server();event.accept()

if __name__=="__main__":
    app=QApplication(sys.argv); win=RemoteWindow();win.show();sys.exit(app.exec_())
