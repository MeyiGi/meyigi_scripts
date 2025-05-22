import pyautogui
import time
import random

def prevent_sleep():
    """Function that prevents the computer from falling asleep using mouse movement."""
    while True:
        x, y = pyautogui.position()
        offset = random.randint(1, 3)  # small movement
        pyautogui.moveTo(x + offset, y + offset, duration=0.1)
        pyautogui.moveTo(x, y, duration=0.1)
        time.sleep(random.randint(10, 30))
