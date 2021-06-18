from pynput import keyboard
from pynput.keyboard import Key, Controller
import threading
import psutil
import keyboard as k
import time
import sys
import ctypes
from pynput.mouse import Button, Controller as Mouse
controller = Controller()
mouse = Mouse()

def ff():
    controller.press(Key.f13)
    controller.release(Key.f13)


def alt_f14():
    # controller.press(Key.)
    controller.press(Key.f16)
    controller.release(Key.f16)
    # controller.release(Key.cmd)

while (1):
    time.sleep(2)
    print ("press")
    alt_f14()
