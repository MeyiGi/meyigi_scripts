import pytest
from bs4 import BeautifulSoup
from meyigi_scripts import get_attribute

html_doc = """
<html>
<body>
  <a class="product" href="http://example1.com">Product 1</a>
  <a class="product" href="http://example2.com">Product 2</a>
  <a class="product">Product 3</a>
  <a class="product" href="http://example4.com">Product 4</a>
</body>
</html>
"""

@pytest.fixture
def soup():
    return BeautifulSoup(html_doc, "html.parser")

@pytest.mark.soup
def test_get_attributes_with_valid_attribute_several(soup):
    products = soup.select(".product")
    hrefs = get_attribute(products, "href")
    assert hrefs == ["http://example1.com", "http://example2.com", "http://example4.com"]

@pytest.mark.soup
def test_get_attributes_with_valid_attribute(soup):
    product = soup.select_one(".product")
    href = get_attribute(product, "href")
    assert href == "http://example1.com"

@pytest.mark.soup
def test_get_attributes_with_invalud_attribute(soup):
    products = soup.select(".product")
    attributes = get_attribute(products, "motherfucker")
    assert attributes == []