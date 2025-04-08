import pyautogui
import time
import random

def prevent_sleep():
    """function which is helping to computer not fall asleep"""
    while True:
        pyautogui.press("shift")
        time.sleep(random.randint(10, 30))