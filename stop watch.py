import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QLabel, QPushButton, QFrame, QGraphicsDropShadowEffect
)
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QColor


class StopWatch(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stopwatch")
        self.setFixedSize(550, 400)

        self.time = QTime(0, 0, 0, 0)
        self.timer = QTimer()
        self.timer.setInterval(10)

        self.setup_ui()

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def setup_ui(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #0f172a;
                color: white;
                font-family: Arial;
            }
        """)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(35, 30, 35, 30)
        main_layout.setSpacing(25)

        title = QLabel("STOPWATCH")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: #94a3b8;
                letter-spacing: 3px;
            }
        """)

        main_layout.addWidget(title)

        self.timer_card = QFrame()
        self.timer_card.setStyleSheet("""
            QFrame {
                background-color: #1e293b;
                border-radius: 25px;
            }
        """)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setOffset(0, 8)
        shadow.setColor(QColor(0, 0, 0, 120))
        self.timer_card.setGraphicsEffect(shadow)

        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(20, 35, 20, 35)

        self.time_label = QLabel("00:00:00.00")
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("""
            QLabel {
                font-size: 55px;
                font-weight: bold;
                color: #f8fafc;
            }
        """)

        card_layout.addWidget(self.time_label)
        self.timer_card.setLayout(card_layout)

        main_layout.addWidget(self.timer_card)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(15)

        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        self.reset_button = QPushButton("Reset")

        for button in [
            self.start_button,
            self.stop_button,
            self.reset_button
        ]:
            button.setFixedHeight(60)

        self.start_button.setStyleSheet("""
            QPushButton {
                background-color: #22c55e;
                color: white;
                border: none;
                border-radius: 15px;
                font-size: 18px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #4ade80;
            }

            QPushButton:pressed {
                background-color: #16a34a;
            }
        """)

        self.stop_button.setStyleSheet("""
            QPushButton {
                background-color: #ef4444;
                color: white;
                border: none;
                border-radius: 15px;
                font-size: 18px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #f87171;
            }

            QPushButton:pressed {
                background-color: #dc2626;
            }
        """)

        self.reset_button.setStyleSheet("""
            QPushButton {
                background-color: #334155;
                color: white;
                border: none;
                border-radius: 15px;
                font-size: 18px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #475569;
            }

            QPushButton:pressed {
                background-color: #1e293b;
            }
        """)

        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.reset_button)

        main_layout.addLayout(button_layout)

        footer = QLabel("Press Start to begin")
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("""
            QLabel {
                font-size: 13px;
                color: #64748b;
            }
        """)

        main_layout.addWidget(footer)

        self.setLayout(main_layout)

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10

        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))


app = QApplication(sys.argv)

stopwatch = StopWatch()
stopwatch.show()

sys.exit(app.exec_())
