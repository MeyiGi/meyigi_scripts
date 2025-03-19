import pytest
import requests
from bs4 import BeautifulSoup
from meyigi_scripts.get_requests import get_requests

@pytest.fixture
def url():
    yield "http://www.example.com"

def test_get_requests_success(requests_mock, url):
    text = "<html><body><h1>Test</h1></body></html>"

    requests_mock.get(url, text=text)
    soup = get_requests(url)

    assert isinstance(soup, BeautifulSoup)
    assert soup.select_one("h1").text == "Test" 

def test_get_requests_failure(requests_mock, url):
    # Mock a 404 response
    requests_mock.get(url=url, status_code=404, text="Not Found")
    
    # Call the function
    with pytest.raises(requests.exceptions.HTTPError):  # Expecting an HTTPError to be raised
        get_requests(url)

def test_get_requests_timeout(requests_mock, url):
    requests_mock.get(url=url, exc=requests.exceptions.ReadTimeout)

    with pytest.raises(requests.exceptions.ReadTimeout):
        get_requests(url)

def test_get_requests_connection(requests_mock, url):
    requests_mock.get(url=url, exc=requests.exceptions.ConnectionError)

    with pytest.raises(requests.exceptions.ConnectionError):
        get_requests(url)

def test_get_requests_exception(requests_mock, url):
    requests_mock.get(url=url, exc=requests.exceptions.RequestException)

    with pytest.raises(requests.exceptions.RequestException):
        get_requests(url)