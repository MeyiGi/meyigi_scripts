import pytest
from meyigi_scripts.clean_string import clean_string

def test_clean_string():
    text = "Example of text &*(&*(&(*&#)))            hello"
    expected_output = "Example of text hello"
    assert clean_string(text) == expected_output