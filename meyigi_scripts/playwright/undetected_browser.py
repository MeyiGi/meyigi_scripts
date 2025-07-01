import os
import shutil
from uuid import uuid4

from playwright.sync_api import sync_playwright, Page, Download
from fake_useragent import UserAgent

from meyigi_scripts import BrowserProtocol

DOWNLOADS_DIR = os.path.join(os.getcwd(), "downloads")

class PlaywrightUndetected(BrowserProtocol):
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page: Page | None = None
        # Use BASE_PROFILE_DIR env var if set, otherwise current working directory
        base_dir = os.getenv("BASE_PROFILE_DIR", os.getcwd())
        self.profile_path = os.path.join(base_dir, f"profile_{uuid4().hex}")
        self.ua = UserAgent()

        os.makedirs(self.profile_path, exist_ok=True)
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)

    def start(self) -> Page:
        self.playwright = sync_playwright().start()

        random_ua = self._get_desktop_user_agent()

        self.browser = self.playwright.chromium.launch_persistent_context(
            user_data_dir=self.profile_path,
            headless=False,
            accept_downloads=True,
            viewport={'width': 1280, 'height': 800},
            locale="en-US",
            user_agent=random_ua,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-infobars",
                "--disable-web-security",
                "--start-maximized",
                "--disable-features=IsolateOrigins,site-per-process",
            ],
            bypass_csp=True,
        )
        self.browser.set_default_timeout(90_000)

        # Automatically clean up the profile directory when the browser context closes
        def _cleanup_profile(_: Download = None):
            if os.path.exists(self.profile_path):
                shutil.rmtree(self.profile_path, ignore_errors=True)
        self.browser.on("close", _cleanup_profile)

        self.page = self.browser.pages[0] if self.browser.pages else self.browser.new_page()

        self.page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
            window.chrome = { runtime: {} };
            Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
            Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5] });
        """
        )

        self.page.on("download", self._handle_download)

        print(f"[✓] Launched undetected browser with UA: {random_ua}")
        return self.page

    def _get_desktop_user_agent(self) -> str:
        for _ in range(5):
            ua = self.ua.chrome
            if all(x not in ua for x in ("Mobile", "iPhone", "Android")):
                return ua
        return (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/123.0.0.0 Safari/537.36"
        )

    def _handle_download(self, download: Download):
        path = os.path.join(DOWNLOADS_DIR, download.suggested_filename)
        download.save_as(path)
        print(f"[✓] Downloaded file saved to {path}")

    def stop(self) -> None:
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
        # Fallback cleanup in case the close event didn't fire
        if os.path.exists(self.profile_path):
            shutil.rmtree(self.profile_path, ignore_errors=True)
        print("[✓] Browser instance stopped and profile cleaned up.")