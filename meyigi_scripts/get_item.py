

from bs4 import BeautifulSoup
from meyigi_scripts import clean_string

def get_item(selector: str, soup: BeautifulSoup) -> str:
    """
    Extracts and cleans text content from a BeautifulSoup object using a CSS selector.

    Args:
        selector (str): The CSS selector used to locate the desired element.
        soup (BeautifulSoup): The BeautifulSoup object containing the HTML content.

    Returns:
        str: The cleaned text content of the selected element. Returns an empty string if the element is not found.

    ```
    product = soup.select_one(".product")
    title = get_item(".title", product)
    ```
    """
    res = soup.select_one(selector.value)
    if res is None:
        return ""
    return clean_string(res.text)