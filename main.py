# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader

import time
# from threading import Thread
from PySide6.QtCore import QThread,QSize
from PySide6.QtWidgets import *

from Timer import my_Time
from Alarm import My_Alarm
from functools import partial
from PySide6.QtGui import QPixmap,QIcon

class My_Stopwatch(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.hour=00
        self.minute=00
        self.second=00
    def reset(self):
        self.hour = 0
        self.minute = 0
        self.second = 0
        window.ui.btn_stopwatch_start.setStyleSheet('color:green')
        window.ui.btn_stopwatch_start.setText("start")

    def increase(self):
        self.second +=1
        if self.second >=60:
            self.second=0
            self.minute+=1
        if self.minute >=60:
            self.minute=0
            self.hour +=1

    def run(self):
        while True:
            self.increase()
            window.ui.lbl_stopwatch.setText(f"{self.hour}:{self.minute}:{self.second}")
            time.sleep(1)

class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('dialog.ui')
        self.ui.show()

        self.ui.btn_stopwatch_start.clicked.connect(self.my_startstopwatch)
        # self.ui.btn_stopwatch_pause.clicked.connect(self.my_pausestopwatch)
        self.ui.btn_stopwatch_stop.clicked.connect(self.my_stopstopwatch)

        self.ui.btn_timer_start.clicked.connect(self.my_starttimer)
        self.ui.btn_timer_pause.clicked.connect(self.my_pausetimer)
        self.ui.btn_timer_stop.clicked.connect(self.my_stoptimer)
        self.my_time = my_Time(self.ui)
        self.running_timer=False

        self.ui.rb_on.clicked.connect(self.my_onalarm)
        self.alarm=My_Alarm(self.ui)

        self.timer = My_Stopwatch()

        self.ui.btn_record.clicked.connect(self.my_save)
        self.row=1
        self.running_stopwatch=False
        # self.ui.btn_timer_start.setStyleSheet('background-color:red; border-radius:15px; border:8px solid red')
        # image icon
        # pixmap=QPixmap("images.jpeg")
        # but=QIcon(pixmap)
        # self.ui.btn_timer_start.setIcon(but)
        # self.ui.btn_timer_start.setIconSize(QSize(100,10))

# StopWatch
    def my_stopstopwatch(self):
        self.timer.terminate()
        self.timer.reset()
        self.ui.lbl_stopwatch.setText("00:00:00")

    # def my_pausestopwatch(self):
    #     self.timer.terminate()

    def my_startstopwatch(self):
        if not self.running_stopwatch:
            self.timer.start()
            self.running_stopwatch=True
            self.ui.btn_stopwatch_start.setStyleSheet('color:red')
            self.ui.btn_stopwatch_start.setText("Pause")
        else:
            self.timer.terminate()
            self.running = False
            self.ui.btn_stopwatch_start.setStyleSheet('color:green')
            self.ui.btn_stopwatch_start.setText("Resume")

    def my_save(self):
        x=window.ui.lbl_stopwatch.text()

        label_1 = QLabel()
        label_1.setText(str(self.row))
        self.ui.hl_r.addWidget(label_1, self.row, 0)

        label = QLabel()
        label.setText(x)
        self.ui.hl_r.addWidget(label,self.row,1)

        self.row += 1


# timer
    def my_stoptimer(self):
        self.my_time.terminate()
        self.ui.le_timer_hour.setText("00")
        self.ui.le_timer_minute.setText("00")
        self.ui.le_timer_second.setText("00")

    def my_pausetimer(self):
        self.my_time.terminate()

    def my_starttimer(self):
        self.my_time.start()

        # if not self.running_timer:
        #     print('d')
        #     self.my_time.start()
        #     self.running_timer=True
        #     self.ui.btn_timer_start.setStyleSheet('color:red')
        #     self.ui.btn_timer_start.setText("Pause")
        # else:
        #     self.my_time.terminate()
        #     self.running_timer = False
        #     self.ui.btn_timer_start.setStyleSheet('color:green')
        #     self.ui.btn_timer_start.setText("Resume")


#Alarm
    def my_onalarm(self):
        print("datetime.now()")
        self.alarm.start()
        self.my_save_alarm()
    def my_save_alarm(self):
        h=window.ui.lineEdit_hour.text()
        m=window.ui.lineEdit_minute.text()

        label_1 = QLabel()
        label_1.setText(str(self.row))
        self.ui.gridLayout.addWidget(label_1, self.row, 0)

        label = QLabel()
        label.setText(h+":"+m)
        self.ui.gridLayout.addWidget(label,self.row,1)

        self.row += 1


if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    # window.show()
    sys.exit(app.exec_())
