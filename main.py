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


chrome = ['chrome.exe']
jetbrains = ['pycharm64.exe','clion64.exe','webstorm64.exe','rider64.exe']
vs = ['devenv.exe']
explorer = ['explorer.exe']
notepadpp = ['notepad++.exe']
cmd = ['cmd.exe']
vlc = ['vlc.exe']

def app():
    try:
        pid = ctypes.wintypes.DWORD()
        ctypes.windll.user32.GetWindowThreadProcessId(ctypes.windll.user32.GetForegroundWindow(), ctypes.byref(pid))
        return psutil.Process(pid.value).name()
    except:return ""

def kill_current():
    pid = ctypes.wintypes.DWORD()
    ctypes.windll.user32.GetWindowThreadProcessId(ctypes.windll.user32.GetForegroundWindow(), ctypes.byref(pid))
    psutil.Process(pid.value).terminate()

def middle_mouse():
    mouse.press(Button.middle)
    mouse.release(Button.middle)
def enter():
    controller.press(Key.enter)
    controller.release(Key.enter)
def alt_f4():
    controller.press(Key.alt)
    controller.press(Key.f4)
    controller.release(Key.f4)
    controller.release(Key.alt)
def alt_left():
    controller.press(Key.alt)
    controller.press(Key.left)
    controller.release(Key.left)
    controller.release(Key.alt)

def alt_right():
    controller.press(Key.alt)
    controller.press(Key.right)
    controller.release(Key.right)
    controller.release(Key.alt)

def left():
    controller.press(Key.left)
    controller.release(Key.left)

def right():
    controller.press(Key.right)
    controller.release(Key.right)

def alt_up():
    controller.press(Key.alt)
    controller.press(Key.up)
    controller.release(Key.up)
    controller.release(Key.alt)

def ctrl_tab():
    controller.press(Key.ctrl)
    controller.press(Key.tab)
    controller.release(Key.tab)
    controller.release(Key.ctrl)

def ctrl_shift_tab():
    controller.press(Key.ctrl)
    controller.press(Key.shift)
    controller.press(Key.tab)
    controller.release(Key.tab)
    controller.release(Key.shift)
    controller.release(Key.ctrl)
def ctrl_pgdown():
    controller.press(Key.ctrl)
    controller.press(Key.page_down)
    controller.release(Key.page_down)
    controller.release(Key.ctrl)

def ctrl_pgup():
    controller.press(Key.ctrl)
    controller.press(Key.page_up)
    controller.release(Key.page_up)
    controller.release(Key.ctrl)

def ctrl_t():
    controller.press(Key.ctrl)
    controller.press('t')
    controller.release('t')
    controller.release(Key.ctrl)

def ctrl_f4():
    controller.press(Key.ctrl)
    controller.press(Key.f4)
    controller.release(Key.f4)
    controller.release(Key.ctrl)
    
def ctrl_ast():
    controller.press(Key.ctrl)
    controller.press('*')
    controller.release('*')
    controller.release(Key.ctrl)

def ctrl_dev():
    controller.press(Key.ctrl)
    controller.press('/')
    controller.release('/')
    controller.release(Key.ctrl)

def up_4():
    p = app()
    time.sleep(.01)
    if p in jetbrains + chrome: ctrl_t()
    elif p in explorer: alt_up()
    print(p,sys._getframe(0).f_code.co_name)
def down_4():
    p = app()
    time.sleep(.01)
    if p in jetbrains + chrome + notepadpp: ctrl_f4()
    elif p in cmd: kill_current()
    elif p in explorer or True:alt_f4()
    print(p,sys._getframe(0).f_code.co_name)
def left_4():
    p = app()
    time.sleep(.01)
    if p in jetbrains + chrome + notepadpp + vs: ctrl_pgdown()
    elif p in explorer:alt_right()
    elif p in vlc:right()
    else:ctrl_tab()
    print(p,sys._getframe(0).f_code.co_name)
def right_4():
    p = app()
    time.sleep(.01)
    if p in jetbrains + chrome + notepadpp + vs: ctrl_pgup()
    elif p in explorer:alt_left()
    elif p in vlc:left()
    else:ctrl_shift_tab()
    print(p,sys._getframe(0).f_code.co_name)
def tap_4():
    p = app()
    time.sleep(.01)
    if p in chrome+jetbrains: middle_mouse()
    else: enter()
    print(p,sys._getframe(0).f_code.co_name)

def f1():threading.Thread(target=up_4).start()
def f2():threading.Thread(target=down_4).start()
def f3():threading.Thread(target=left_4).start()
def f5():threading.Thread(target=right_4).start()
def f6():threading.Thread(target=tap_4).start()


with keyboard.GlobalHotKeys({
        '<ctrl>+<shift>+<f1>': f1,
        '<ctrl>+<shift>+<f2>': f2,
        '<ctrl>+<shift>+<f3>': f3,
        '<ctrl>+<shift>+<f5>': f5,
        '<ctrl>+<shift>+<f6>': f6,
}) as h:
    h.join()