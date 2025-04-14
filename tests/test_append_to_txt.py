import os
import pytest
from meyigi_scripts import append_to_txt

@pytest.fixture
def filename():
    filepath = "data/output.txt"
    if os.path.exists(filepath):
        os.remove(filepath)
    yield filepath
    if os.path.exists(filepath):
        os.remove(filepath)

@pytest.mark.txt
def test_append_to_txt(filename):
    data = ["hoho", "jojo", "koko"]

    for item in data:
        append_to_txt(item, filename)
    
    with open(filename, "r", encoding="utf-8") as file:
        results = file.readlines()

    assert f"{data[1]}\n" == results[1]
    assert f"{data[2]}\n" == results[2] 
    assert f"{data[0]}\n" == results[0]
    

@pytest.mark.txt
def test_append_to_txt_multuple(filename):
    data = ["hoho", "jojo", "koko"]

    append_to_txt(data, filename)
    
    with open(filename, "r", encoding="utf-8") as file:
        results = file.readlines()

    assert f"{data[1]}\n" == results[1]
    assert f"{data[2]}\n" == results[2] 
    assert f"{data[0]}\n" == results[0]
    