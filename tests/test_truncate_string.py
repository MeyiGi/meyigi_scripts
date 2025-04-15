import pytest
from meyigi_scripts import truncate_string

@pytest.fixture
def text():
    return "Lorem Ipsum is simply dummy text of the printing and typesettin"

@pytest.mark.truncate
def test_truncate_with_dots(text):
    res = truncate_string(text, 10)
    assert res == "Lorem Ipsu..."


@pytest.mark.truncate
def test_truncate_without_dots(text):
    res = truncate_string(text, 10, triple_dot=False)
    assert res == "Lorem Ipsu"

