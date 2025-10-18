import pyautogui
import time

print("Move your mouse to the TOP-LEFT corner of the Dino game and wait...")

try:
    while True:
        x, y = pyautogui.position()
        print(f"Mouse at: ({x}, {y})", end="\r")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nDone")
