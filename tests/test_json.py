import os
import json
import pytest
from meyigi_scripts.fileio.json import append_to_json, read_json_file, read_json_folder

@pytest.fixture
def temp_json_file():
    """Creates a temporary JSON file for testing."""
    directory = "data"
    filename = os.path.join(directory, "test.json")
    
    # Create the directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)

    if os.path.exists(filename):
        os.remove(filename)
    yield filename
    if os.path.exists(filename):
        os.remove(filename)

@pytest.mark.json
def test_list(temp_json_file):
    data = [
        {"Name": "Meyigi", "Age": 34, "city": "Naryn"},
        {"Name": "Daniel", "Age": 24, "city": "New-York"},
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



@pytest.fixture
def temp_json_folder():
    """Creates a temporary folder with multiple JSON files for testing."""
    folder = "data/test_folder"
    os.makedirs(folder, exist_ok=True)
    
    # Cleanup before and after test
    for f in os.listdir(folder):
        os.remove(os.path.join(folder, f))

    yield folder

    for f in os.listdir(folder):
        os.remove(os.path.join(folder, f))
    os.rmdir(folder)

@pytest.mark.json
def test_read_single_dict(temp_json_file):
    data = {"Name": "Alice", "Age": 30}
    with open(temp_json_file, "w", encoding="utf-8") as f:
        json.dump(data, f)
    
    result = read_json_file(temp_json_file)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["Name"] == "Alice"
    assert result[0]["Age"] == 30

@pytest.mark.json
def test_read_list_of_dicts(temp_json_file):
    data = [{"Name": "Alice"}, {"Name": "Bob"}]
    with open(temp_json_file, "w", encoding="utf-8") as f:
        json.dump(data, f)
    
    result = read_json_file(temp_json_file)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["Name"] == "Alice"
    assert result[1]["Name"] == "Bob"

@pytest.mark.json
def test_read_invalid_json(temp_json_file):
    with open(temp_json_file, "w", encoding="utf-8") as f:
        f.write("invalid json")
    
    with pytest.raises(ValueError):
        read_json_file(temp_json_file)

@pytest.mark.json
def test_read_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        read_json_file("nonexistent.json")

@pytest.mark.json
def test_read_json_folder(temp_json_folder):
    # Create multiple JSON files
    file1 = os.path.join(temp_json_folder, "file1.json")
    file2 = os.path.join(temp_json_folder, "file2.json")
    json.dump({"Name": "Alice"}, open(file1, "w", encoding="utf-8"))
    json.dump([{"Name": "Bob"}, {"Name": "Charlie"}], open(file2, "w", encoding="utf-8"))
    
    result = read_json_folder(temp_json_folder)
    assert isinstance(result, list)
    names = [item["Name"] for item in result]
    assert "Alice" in names
    assert "Bob" in names
    assert "Charlie" in names

@pytest.mark.json
def test_read_json_folder_with_non_json(temp_json_folder):
    # Create one JSON and one non-JSON file
    json_file = os.path.join(temp_json_folder, "file.json")
    txt_file = os.path.join(temp_json_folder, "file.txt")
    json.dump({"Name": "Alice"}, open(json_file, "w", encoding="utf-8"))
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write("ignore this")
    
    result = read_json_folder(temp_json_folder)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["Name"] == "Alice"

@pytest.mark.json
def test_read_json_folder_invalid_directory():
    with pytest.raises(NotADirectoryError):
        read_json_folder("invalid_folder")