import os
import json
import pytest
from meyigi_scripts.file_writers.append_to_json import append_to_json

@pytest.fixture
def temp_json_file():
    filename = "data/test.json"
    if os.path.exists(filename):
        os.remove(filename)
    yield filename
    if os.path.exists(filename):
        os.remove(filename)

@pytest.mark.json
def test_list(temp_json_file):
    data = [
        {"Name" : "Meyigi", "Age" : 34, "city" : "Naryn"},
        {"Name" : "Daniel", "Age" : 24, "city" : "New-York"},
    ]
    append_to_json(data, temp_json_file)
    with open(temp_json_file, "r") as file:
        res = json.load(file)
    assert res[0]["Name"] == "Meyigi"
    assert res[0]["Age"] == 34
    assert res[0]["city"] == "Naryn"
    assert res[1]["Name"] == "Daniel"
    assert res[1]["Age"] == 24
    assert res[1]["city"] == "New-York"