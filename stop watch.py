import sys
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout,QLabel,QPushButton
from PyQt5.QtCore import Qt,QTime,QTimer

class Stop_watch(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(1000,300,300,300)
        self.setWindowTitle("STOP WATCH")

        self.time=QTime(0,0,0,0)
        self.time_label=QLabel("00:00:00.00",self)
        self.timer=QTimer()
        self.start_button=QPushButton("Start",self)
        self.stop_button=QPushButton("Stop",self)
        self.reset_button=QPushButton("Reset",self)

        vbox=QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter )

        hbox=QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)

        self.setStyleSheet("""
                           QPushButton,QLabel{
                           border-radius:30px;
                           font-family:Arial;
                           }
                            QPushButton{
                           font-size:50px; 
                           background-color:red; 

                           }
                           QLabel{
                           font-size:110px;
                           background-color:Blue; 
                           }""")


        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time=QTime(0,0,0,0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self,time):
        hrs=time.hour()
        minutes=time.minute()
        seconds=time.second()
        mmseconds=time.msec()//10
        return f"{hrs:02}:{minutes:02}:{seconds:02}.{mmseconds:02}" 

    def update_display(self)   :
        self.time=self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))    


app=QApplication(sys.argv)
stopwatch=Stop_watch()
stopwatch.show()        
sys.exit(app.exec_())