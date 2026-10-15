# -*- coding: utf-8 -*-

"""Учебный прототип конкурсного задания «Проектирование нейроинтерфейсов».
Запуск: python main.py
"""
import sys, csv, json, time, socket, threading, shutil
from pathlib import Path
from datetime import datetime, date
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton,
    QSpinBox, QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout, QTabWidget,
    QMessageBox, QGroupBox, QComboBox, QTextEdit, QSlider, QFileDialog
)

ROOT = Path(__file__).resolve().parent
DB = ROOT / "operators_db.csv"
PHOTOS = ROOT / "operators"
PORT = 50555
FIELDS = [
    "id", "last_name", "first_name", "middle_name", "age", "date", "time",
    "software_start_time", "drive_duration", "pulse_threshold_critical",
    "pulse_normal", "current_pulse", "operator_status"
]

def now_text(fmt="%H:%M:%S"):
    return datetime.now().strftime(fmt)

def read_operators():
    if not DB.exists():
        return []
    with DB.open("r", newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def write_operators(rows):
    with DB.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in FIELDS})

def get_operator(op_id):
    return next((r for r in read_operators() if r.get("id") == str(op_id).strip()), None)

def save_operator(row):
    rows = read_operators()
    rows.append(row)
    write_operators(rows)

def update_operator(op_id, **changes):
    rows = read_operators()
    for row in rows:
        if row.get("id") == str(op_id):
            row.update(changes)
            break
    write_operators(rows)

