import pytest
from bs4 import BeautifulSoup
from meyigi_scripts import get_item

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
def test_title_extracted_with_valid_selector(soup):
    title = get_item(".product", soup)
    assert title == "Product 1"

@pytest.mark.soup
@pytest.mark.skip(reason="I need change logic in get_item for working several Tag objects")
def test_title_extracted_with_valid_selector_multiple(soup):
    titles = get_item(soup.select(".product"))
    assert titles[0] == "Product 1"
    assert titles[1] == "Product 2"
    assert titles[2] == "Product 3"


@pytest.mark.soup
def test_title_extracted_with_invalid_selectro(soup):
    title = get_item("motherfucker", soup)
    assert title == ""