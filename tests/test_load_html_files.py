import os
import pytest
from meyigi_scripts import load_html_files, append_to_txt

# Utility function to create files for testing
def create_html_files(directory, filenames):
    for filename in filenames:
        file_path = os.path.join(directory, filename)
        append_to_txt(f"content for {filename}", file_path)

# Clean up function
def remove_files(filenames, directory):
    for filename in filenames:
        file_path = os.path.join(directory, filename)
        if os.path.exists(file_path):
            os.remove(file_path)

@pytest.fixture
def filepath():
    # Define the filenames to be used
    filenames = ["1.html", "2.html", "3.html"]
    directory = "data"

    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)

    # Clean up any pre-existing files
    remove_files(filenames, directory)

    # Create new HTML files for the test
    create_html_files(directory, filenames)

    # Yield the directory for use in the test
    yield directory

    # Cleanup after the test is done
    remove_files(filenames, directory)

@pytest.mark.html
def test_html_files_valid(filepath):
    # Fetch the list of HTML files from the directory
    html_files = load_html_files(filepath)

    # Test that the files match the expected names
    expected_files = ["1.html", "2.html", "3.html"]
    assert sorted(html_files) == sorted(expected_files)
