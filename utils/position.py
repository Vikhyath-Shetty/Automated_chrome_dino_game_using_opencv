"""uv run position.py to and hower 
mouse to get coordinates of the 
respective point"""

import pyautogui
import time

print("Move your mouse to the TOP-LEFT corner of the Dino game and wait...")


def print_mouse_coordinates() -> None:
    """This is a function used for development purpose. 
    This gets mouse coordinates for configuraton of
    dino motion 
    """
    try:
        while True:
            x, y = pyautogui.position()
            print(f"Mouse at: ({x}, {y})", end="\r")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nDone")


if __name__ == "__main__":
    print_mouse_coordinates()
