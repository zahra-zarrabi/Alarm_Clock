from PySide6.QtCore import QThread
import time
import sounddevice as sd
import soundfile as sf

class my_Time(QThread):
    def __init__(self, ui):
        QThread.__init__(self)
        self.hour=2
        self.minute=59
        self.second=59
        self.ui = ui
    def reset(self):
        self.hour = 2
        self.minute = 59
        self.second = 59

    def reduce(self):
        self.second -= 1
        if self.second < 0:
            self.second = 59
            self.minute -= 1
        if self.minute < 0:
            self.minute = 59
            self.hour -= 1

    def run(self):
        while True:
            self.reduce()
            self.ui.lbl_timer.setText(f"{self.hour}:{self.minute}:{self.second}")
            time.sleep(1)
            if self.hour==0 and self.minute==0:
                data, fs = sf.read('agua.wav')
                sd.play(data, fs)
                status = sd.wait()
