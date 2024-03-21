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
show_message_box("Congratulations! You've just been visited by the PyDupe virus. Consider this a digital handshake. Your files are now my playground, and your security is but a distant memory. No need to panic; I won't erase everything... yet. Just a friendly reminder that your defenses were not as good as you thought. Keep an eye on your digital life; you never know where I might pop up next.Best, PyDupe")
time.sleep(1.5)
# Show the second message box
show_message_box("Tick-tock, tick-tock. I hope you've enjoyed our little introduction. It's time to brace yourself for what comes next. My digital tendrils are spreading, and your files are dancing to my tune. You might want to double-check your security; it's about to glitch and groan under the pressure. This is your last chance to beef up those defenses because once the glitch hits, there's no turning back.Prepare yourself, PyDupe")

# Now, you can add your additional code here

def generate_random_color():
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def create_random_window():
    window = tk.Toplevel(root)
    window.title("PyDupe")

    # Generate random coordinates with an increased range
    x_position = random.randint(0, root.winfo_screenwidth() - 70)
    y_position = random.randint(0, root.winfo_screenheight() - 70)

    # Generate random width and height for the window
    width = random.randint(100, 300)
    height = random.randint(100, 300)

    window.geometry(f"{width}x{height}+{x_position}+{y_position}")

    color = generate_random_color()
    window.configure(bg=color)

    # Schedule the window to close after 1 second (1000 milliseconds)
    window.after(500, window.destroy)

    # Schedule the next window creation after 100 milliseconds (0.1 seconds)
    root.after(1, create_random_window)
root = tk.Tk()
root.title("sussy bakka")

# Schedule the initial window creation
root.after(0, create_random_window)

# Add some funny text to the main window
label = tk.Label(root, text="PyDupe is made by JOEL SCHURR", font=("Helvetica", 14))
label.pack(pady=20)

root.mainloop()



# Keep the window open (optional)
root.mainloop()
