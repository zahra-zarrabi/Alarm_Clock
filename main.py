# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader

import time
# from threading import Thread
from PySide6.QtCore import QThread

from Timer import my_Time
from Alarm import My_Alarm
from functools import partial

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
        self.ui.btn_stopwatch_pause.clicked.connect(self.my_pausestopwatch)
        self.ui.btn_stopwatch_stop.clicked.connect(self.my_stopstopwatch)

        self.ui.btn_timer_start.clicked.connect(self.my_starttimer)
        self.ui.btn_timer_pause.clicked.connect(self.my_pausetimer)
        self.ui.btn_timer_stop.clicked.connect(self.my_stoptimer)
        self.my_time = my_Time(self.ui)

        self.ui.rb_on.clicked.connect(self.my_onalarm)
        self.alarm=My_Alarm(self.ui)

        self.timer = My_Stopwatch()

    def my_stopstopwatch(self):
        self.timer.terminate()
        self.timer.reset()
        self.ui.lbl_stopwatch.setText("00:00:00")

    def my_pausestopwatch(self):
        self.timer.terminate()

    def my_startstopwatch(self):
        self.timer.start()


# timer
    def my_stoptimer(self):
        self.my_time.terminate()
        self.my_time.reset()
        self.ui.lbl_stopwatch.setText("02:59:59")

    def my_pausetimer(self):
        self.my_time.terminate()

    def my_starttimer(self):
        print('hi')
        self.my_time.start()

#Alarm
    def my_onalarm(self):
        print("datetime.now()")
        self.alarm.start()

if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    # window.show()
    sys.exit(app.exec_())
