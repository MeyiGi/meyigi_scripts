from bs4 import BeautifulSoup, Tag
from playwright.sync_api import ElementHandle
from typing import List
from meyigi_scripts.types import ScrapableElement, ScrapableElementList

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