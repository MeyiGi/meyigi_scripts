import pyautogui
import time
import random

def prevent_sleep():
    """Function to prevent the computer from falling asleep by moving the mouse slightly"""
    while True:
        # Get current mouse position
        x, y = pyautogui.position()

        # Move mouse a few pixels in a random direction
        dx = random.randint(-10, 10)
        dy = random.randint(-10, 10)
        pyautogui.moveTo(x + dx, y + dy, duration=0.2)

        # Wait a random interval
        time.sleep(random.randint(10, 30))