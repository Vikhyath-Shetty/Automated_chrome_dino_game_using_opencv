import cv2 as cv
import time
import subprocess
from vision import detect_obstacles
import pyautogui as py


def run_bot() -> None:
    """Main loop for the Dino game bot."""
    while True:
        game_region, cactus, pterodactyl = detect_obstacles()
        if cactus:
            py.press("space")
            time.sleep(0.1)
            py.press("down")
        if pterodactyl:
            py.keyDown("down")
            time.sleep(0.2)
            py.keyUp("down")

    


if __name__ == '__main__':
    subprocess.run(["wmctrl", "-a", "Google Chrome"])
    py.press("f5")
    time.sleep(3)
    py.press("space")
    run_bot()
