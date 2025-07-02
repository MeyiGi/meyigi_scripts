import time
from playwright.sync_api import Page

def wait_for_min_elements(page: Page, selector, min_count=3, timeout=15):
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
    page.wait_for_selector(selector, timeout=timeout*1000)
    
    locator = page.locator(selector)
    
    while True:
        count = locator.count()
        if count >= min_count:
            return
        if time.time() - start_time > timeout:
            raise TimeoutError(f"Timeout waiting for at least {min_count} elements matching {selector}, found {count}")
        time.sleep(0.2)