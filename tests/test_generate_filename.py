import pytest
from meyigi_scripts import generate_filename

@pytest.fixture
def filename():
    return "hello.txt"

def test_generate_filename_with_cleaning(filename):
    output = generate_filename(filename)
    assert output.startswith("hello")
    assert output.endswith("txt")