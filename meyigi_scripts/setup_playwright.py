from meyigi_scripts import get_random_headers
from playwright.sync_api import sync_playwright

def setup_browser(
        URL: str,
        DEFAULT_TIMEOUT: int = 10,
):
    headers = get_random_headers()
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        user_agent=headers["User-Agent"],
        locale="en-US",
        extra_http_headers=headers
    )
    context.set_default_timeout(DEFAULT_TIMEOUT)
    page = context.new_page()
    page.goto(URL)
    return playwright, browser, context, page