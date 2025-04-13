from bs4 import Tag
from typing import List

def get_attribute(tag: List[Tag] | Tag, attribute: str) -> List[str] | str:    
    """Funcition to extract specified attr or several attr from tag

    Args:
        tag List[Tag] | Tag: A list of BeautifulSoup tag or one tag object from which the attribute should be extracted  
        attribute (str): name of the attribute to extract

    Returns:
        List[str]: list of attributes extracted from tag

    Example:
        ```
        products = soup.select(".product")
        get_attributes(products, "href")
        ```
    """
    helper = lambda tag: tag.get(attribute, "").strip()
    if isinstance(tag, list):
        return [helper(tag=tag) for tag in tag if tag.get(attribute)]
    elif isinstance(tag, Tag):
        return helper(tag=tag)
    else:
        print("not worked")
        return []