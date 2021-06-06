from PySide6.QtCore import QThread
from datetime import datetime

# import winsound
from playsound import playsound
import sounddevice as sd
import soundfile as sf
# from PySide6.QtGui import QSound

class My_Alarm(QThread):
    def __init__(self, ui):
        QThread.__init__(self)
        self.ui=ui

        print(datetime.now())

        # a= '{0:%H:%M}'.format(datetime.now())

    def run(self):
        self.hour = self.ui.lineEdit_hour.text()
        self.minute = self.ui.lineEdit_minute.text()

        if self.hour == str('{0:%H}'.format(datetime.now())) and self.minute == str('{0:%M}'.format(datetime.now())):
            print('zah')
            data, fs = sf.read('agua.wav')
            sd.play(data, fs)
            status = sd.wait()

        else:
            print('no')