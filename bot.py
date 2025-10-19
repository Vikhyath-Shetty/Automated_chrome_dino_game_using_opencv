import cv2 as cv
import numpy as np
import time
import subprocess
from vision import detect_obstacles
import pyautogui as py
from config import region


def create_window() -> None:
    cv.namedWindow("Chrome_Dino_Bot", cv.WINDOW_NORMAL)
    cv.setWindowProperty("Chrome_Dino_Bot", cv.WND_PROP_TOPMOST, 1)
    cv.imshow("Chrome_Dino_Bot", np.zeros(
        (region["height"], region["width"], 3), dtype=np.uint8))
    subprocess.run(["wmctrl","-r","Chrome_Dino_Bot","-b","add,below"])




def run_bot():
    while True:
        game_region, cactus, pterodactyl = detect_obstacles()
        if cactus:
            py.press("space")
        if pterodactyl:
            py.keyDown("down")
            time.sleep(0.2)
            py.keyUp("down")

        cv.imshow("Chrome_Dino_Bot", game_region)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    create_window()
    subprocess.run(["wmctrl", "-a", "Google Chrome"])
    py.press("f5")
    time.sleep(3)
    py.press("space")
    run_bot()
