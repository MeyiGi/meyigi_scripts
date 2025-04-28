from bs4 import BeautifulSoup, Tag
from playwright.sync_api import ElementHandle

ScrapableElement = BeautifulSoup | Tag | ElementHandle
ScrapableElementList = list[ScrapableElement]