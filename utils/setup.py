import subprocess
import platform
from .import config
import time
import pyautogui as py


def notify(title: str, message: str) -> None:
    """Cross-platform notification function"""
    system = platform.system()
    if system == "Linux":
        subprocess.run(["notify-send", title, message])
    elif system == "Windows":
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast(title, message, duration=3, threaded=True)
        except ImportError:
            print(f"{title}: {message}")
    else:
        print(f"{title}: {message}")


def kill_bot(key) -> bool | None:
    """Keypress listener function to kill the bot on 'q' keypress"""
    try:
        if getattr(key, "char", None) == 'q':
            print("The Dino Bot has been Killed!")
            notify("Dino Bot", "Bot has been killed!")
            config.KILL_BOT = True
            return False
    except AttributeError:
        pass


def focus_chrome() -> None:
    """Cross-platform function to focus Chrome window"""
    system = platform.system()
    if system == "Linux":
        subprocess.run(["wmctrl", "-a", "Google Chrome"])
    elif system == "Windows":
        chrome_windows = py.getWindowsWithTitle("Google Chrome")
        if chrome_windows:
            chrome_windows[0].activate()
            chrome_windows[0].maximize()
    py.press("f5")
    time.sleep(2)
    py.press("space")
  