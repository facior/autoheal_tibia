import time
import webbrowser

import keyboard
import threading
import tkinter as tk

running = False

def press_key():
    global running
    running = True
    while running:
        keyboard.press('1')
        time.sleep(0.5)
        keyboard.release('1')

def stop_key():
    global running
    running = False
    status_label.config(text=" AutoHeal OFF", fg="red")

def start_press_key():
    global running
    if not running:
        running = True
        press_thread = threading.Thread(target=press_key)
        press_thread.start()
        status_label.config(text=" AutoHeal ON ", fg="green")

def on_closing(event=None):
    global running
    running = False
    root.destroy()

class HyperlinkLabel(tk.Label):
    def __init__(self, master, text, url, *args, **kwargs):
        super().__init__(master, text=text, fg="blue", cursor="hand2", *args, **kwargs)
        self.url = url
        self.bind("<Button-1>", self.open_link)

    def open_link(self, event):
        webbrowser.open(self.url)

root = tk.Tk()
root.title("Hello in Tibia AutoHeal Bot by facior")



label = tk.Label(root, text="Hello in Tibia AutoHeal Bot by facior")
label.pack(pady=20)

hyperlink_label = HyperlinkLabel(root, text="My other GitHub projects", url="https://www.github.com/facior")
hyperlink_label.pack(pady=20)


status_label = tk.Label(root, text="Program is ready", fg="black")
status_label.pack(pady=10)

custom_label = tk.Label(root, text="Press key M to start AutoHeal", font=("Arial", 12))
custom_label.pack(pady=10)
custom_label = tk.Label(root, text="Press key J to stop AutoHeal", font=("Arial", 12))
custom_label.pack(pady=10)
custom_label = tk.Label(root, text="Press key ESC to close program", font=("Arial", 12))
custom_label.pack(pady=10)

keyboard.add_hotkey('m', start_press_key)
keyboard.add_hotkey('j', stop_key)

root.bind('<Escape>', on_closing)

root.mainloop()
