import os
import pytest
from meyigi_scripts import load_txt, append_to_txt

txt_data = """This is very important data1
This is very important data2"""

@pytest.fixture
def filename():
    filepath = "data/output.txt"
    if os.path.exists(filepath):
        os.remove(filepath)
    append_to_txt(txt_data, filepath)
    yield filepath
    if os.path.exists(filepath):
        os.remove(filepath)

@pytest.mark.txt
def test_load_data(filename):
    data = load_txt(filename).split("\n")
    assert data[0] == "This is very important data1"
    assert data[1] == "This is very important data2"