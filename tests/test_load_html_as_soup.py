# tests/test_load_html_as_soup.py

import os
import pytest
from bs4 import BeautifulSoup
# Make sure to import the function from the correct module
from meyigi_scripts.fileio.loaders import load_html_as_soup 

@pytest.fixture
def temp_html_files(tmp_path):
    """
    Pytest fixture to create a temporary directory with a few sample HTML files
    for testing purposes.
    """
    # Define content for the test files
    html_content_1 = "<html><head><title>Test Page 1</title></head></html>"
    html_content_2 = "<html><body><h1>Welcome to Page 2</h1></body></html>"
    
    # Create the file paths within the temporary directory
    file1_path = tmp_path / "page1.html"
    file2_path = tmp_path / "page2.html"
    
    # Write the content to the files
    file1_path.write_text(html_content_1, encoding="utf-8")
    file2_path.write_text(html_content_2, encoding="utf-8")
    
    # Return a dictionary of paths for easy access in tests
    return {
        "file1": str(file1_path),
        "file2": str(file2_path),
        "nonexistent": str(tmp_path / "nonexistent.html")
    }

# === Success Cases ===

def test_load_single_valid_file(temp_html_files):
    """
    Tests if the function correctly loads a single HTML file as a BeautifulSoup object.
    """
    soup = load_html_as_soup(temp_html_files["file1"])
    
    assert isinstance(soup, BeautifulSoup), "Should return a BeautifulSoup object"
    assert soup.title.text == "Test Page 1", "The content of the parsed soup should be correct"

def test_load_multiple_valid_files(temp_html_files):
    """
    Tests if the function correctly loads a list of HTML files and returns a list of soup objects.
    """
    file_paths = [temp_html_files["file1"], temp_html_files["file2"]]
    soups = load_html_as_soup(file_paths)
    
    assert isinstance(soups, list), "Should return a list for multiple filepaths"
    assert len(soups) == 2, "The list should contain two soup objects"
    assert all(isinstance(s, BeautifulSoup) for s in soups), "All items in the list should be BeautifulSoup objects"
    
    # Verify content of each soup object
    assert soups[0].title.text == "Test Page 1"
    assert soups[1].h1.text == "Welcome to Page 2"

# === Edge Cases ===

def test_load_empty_list_returns_empty_list():
    """
    Tests if providing an empty list returns an empty list.
    """
    result = load_html_as_soup([])
    assert result == [], "Should return an empty list when given an empty list"

# === Error Cases ===

def test_load_single_nonexistent_file_raises_error(temp_html_files):
    """
    Tests if a FileNotFoundError is raised for a single non-existent filepath.
    """
    with pytest.raises(FileNotFoundError):
        load_html_as_soup(temp_html_files["nonexistent"])

def test_load_list_with_a_nonexistent_file_raises_error(temp_html_files):
    """
    Tests if a FileNotFoundError is raised if any file in a list does not exist.
    """
    file_paths = [temp_html_files["file1"], temp_html_files["nonexistent"]]
    with pytest.raises(FileNotFoundError):
        load_html_as_soup(file_paths)

@pytest.mark.parametrize("invalid_input", [
    123,                                  # Integer
    None,                                 # NoneType
    {"path": "file.html"},                # Dictionary
    [1, 2, 3],                            # List of integers
    ["valid_path.html", 123]              # List of mixed types
])
def test_load_invalid_input_type_raises_typeerror(invalid_input):
    """
    Tests if a TypeError is raised for inputs that are not a string or a list of strings.
    """
    with pytest.raises(TypeError):
        load_html_as_soup(invalid_input)