import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout,
    QFrame, QGraphicsDropShadowEffect
)
from PyQt5.QtCore import Qt, QTime, QTimer, QDate
from PyQt5.QtGui import QColor


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Digital Clock")
        self.setFixedSize(600, 400)

        self.setup_ui()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def setup_ui(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #020617;
                color: white;
                font-family: Arial;
            }
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(40, 35, 40, 35)
        layout.setSpacing(25)

        title = QLabel("DIGITAL CLOCK")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                font-size: 22px;
                font-weight: bold;
                color: #64748b;
                letter-spacing: 5px;
            }
        """)

        layout.addWidget(title)

        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background-color: #0f172a;
                border: 1px solid #1e293b;
                border-radius: 30px;
            }
        """)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(40)
        shadow.setOffset(0, 12)
        shadow.setColor(QColor(0, 0, 0, 180))
        card.setGraphicsEffect(shadow)

        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(20, 35, 20, 35)
        card_layout.setSpacing(25)

        self.time_label = QLabel()
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("""
            QLabel {
                font-size: 70px;
                font-weight: bold;
                color: #38bdf8;
            }
        """)

        self.date_label = QLabel()
        self.date_label.setAlignment(Qt.AlignCenter)
        self.date_label.setStyleSheet("""
            QLabel {
                font-size: 18px;
                color: #94a3b8;
            }
        """)

        card_layout.addWidget(self.time_label)
        card_layout.addWidget(self.date_label)

        card.setLayout(card_layout)

        layout.addWidget(card)

        status = QLabel("●  LIVE")
        status.setAlignment(Qt.AlignCenter)
        status.setStyleSheet("""
            QLabel {
                color: #22c55e;
                font-size: 14px;
                font-weight: bold;
            }
        """)

        layout.addWidget(status)

        self.setLayout(layout)

    def update_time(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()

        self.time_label.setText(
            current_time.toString("hh:mm:ss AP")
        )

        self.date_label.setText(
            current_date.toString("dddd, dd MMMM yyyy")
        )


app = QApplication(sys.argv)

clock = DigitalClock()
clock.show()

sys.exit(app.exec_())