class MonitorServer:
    """Отправляет последний снимок состояния удалённому приложению по TCP."""
    def __init__(self):
        self.data = {}
        self.lock = threading.Lock()
        self.running = True
        self.clients = set()
        self.thread = threading.Thread(target=self._serve, daemon=True)
        self.thread.start()

    def update(self, data):
        with self.lock:
            self.data = dict(data)

    def _serve(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind(("0.0.0.0", PORT))
            s.listen(5)
            s.settimeout(1)
            while self.running:
                try:
                    conn, _ = s.accept()
                    threading.Thread(target=self._client, args=(conn,), daemon=True).start()
                except socket.timeout:
                    continue
        except OSError:
            pass
        finally:
            s.close()

    def _client(self, conn):
        try:
            conn.settimeout(3)
            while self.running:
                with self.lock:
                    payload = json.dumps(self.data, ensure_ascii=False).encode("utf-8") + b"\n"
                conn.sendall(payload)
                time.sleep(1)
        except (OSError, ConnectionError):
            pass
        finally:
            try: conn.close()
            except OSError: pass

    def stop(self):
        self.running = False

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NeuroMonitor — мониторинг состояния оператора")
        self.resize(1100, 760)
        self.operator = None
        self.pulse = 72
        self.pulse_normal = 75
        self.pulse_critical = 100
        self.drive_seconds = 0
        self.started_at = time.time()
        self.camera = None
        self.server = MonitorServer()
        self._build_ui()
        self._load_operator_list()
        self.clock = QTimer(self)
        self.clock.timeout.connect(self._tick)
        self.clock.start(1000)
        self._log("Программа запущена. Данные хранятся локально в operators_db.csv.")

    def _build_ui(self):
        self.setStyleSheet("""
            QMainWindow, QWidget { background:#101820; color:#eaf2f8; font-size:14px; }
            QGroupBox { border:1px solid #334b5c; border-radius:10px; margin-top:12px; padding:12px; font-weight:bold; }
            QGroupBox::title { subcontrol-origin:margin; left:12px; padding:0 5px; color:#5ee0a0; }
            QLineEdit, QSpinBox, QComboBox, QTextEdit { background:#192833; border:1px solid #3b5668; border-radius:6px; padding:7px; color:#fff; }
            QPushButton { background:#263d4d; border:1px solid #426176; border-radius:8px; padding:9px 14px; font-weight:bold; }
            QPushButton:hover { background:#1c8b5d; border-color:#5ee0a0; }
            QPushButton:disabled { color:#778899; background:#1a242c; }
            QTabWidget::pane { border:1px solid #334b5c; border-radius:8px; }
            QTabBar::tab { background:#1a2a35; padding:12px 18px; margin:2px; border-radius:6px; }
            QTabBar::tab:selected { background:#167a54; }
            QSlider::groove:horizontal { height:8px; background:#304653; border-radius:4px; }
            QSlider::handle:horizontal { background:#5ee0a0; width:18px; margin:-5px 0; border-radius:9px; }
        """)
        root = QWidget()
        layout = QVBoxLayout(root)
        header = QHBoxLayout()
        title = QLabel("NEUROMONITOR")
        title.setFont(QFont("Arial", 22, QFont.Bold))
        title.setStyleSheet("color:#5ee0a0;")
        subtitle = QLabel("Система контроля состояния оператора · учебный прототип")
        subtitle.setStyleSheet("color:#9bb0bf;")
        header.addWidget(title)
        header.addSpacing(18)
        header.addWidget(subtitle)
        header.addStretch()
        self.clock_label = QLabel()
        header.addWidget(self.clock_label)
        layout.addLayout(header)

        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)
        self.tabs.addTab(self._registration_tab(), "Регистрация")
        self.tabs.addTab(self._auth_tab(), "Авторизация")
        self.tabs.addTab(self._instruction_tab(), "Инструкция")
        self.tabs.addTab(self._analysis_tab(), "Анализ")
        self.tabs.addTab(self._control_tab(), "Управление")
        self.tabs.addTab(self._log_tab(), "Журнал")
        self.setCentralWidget(root)

    def _registration_tab(self):
        w = QWidget(); outer = QVBoxLayout(w)
        formbox = QGroupBox("Регистрация нового оператора (возраст от 18 лет)")
        form = QFormLayout(formbox)
        self.last_name = QLineEdit(); self.last_name.setPlaceholderText("Иванов")
        self.first_name = QLineEdit(); self.first_name.setPlaceholderText("Иван")
        self.middle_name = QLineEdit(); self.middle_name.setPlaceholderText("Иванович (необязательно)")
        self.age = QSpinBox(); self.age.setRange(0, 120); self.age.setValue(18)
        form.addRow("Фамилия *", self.last_name)
        form.addRow("Имя *", self.first_name)
        form.addRow("Отчество", self.middle_name)
        form.addRow("Возраст *", self.age)
        outer.addWidget(formbox)
        actions = QHBoxLayout()
        self.register_btn = QPushButton("Записать данные")
        self.register_btn.clicked.connect(self.register_operator)
        self.photo_btn = QPushButton("Сделать фото")
        self.photo_btn.clicked.connect(self.capture_photo)
        self.photo_btn.setEnabled(False)
        actions.addWidget(self.register_btn); actions.addWidget(self.photo_btn); actions.addStretch()
        outer.addLayout(actions)
        self.reg_status = QLabel("Заполните поля и нажмите «Записать данные».")
        self.reg_status.setWordWrap(True)
        self.reg_status.setStyleSheet("color:#9bb0bf; padding:8px;")
        outer.addWidget(self.reg_status)
        self.photo_preview = QLabel("Фото оператора не выбрано")
        self.photo_preview.setAlignment(Qt.AlignCenter)
        self.photo_preview.setMinimumHeight(180)
        self.photo_preview.setStyleSheet("border:1px dashed #426176; border-radius:8px; color:#9bb0bf;")
        outer.addWidget(self.photo_preview, 1)
        note = QLabel("Если камера недоступна, можно выбрать готовое изображение. Реальное распознавание личности не заявляется.")
        note.setStyleSheet("color:#9bb0bf;")
        outer.addWidget(note)
        self.choose_photo_btn = QPushButton("Выбрать фото из файла")
        self.choose_photo_btn.clicked.connect(self.choose_photo)
        outer.addWidget(self.choose_photo_btn)
        return w

    def _auth_tab(self):
        w = QWidget(); lay = QVBoxLayout(w)
        box = QGroupBox("Авторизация по ID")
        form = QFormLayout(box)
        self.auth_id = QLineEdit(); self.auth_id.setPlaceholderText("Введите ID оператора")
        form.addRow("ID оператора", self.auth_id)
        self.auth_btn = QPushButton("Авторизоваться")
        self.auth_btn.clicked.connect(self.authorize)
        lay.addWidget(box); lay.addWidget(self.auth_btn)
        self.auth_info = QLabel("После авторизации данные появятся здесь.")
        self.auth_info.setWordWrap(True); self.auth_info.setStyleSheet("padding:14px; background:#192833; border-radius:8px;")
        lay.addWidget(self.auth_info)
        self.auth_photo = QLabel("Фото")
        self.auth_photo.setAlignment(Qt.AlignCenter); self.auth_photo.setMinimumHeight(200)
        self.auth_photo.setStyleSheet("border:1px dashed #426176; border-radius:8px;")
        lay.addWidget(self.auth_photo, 1)
        self.continue_btn = QPushButton("Далее — открыть управление")
        self.continue_btn.setEnabled(False)
        self.continue_btn.clicked.connect(lambda: self.tabs.setCurrentIndex(4))
        lay.addWidget(self.continue_btn)
        return w

    def _instruction_tab(self):
        w = QWidget(); lay = QVBoxLayout(w)
        title = QLabel("Инструкция по индикаторам состояния")
        title.setFont(QFont("Arial", 17, QFont.Bold)); lay.addWidget(title)
        for color, name, text in [
            ("#26c281", "НОРМА", "Оператор бодрствует, пульс находится в допустимом диапазоне."),
            ("#f5c542", "ВНИМАНИЕ", "Пульс отклоняется от нормы примерно на 20%, но не достиг критического порога; в полной версии сюда также относятся признаки микросна или наклона головы."),
            ("#ff5c62", "КРИТИЧНО", "Пульс достиг критического порога или существенно ниже нормы; в полной версии сюда относятся длительное закрытие век и наклон головы.")
        ]:
            row = QHBoxLayout()
            dot = QLabel("●"); dot.setStyleSheet(f"color:{color}; font-size:28px;")
            name_lbl = QLabel(name); name_lbl.setMinimumWidth(130); name_lbl.setFont(QFont("Arial", 12, QFont.Bold))
            desc = QLabel(text); desc.setWordWrap(True)
            row.addWidget(dot); row.addWidget(name_lbl); row.addWidget(desc, 1)
            lay.addLayout(row)
        lay.addStretch()
        info = QLabel("Важно: статусы и звуковые предупреждения в этом учебном прототипе служат демонстрацией алгоритма, а не медицинской диагностикой.")
        info.setWordWrap(True); info.setStyleSheet("color:#f5c542; padding:10px;")
        lay.addWidget(info)
        return w

    def _analysis_tab(self):
        w = QWidget(); lay = QVBoxLayout(w)
        box = QGroupBox("Настройки анализа пульса")
        form = QFormLayout(box)
        self.normal_spin = QSpinBox(); self.normal_spin.setRange(30, 220); self.normal_spin.setValue(75)
        self.critical_spin = QSpinBox(); self.critical_spin.setRange(40, 250); self.critical_spin.setValue(100)
        form.addRow("Норма пульса (уд/мин)", self.normal_spin)
        form.addRow("Критический порог (уд/мин)", self.critical_spin)
        lay.addWidget(box)
        btns = QHBoxLayout()
        save = QPushButton("Записать настройки")
        save.clicked.connect(self.save_analysis)
        self.port_combo = QComboBox()
        self.port_combo.addItems(["Авто / не подключено"])
        self.refresh_ports_btn = QPushButton("Обновить COM-порты")
        self.refresh_ports_btn.clicked.connect(self.refresh_ports)
        btns.addWidget(save); btns.addWidget(self.port_combo); btns.addWidget(self.refresh_ports_btn)
        lay.addLayout(btns)
        self.signal_label = QLabel("Проверка сигнала: демонстрационный режим")
        self.signal_label.setStyleSheet("background:#192833; padding:12px; border-radius:8px;")
        lay.addWidget(self.signal_label)
        self.analysis_operator = QLabel("Сначала зарегистрируйте или авторизуйте оператора.")
        lay.addWidget(self.analysis_operator)
        lay.addStretch()
        return w

    def _control_tab(self):
        w = QWidget(); lay = QVBoxLayout(w)
        top = QHBoxLayout()
        self.status_badge = QLabel("НОРМА")
        self.status_badge.setAlignment(Qt.AlignCenter)
        self.status_badge.setMinimumHeight(90)
        self.status_badge.setFont(QFont("Arial", 24, QFont.Bold))
        self.pulse_big = QLabel("72")
        self.pulse_big.setAlignment(Qt.AlignCenter)
        self.pulse_big.setFont(QFont("Arial", 34, QFont.Bold))
        top.addWidget(self._card("СОСТОЯНИЕ", self.status_badge), 2)
        top.addWidget(self._card("ПУЛЬС · уд/мин", self.pulse_big), 1)
        lay.addLayout(top)
        self.operator_summary = QLabel("Оператор не выбран. Перейдите в «Авторизация» или зарегистрируйте оператора.")
        self.operator_summary.setWordWrap(True); self.operator_summary.setStyleSheet("background:#192833; padding:12px; border-radius:8px;")
        lay.addWidget(self.operator_summary)
        box = QGroupBox("Симулятор пульса — для тестирования без датчика")
        b = QVBoxLayout(box)
        self.pulse_slider = QSlider(Qt.Horizontal); self.pulse_slider.setRange(35, 160); self.pulse_slider.setValue(72)
        self.pulse_slider.valueChanged.connect(self._sim_pulse_changed)
        self.pulse_value = QLabel("72 уд/мин"); self.pulse_value.setAlignment(Qt.AlignCenter)
        b.addWidget(self.pulse_slider); b.addWidget(self.pulse_value)
        quick = QHBoxLayout()
        for val, label in [(72, "Норма: 72"), (55, "Внимание: 55"), (130, "Критично: 130")]:
            bt = QPushButton(label); bt.clicked.connect(lambda checked=False, v=val: self.pulse_slider.setValue(v)); quick.addWidget(bt)
        b.addLayout(quick); lay.addWidget(box)
        row = QHBoxLayout()
        self.drive_label = QLabel("Время в пути: 00:00:00")
        self.remaining_label = QLabel("Осталось: 09:00:00")
        row.addWidget(self.drive_label); row.addStretch(); row.addWidget(self.remaining_label)
        lay.addLayout(row)
        self.start_drive_btn = QPushButton("Начать отсчёт времени в пути")
        self.start_drive_btn.setCheckable(True)
        self.start_drive_btn.toggled.connect(self._toggle_drive)
        self.stop_btn = QPushButton("Стоп программа")
        self.stop_btn.clicked.connect(self.stop_program)
        lay.addWidget(self.start_drive_btn); lay.addWidget(self.stop_btn)
        self.control_message = QLabel("Состояние вычисляется по демонстрационному пульсу.")
        self.control_message.setWordWrap(True); lay.addWidget(self.control_message)
        lay.addStretch()
        return w

    def _card(self, heading, widget):
        box = QGroupBox(heading)
        lay = QVBoxLayout(box); lay.addWidget(widget)
        return box

    def _log_tab(self):
        w = QWidget(); lay = QVBoxLayout(w)
        self.log_text = QTextEdit(); self.log_text.setReadOnly(True)
        lay.addWidget(self.log_text)
        btn = QPushButton("Очистить журнал"); btn.clicked.connect(self.log_text.clear)
        lay.addWidget(btn)
        return w

    def _log(self, message):
        if hasattr(self, "log_text"):
            self.log_text.append(f"[{now_text()}] {message}")

    def _load_operator_list(self):
        PHOTOS.mkdir(exist_ok=True)

    def register_operator(self):
        last = self.last_name.text().strip()
        first = self.first_name.text().strip()
        middle = self.middle_name.text().strip()
        age = self.age.value()
        if not last or not first:
            QMessageBox.warning(self, "Проверка данных", "Заполните фамилию и имя.")
            return
        if age < 18:
            QMessageBox.warning(self, "Возрастное ограничение", "Регистрация разрешена только с 18 лет.")
            return
        rows = read_operators()
        new_id = str(max([int(r.get("id") or 0) for r in rows if str(r.get("id") or "").isdigit()] + [0]) + 1)
        now = datetime.now()
        row = {
            "id": new_id, "last_name": last, "first_name": first, "middle_name": middle,
            "age": str(age), "date": now.strftime("%d-%m-%Y"), "time": now.strftime("%H:%M:%S"),
            "software_start_time": now.strftime("%H:%M:%S"), "drive_duration": "00:00:00",
            "pulse_threshold_critical": str(self.critical_spin.value()),
            "pulse_normal": str(self.normal_spin.value()), "current_pulse": str(self.pulse),
            "operator_status": "NORMAL"
        }
        save_operator(row)
        self.operator = row
        self.photo_btn.setEnabled(True)
        self.reg_status.setText(f"Оператор записан. Присвоен ID: {new_id}. Теперь сделайте фото или выберите изображение.")
        self.auth_id.setText(new_id)
        self._update_operator_ui()
        self._log(f"Зарегистрирован оператор ID={new_id}: {last} {first}.")
        QMessageBox.information(self, "Успешно", f"Данные сохранены в operators_db.csv.\nID оператора: {new_id}")

    def choose_photo(self):
        if not self.operator:
            QMessageBox.information(self, "Фото", "Сначала запишите данные оператора.")
            return
        path, _ = QFileDialog.getOpenFileName(self, "Выберите фотографию", "", "Изображения (*.png *.jpg *.jpeg *.bmp)")
        if path:
            dest = PHOTOS / f"ID_{self.operator['id']}.jpg"
            try:
                pix = QPixmap(path)
                if pix.isNull(): raise ValueError("Не удалось прочитать изображение")
                pix.save(str(dest), "JPG")
                self._show_photo(dest, self.photo_preview)
                self.reg_status.setText(f"Фото сохранено: {dest.relative_to(ROOT)}")
                self._log(f"Сохранено фото для ID={self.operator['id']}.")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка фото", str(e))

    def capture_photo(self):
        # Camera capture is optional; OpenCV is imported only when requested.
        if not self.operator:
            return
        try:
            import cv2
            cap = cv2.VideoCapture(0)
            ok, frame = cap.read()
            cap.release()
            if not ok:
                raise RuntimeError("Камера не вернула изображение.")
            dest = PHOTOS / f"ID_{self.operator['id']}.jpg"
            cv2.imwrite(str(dest), frame)
            self._show_photo(dest, self.photo_preview)
            self.reg_status.setText(f"Фото с камеры сохранено: {dest.name}")
            self._log(f"Сделан снимок с камеры для ID={self.operator['id']}.")
        except Exception as e:
            QMessageBox.warning(self, "Камера недоступна", f"{e}\nМожно выбрать фотографию из файла.")

    def _show_photo(self, path, label):
        pix = QPixmap(str(path))
        if not pix.isNull():
            label.setPixmap(pix.scaled(label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def authorize(self):
        op_id = self.auth_id.text().strip()
        if not op_id:
            QMessageBox.warning(self, "Авторизация", "Введите ID оператора.")
            return
        row = get_operator(op_id)
        if not row:
            self.continue_btn.setEnabled(False)
            self.auth_info.setText("ID не найден. Проверьте номер и повторите попытку.")
            QMessageBox.warning(self, "Ошибка авторизации", "ID не найден.")
            self._log(f"Неудачная авторизация: ID={op_id} не найден.")
            return
        self.operator = row
        self.pulse_normal = int(row.get("pulse_normal") or 75)
        self.pulse_critical = int(row.get("pulse_threshold_critical") or 100)
        self.normal_spin.setValue(self.pulse_normal)
        self.critical_spin.setValue(self.pulse_critical)
        full_name = " ".join(x for x in [row.get("last_name"), row.get("first_name"), row.get("middle_name")] if x)
        self.auth_info.setText(
            f"Оператор определён по ID: {row['id']}\\nФИО: {full_name}\\nВозраст: {row.get('age')}\\n"
            f"Дата регистрации: {row.get('date')} {row.get('time')}\\n"
            f"Время запуска ПО: {row.get('software_start_time')}\\n"
            "Примечание: ID подтверждён по базе данных; автоматическая биометрическая сверка в прототипе не реализована."
        )
        photo = PHOTOS / f"ID_{row['id']}.jpg"
        if photo.exists(): self._show_photo(photo, self.auth_photo)
        else: self.auth_photo.setText("Фото для этого ID отсутствует")
        self.continue_btn.setEnabled(True)
        self._update_operator_ui()
        self._log(f"Авторизован оператор ID={row['id']}.")
        QMessageBox.information(self, "Авторизация", "Оператор найден. Можно перейти к анализу и управлению.")

    def save_analysis(self):
        try:
            normal = self.normal_spin.value()
            critical = self.critical_spin.value()
            if critical <= normal:
                QMessageBox.warning(self, "Проверка", "Критический порог должен быть выше нормы пульса.")
                return
            self.pulse_normal, self.pulse_critical = normal, critical
            if self.operator:
                update_operator(self.operator["id"], pulse_normal=str(normal), pulse_threshold_critical=str(critical))
                self.operator.update(pulse_normal=str(normal), pulse_threshold_critical=str(critical))
            self.analysis_operator.setText(f"Настройки сохранены: норма {normal}, критический порог {critical}.")
            self.signal_label.setText(f"Проверка сигнала: OK (симулятор) · Пульс: {self.pulse} · COM-порт: {self.port_combo.currentText()}")
            self._log(f"Сохранены настройки пульса: норма={normal}, порог={critical}.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))

    def refresh_ports(self):
        self.port_combo.clear()
        try:
            from serial.tools import list_ports
            ports = [p.device for p in list_ports.comports()]
        except Exception:
            ports = []
        self.port_combo.addItems(ports or ["Авто / не подключено"])
        self._log("Обновлён список COM-портов.")

    def _sim_pulse_changed(self, value):
        self.pulse = int(value)
        self.pulse_value.setText(f"{value} уд/мин")
        self._refresh_status()

    def _get_status(self):
        normal = self.pulse_normal
        critical = self.pulse_critical
        if self.pulse >= critical or self.pulse <= normal * 0.70:
            return "CRITICAL", "КРИТИЧНО", "#ff5c62"
        if self.pulse >= normal * 1.20 or self.pulse <= normal * 0.80:
            return "WARNING", "ВНИМАНИЕ", "#f5c542"
        return "NORMAL", "НОРМА", "#26c281"

    def _refresh_status(self):
        code, label, color = self._get_status()
        self.status_badge.setText(label)
        self.status_badge.setStyleSheet(f"background:{color}; color:#101820; border-radius:10px; padding:12px;")
        self.pulse_big.setText(str(self.pulse))
        self.pulse_big.setStyleSheet(f"color:{color};")
        messages = {
            "NORMAL": "Состояние оператора нормальное.",
            "WARNING": "Состояние выходит за пределы нормы. Внимание, оператор, остановите движение!",
            "CRITICAL": "Требуется немедленное вмешательство! Ваше состояние критично — немедленно остановитесь!"
        }
        self.control_message.setText(messages[code])
        if code != getattr(self, "_previous_status", None):
            if code != "NORMAL":
                QApplication.beep()
                self._log(f"Звуковое оповещение: {messages[code]}")
            self._previous_status = code
        if self.operator:
            update_operator(self.operator["id"], current_pulse=str(self.pulse), operator_status=code)
            self.operator.update(current_pulse=str(self.pulse), operator_status=code)
        self.server.update(self._remote_payload(code, label))
        self._update_operator_ui()

    def _remote_payload(self, code=None, label=None):
        code, label, _ = self._get_status()
        row = self.operator or {}
        photo = str((PHOTOS / f"ID_{row.get('id','')}.jpg").resolve()) if row else ""
        return {
            "id": row.get("id", ""), "last_name": row.get("last_name", ""),
            "first_name": row.get("first_name", ""), "middle_name": row.get("middle_name", ""),
            "age": row.get("age", ""), "pulse": self.pulse, "status": code,
            "status_label": label, "drive_duration": self._format_duration(self.drive_seconds),
            "photo_path": photo, "updated_at": now_text()
        }

    def _update_operator_ui(self):
        row = self.operator or {}
        if row:
            full_name = " ".join(x for x in [row.get("last_name"), row.get("first_name"), row.get("middle_name")] if x)
            self.operator_summary.setText(f"Оператор: {full_name} · ID {row.get('id')} · возраст {row.get('age')} лет")
            self.analysis_operator.setText(f"Текущий оператор: {full_name} · ID {row.get('id')}")
        self.server.update(self._remote_payload())

    def _toggle_drive(self, checked):
        self.start_drive_btn.setText("Остановить отсчёт времени в пути" if checked else "Начать отсчёт времени в пути")
        self._log("Отсчёт времени в пути запущен." if checked else "Отсчёт времени в пути остановлен.")

    def _format_duration(self, seconds):
        h = seconds // 3600; m = (seconds % 3600) // 60; s = seconds % 60
        return f"{h:02d}:{m:02d}:{s:02d}"

    def _tick(self):
        self.clock_label.setText(now_text("%d.%m.%Y %H:%M:%S"))
        if self.start_drive_btn.isChecked():
            self.drive_seconds += 1
        duration = self._format_duration(self.drive_seconds)
        self.drive_label.setText("Время в пути: " + duration)
        remaining = max(0, 9 * 3600 - self.drive_seconds)
        self.remaining_label.setText("Осталось: " + self._format_duration(remaining))
        if self.operator:
            update_operator(self.operator["id"], drive_duration=duration, current_pulse=str(self.pulse), operator_status=self._get_status()[0])
        self.server.update(self._remote_payload())

    def stop_program(self):
        self.start_drive_btn.setChecked(False)
        self.tabs.setCurrentIndex(0)
        self._log("Выполнен переход к начальной форме.")
        QMessageBox.information(self, "Программа", "Мониторинг остановлен. Вы вернулись к стартовому разделу.")

    def closeEvent(self, event):
        self.server.stop()
        event.accept()

def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
