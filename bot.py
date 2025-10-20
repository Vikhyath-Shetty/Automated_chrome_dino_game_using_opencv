import time
from vision import detect_obstacles
import pyautogui as py
from pynput import keyboard
from utils.setup import kill_bot, notify, focus_chrome
from utils import config

# For windows install win10toast module for notifications
# uv add wind10toast


def run_bot() -> None:
    """Main loop for the Dino game bot."""
    print("Press 'q' to kill the bot!")
    while not config.KILL_BOT:
        _, cactus, pterodactyl = detect_obstacles()
        if cactus:
            py.press("space")
            time.sleep(0.1)
            py.press("down")
        if pterodactyl:
            py.keyDown("down")
            time.sleep(0.2)
            py.keyUp("down")


if __name__ == '__main__':
    focus_chrome()
    notify("Dino Bot", "The Dino Bot has started!\nPress 'q' to kill the bot.")
    # Runs a seperate thread that listens for keypress(key='q')
    listener = keyboard.Listener(on_press=kill_bot)  # type: ignore
    listener.start()
    run_bot()
