from PySide6.QtCore import QThread, Signal
import time
import sounddevice as sd
import soundfile as sf
from PySide6.QtWidgets import QMessageBox

class my_Time(QThread):
    mysignal_end=Signal()
    def __init__(self, ui):
        QThread.__init__(self)
        self.ui = ui


    def reset(self):
        self.hour = 0
        self.minute =0
        self.second = 4


    def reduce(self):
        # if self.hour != 0 or self.minute != 0 or self.second != 0:
        self.second -= 1
        if self.second < 0:
            self.second = 59
            self.minute -= 1

        if self.minute < 0:
            self.minute = 59
            self.hour -= 1
        #     return True
        # else:
        #     return False

    def run(self):
        self.hour = int(self.ui.le_timer_hour.text())
        self.minute = int(self.ui.le_timer_minute.text())
        self.second = int(self.ui.le_timer_second.text())
        while True:
            self.reduce()
            # self.ui.lbl_timer.setText(f"{self.hour}:{self.minute}:{self.second}")
            self.ui.le_timer_hour.setText(str(self.hour))
            self.ui.le_timer_minute.setText(str(self.minute))
            self.ui.le_timer_second.setText(str(self.second))
            time.sleep(1)
            if self.hour==0 and self.minute==0 and self.second==0:
                data, fs = sf.read('agua.wav')
                sd.play(data, fs)
                status = sd.wait()
                self.mysignal_end.emit()
                break



                # self.reset()
                # self.ui.le_timer_hour.setText("00")
                # self.ui.le_timer_hour.setText("00")
                # self.ui.le_timer_hour.setText("00")
                # print('ff')
