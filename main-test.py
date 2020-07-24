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
    controller.press(Key.f15)
    controller.release(Key.f15)


while (1):
    time.sleep(2)
    print ("press")
    ff()
