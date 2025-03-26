import os
import pytest
from meyigi_scripts import download_file

@pytest.fixture
def load_filename_url():
    filename = "data/test.pdf"
    url = "https://media.geeksforgeeks.org/wp-content/uploads/20240226121023/GFG.pdf"
    if os.path.exists(filename):
        os.remove(filename)
    yield filename, url
    if os.path.exists(filename):
        os.remove(filename)

def test_download_file(load_filename_url):
    download_file(load_filename_url[0], load_filename_url[1])
    assert os.path.exists(load_filename_url[0])