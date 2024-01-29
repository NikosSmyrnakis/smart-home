import os
import sys
from PyP100 import PyP100
import os
os.system("/Users/nikossmyrnakis/Desktop/python_projects/smart\ home/adb connect 192.168.2.31")


#p100 = PyP100.P100("192.168.2.42", "nick8smirn@gmail.com", "Papadopoulos1!")
#p100.handshake()
#p100.login()
sys.path.append(os.path.abspath('.'))
k2 = 0
from piclap import *

def tv():
    os.system("/Users/nikossmyrnakis/Desktop/python_projects/smart\ home/adb shell input keyevent KEYCODE_POWER")

def lamp():
    global k2
    k2=k2+1
    if k2==1:
        pass
        #p100.turnOn()
    if k2%2:
        pass
        #p100.turnOff()
    else:
        pass
        #p100.turnOn()


class Config(Settings):
    '''Describes custom configurations and action methods to be executed based
    on the number of claps detected.
    '''

    def __init__(self):
        super().__init__()
        self.chunk_size = 150      # Reduce as power of 2 if pyaudio overflow
        self.wait = 0.5           # Adjust wait between claps
        self.method.value = 28000   # Threshold value adjustment

    def on1Claps(self):
        lamp()
    def on2Claps(self):
        lamp()

    def on3Claps(self):
        lamp()
    def on4Claps(self):
        tv()


def main():
    config = Config()
    listener = Listener(config=config, calibrate=False)
    listener.start()


if __name__ == '__main__':
    main()