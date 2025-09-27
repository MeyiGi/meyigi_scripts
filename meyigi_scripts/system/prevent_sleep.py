import pyautogui
import time
import random

def prevent_sleep():
    """Function to prevent the computer from falling asleep by moving the mouse slightly"""
    while True:
        # Get current mouse position
        x, y = pyautogui.position()

        # Move mouse by only 1 pixel in a random direction (including staying in place)
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        pyautogui.moveTo(x + dx, y + dy, duration=0.2)

        # Wait a random interval
        time.sleep(random.randint(10, 30))