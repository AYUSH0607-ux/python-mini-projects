import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QHBoxLayout,QVBoxLayout
from PyQt5.QtCore import Qt,QTime,QTimer

class Digital_clock(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,500,400,200)
        self.setWindowTitle("DIGITAL CLOCK")
        self.setStyleSheet("background-color:Black;")

        self.time_label=QLabel("12:00:00",self)
        self.timer=QTimer(self)
        self.time_label.setStyleSheet("font-size:100px;"
                                      "color:white;")

        hbox=QHBoxLayout()
        hbox.addWidget(self.time_label)
        self.setLayout(hbox)
        self.time_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time=QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)



app=QApplication(sys.argv)
clock=Digital_clock()
clock.show()
sys.exit(app.exec_()) 