import time
import os
import shutil
import asyncio
from uuid import uuid4
from fake_useragent import UserAgent
from ..protocols import BrowserProtocol
from .network import get_random_headers
from playwright.async_api import async_playwright, Page, Download

DOWNLOADS_DIR = os.path.join(os.getcwd(), "downloads")


async def wait_for_min_elements(page: Page, selector, min_count=3, timeout=15):
    """
    Wait until at least `min_count` elements matching `selector` are present on the page.
    Args:
        page: Playwright Page object
        selector: CSS or XPath selector string
        min_count: minimum number of elements to wait for
        timeout: max seconds to wait
    Raises:
        TimeoutError if min_count elements not found within timeout.
    """
    start_time = time.time()

    # First wait for at least one element (guaranteed by wait_for_selector)
    await page.wait_for_selector(selector, timeout=timeout * 1000)

    locator = page.locator(selector)

    while True:
        count = await locator.count()
        if count >= min_count:
            return
        if time.time() - start_time > timeout:
            raise TimeoutError(
                f"Timeout waiting for at least {min_count} elements matching {selector}, found {count}"
            )
        await asyncio.sleep(0.2)


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

    async def start(self) -> Page:
        self.playwright = await async_playwright().start()

        random_ua = self._get_desktop_user_agent()

        self.browser = await self.playwright.chromium.launch_persistent_context(
            user_data_dir=self.profile_path,
            headless=False,
            accept_downloads=True,
            viewport={"width": 1280, "height": 800},
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

        self.page = self.browser.pages[0] if self.browser.pages else await self.browser.new_page()

        await self.page.add_init_script(
            """
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

    async def stop(self) -> None:
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()
        # Fallback cleanup in case the close event didn't fire
        if os.path.exists(self.profile_path):
            shutil.rmtree(self.profile_path, ignore_errors=True)
        print("[✓] Browser instance stopped and profile cleaned up.")


async def setup_browser(
    URL: str,
    DEFAULT_TIMEOUT: int = 10,
):
    headers = get_random_headers()
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context(
        user_agent=headers["User-Agent"],
        locale="en-US",
        extra_http_headers=headers,
    )
    context.set_default_timeout(DEFAULT_TIMEOUT)
    page = await context.new_page()
    await page.goto(URL)
    return playwright, browser, context, page