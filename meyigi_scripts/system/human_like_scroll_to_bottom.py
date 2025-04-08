import time
import random
import pyautogui

def human_like_scroll_bottom_hits(hits=None, countdown=3):
    """
    Smoothly scrolls down a page either a specific number of times
    when reaching the bottom, or infinitely if hits is None.
    """

    # Countdown before start
    for i in range(countdown, 0, -1):
        print(f"Scrolling starts in {i}...")
        time.sleep(1)

    print("🔽 Starting to scroll down...")

    bottom_hit_count = 0

    while True:
        # Scroll down by a random amount
        scroll_amount = random.randint(-200, -100)
        pyautogui.scroll(scroll_amount)

        # Small random delay to simulate human-like behavior
        time.sleep(random.uniform(0.2, 0.6))

        # Screenshot the bottom region of the screen to detect changes
        screen_before = pyautogui.screenshot(region=(100, 800, 800, 50))
        time.sleep(0.5)
        screen_after = pyautogui.screenshot(region=(100, 800, 800, 50))

        # Compare pixels to see if content changed
        if list(screen_before.getdata()) == list(screen_after.getdata()):
            bottom_hit_count += 1
            print(f"🔁 Bottom hits: {bottom_hit_count}" + (f"/{hits}" if hits else " (infinite)"))
        else:
            print("🔄 New content loaded, continuing...")

        # Exit if we reached the defined number of bottom hits
        if hits is not None and bottom_hit_count >= hits:
            print("✅ Done. Reached bottom the desired number of times.")
            break

if __name__ == "__main__":
    human_like_scroll_bottom_hits()  # You can pass hits=200 if needed
