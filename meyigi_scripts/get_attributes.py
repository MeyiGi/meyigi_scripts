from bs4 import Tag
from typing import List

def get_attributes(tags: List[Tag], attribute: str) -> List[str]:    
    """Funcition to extract specified attrubutes from tags

    Args:
        tags (List[Tag]): A list of BeautifulSoup tag objects from which the attribute should be extracted  
        attribute (str): name of the attribute to extract

    Returns:
        List[str]: list of attributes extracted from tags

    Example:
        ```
        products = soup.select(".product")
        get_attributes(products, "href")
        ```
    """
    return [tag.get(attribute, "").strip() for tag in tags if tag.get(attribute)]