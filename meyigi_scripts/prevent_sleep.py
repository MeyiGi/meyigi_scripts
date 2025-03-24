import pyautogui
import time

def prevent_sleep():
    while True:
        pyautogui.press("shift")
        time.sleep(10, 30)