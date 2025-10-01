import os
import csv
import pytest
from meyigi_scripts import append_to_csv, read_csv_as_dicts

@pytest.fixture
def temp_csv_file(tmp_path):
    filename = tmp_path / "test.csv"
    yield str(filename)
    if os.path.exists(filename):
        os.remove(filename)

def test_append_to_csv_creates_file(temp_csv_file):
    # Write a single dictionary to CSV and verify file creation.
    data = {"Name": "Alice", "Age": "30", "City": "New York"}
    append_to_csv(data, temp_csv_file)
    assert os.path.exists(temp_csv_file)
    
    with open(temp_csv_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        assert headers == list(data.keys())
        rows = list(reader)
        assert len(rows) == 1
        assert rows[0] == data

def test_append_to_csv_multiple(temp_csv_file):
    # Append multiple dictionaries and verify that rows are added.
    data1 = {"Name": "Alice", "Age": "30", "City": "New York"}
    data2 = {"Name": "Bob", "Age": "25", "City": "Los Angeles"}
    
    append_to_csv(data1, temp_csv_file)
    append_to_csv(data2, temp_csv_file)
    
    # Use read_csv_as_dicts to read and verify the file content.
    rows = read_csv_as_dicts(temp_csv_file)
    assert len(rows) == 2
    assert rows[0] == data1
    assert rows[1] == data2

def test_read_csv_as_dicts_invalid_file(tmp_path):
    # Create an empty file and expect ValueError when reading it.
    file_path = tmp_path / "empty.csv"
    file_path.write_text("")
    with pytest.raises(ValueError):
        read_csv_as_dicts(str(file_path))
        
def test_read_csv_as_dicts_nonexistent_file(tmp_path):
    # Expect FileNotFoundError when reading a non-existent file.
    file_path = tmp_path / "nonexistent.csv"
    with pytest.raises(FileNotFoundError):
        read_csv_as_dicts(str(file_path))