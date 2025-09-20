from enum import Enum
from typing import Type, Optional, Union, List
from bs4 import BeautifulSoup, Tag
from ..utils.text import clean_string
from playwright.sync_api import ElementHandle
from ..types import ScrapableElement, ScrapableElementList

def get_selector(enum_cls: Type[Enum], name: str) -> Optional[str]:
    try:
        return enum_cls[name].value
    except KeyError:
        return None

def get_attribute(
    tag: ScrapableElement | ScrapableElementList, 
    attribute: str
) -> List[str] | str:    
    """Extract specified attribute(s) from HTML element(s).
    
    Works with both BeautifulSoup tags and Playwright ElementHandles, handling both
    single elements and lists of elements.

    Args:
        tag: Either:
            - A single scrapable element (BeautifulSoup, Tag, or ElementHandle)
            - A list of scrapable elements
        attribute: Name of the attribute to extract (e.g., "href", "class")

    Returns:
        The attribute value(s):
        - For single element input: returns attribute value as string
        - For list input: returns list of attribute values
        - Returns empty string/list if attribute not found

    Examples:
        >>> # BeautifulSoup usage
        >>> soup = BeautifulSoup('<a href="example.com">Link</a>', 'html.parser')
        >>> get_attribute(soup.a, "href")  # Returns "example.com"

        >>> # Playwright usage
        >>> element = page.query_selector("a")  # Assume page is loaded
        >>> get_attribute(element, "href")  # Returns URL or empty string

        >>> # List usage
        >>> products = soup.select(".product")
        >>> get_attribute(products, "data-id")  # Returns list of data IDs
    """
    def helper(element: ScrapableElement) -> str:
        """Inner helper to extract attribute from single element."""
        if isinstance(element, ElementHandle):
            return element.get_attribute(attribute) or ""
        return element.get(attribute, "")
    
    if isinstance(tag, (BeautifulSoup, Tag, ElementHandle)):
        return helper(element=tag)
    
    return [helper(element=el) for el in tag if (
        (isinstance(el, (Tag, BeautifulSoup)) and el.get(attribute) is not None) or
        (isinstance(el, ElementHandle) and el.get_attribute(attribute) is not None)
    )]

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
