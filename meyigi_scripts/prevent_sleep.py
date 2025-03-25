import pyautogui
import time
import random

def prevent_sleep():
    while True:
        pyautogui.press("shift")
        time.sleep(random.randint(10, 30))