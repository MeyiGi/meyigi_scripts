from typing import Union
from bs4 import BeautifulSoup, Tag
from meyigi_scripts import clean_string

def get_item(selector: str, soup: Union[BeautifulSoup, Tag, list[Tag]]) -> str:
    """
    Extracts and cleans text content from a BeautifulSoup object or a Tag object (or a list of Tag objects) 
    using a CSS selector.

    Args:
        selector (str): The CSS selector used to locate the desired element.
        soup (Union[BeautifulSoup, Tag, list[Tag]]): A BeautifulSoup object, a Tag object, or a list of Tag objects.

    Returns:
        str: The cleaned text content of the selected element. Returns an empty string if the element is not found.

    Example:
        product = soup.select_one(".product")
        title = get_item(".title", product)
    """
    def helper(x: BeautifulSoup):
        res = x.select_one(selector)
        if res is None:
            return ""
        return clean_string(res.text)

    if isinstance(soup, Tag) or isinstance(soup, BeautifulSoup):
        return helper(soup)
    if isinstance(soup, list) and all([isinstance(item, Tag) for item in soup]):
        return [helper(x) for x in soup]
    
    raise TypeError("Argument 'soup' must be either a BeautifulSoup object, Tag object, or a list of Tag objects.")
