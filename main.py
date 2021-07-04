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


chrome = ['chrome.exe','firefox.exe']
terminal = ['WindowsTerminal.exe']
jetbrains = ['pycharm64.exe','clion64.exe','webstorm64.exe','rider64.exe','pycharm.exe','clion.exe','webstorm.exe','rider.exe', 'studio.exe','studio64.exe', 'idea.exe', 'idea64.exe']
vs = ['devenv.exe']
explorer = ['explorer.exe']
notepadpp = ['notepad++.exe', 'notepad.exe']
cmd = ['cmd.exe']
taskmgr = ['Taskmgr.exe']
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

def f14():
    controller.press(Key.f14)
    controller.release(Key.f14)
def f13():
    controller.press(Key.f13)
    controller.release(Key.f13)
def f15():
    controller.press(Key.f15)
    controller.release(Key.f15)
def f16():
    controller.press(Key.f16)
    controller.release(Key.f16)

def up_4():
    p = app()
    print(p)
    time.sleep(.01)
    if p in terminal+jetbrains + chrome + notepadpp: ctrl_t()
    elif p in explorer: alt_up()
    print(p,sys._getframe(0).f_code.co_name)
def down_4():
    print("down_4")
    p = app()
    print(p)
    time.sleep(.01)
    if p in terminal+jetbrains + chrome : ctrl_f4()
    elif p in cmd + taskmgr: kill_current()
    elif p in vs:f15()
    elif p in explorer or True:alt_f4()
    print(p,sys._getframe(0).f_code.co_name)
def left_4():
    p = app()
    print(p)
    time.sleep(.01)
    if p in terminal+jetbrains + chrome + notepadpp: ctrl_pgdown()
    elif p in explorer:alt_right()
    elif p in vlc:right()
    elif p in vs:f14()
    else:ctrl_tab()
    print(p,sys._getframe(0).f_code.co_name)
def right_4():
    p = app()
    print(p)
    time.sleep(.01)
    if p in terminal+jetbrains + chrome + notepadpp : ctrl_pgup()
    elif p in explorer:alt_left()
    elif p in vlc:left()
    elif p in vs:f13()
    else:ctrl_shift_tab()
    print(p,sys._getframe(0).f_code.co_name)
def tap_4():
    print("tap_4")
    p = app()
    print(p)
    time.sleep(.01)
    if p in chrome+jetbrains+vs: middle_mouse()
    else: enter()
    print(p,sys._getframe(0).f_code.co_name)

def up_4_c():threading.Thread(target=up_4).start()
def down_4_c():threading.Thread(target=down_4).start()
def left_4_c():threading.Thread(target=left_4).start()
def right_4_c():threading.Thread(target=right_4).start()
def tap_4_c():threading.Thread(target=tap_4).start()


with keyboard.GlobalHotKeys({
        '<f6>': up_4_c,
        '<f3>': down_4_c,
        '<pause>': left_4_c,
        '<scroll_lock>': right_4_c,
        # '<f8>': tap_4_c,
}) as h:
    h.join()