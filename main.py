import time
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

# Tworzenie okna głównego
root = tk.Tk()
root.title("Proste GUI")

# Tworzenie etykiety
label = tk.Label(root, text="Witaj w prostym GUI!")
label.pack(pady=20)

# Tworzenie etykiety statusu
status_label = tk.Label(root, text="Funkcja gotowa", fg="black")
status_label.pack(pady=10)

custom_label = tk.Label(root, text="Klawisz M start AutoHeala", font=("Arial", 12))
custom_label.pack(pady=10)
custom_label = tk.Label(root, text="Klawisz J stop AutoHeala", font=("Arial", 12))
custom_label.pack(pady=10)
custom_label = tk.Label(root, text="Klawisz ESC wyłącza program", font=("Arial", 12))
custom_label.pack(pady=10)

keyboard.add_hotkey('m', start_press_key)  # Uruchomienie funkcji start_press_key() po naciśnięciu klawisza "M"
keyboard.add_hotkey('j', stop_key)  # Wywołanie funkcji stop_key() po naciśnięciu klawisza "J"

root.bind('<Escape>', on_closing)  # Wywołanie funkcji on_closing() przy naciśnięciu klawisza Esc

root.mainloop()
