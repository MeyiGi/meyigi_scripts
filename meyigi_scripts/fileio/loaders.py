import os
from bs4 import BeautifulSoup

def load_html_files(filepath: str) -> list[str]:
    """function to get all html files from provided directory

    Args:
        filepath (str): filepath where containing html files

    Returns:
        list[str]: html pathes
    """
    return [f for f in os.listdir(filepath) if f.endswith(".html")]
    
def load_html_as_soup(filepath: str| list[str]) -> BeautifulSoup:
    """
    Loads a local HTML file and returns it as a BeautifulSoup object for parsing.

    Args:
        filepath (str): The path to the local HTML file.

    Returns:
        BeautifulSoup: A BeautifulSoup object ready for parsing.
    
    Raises:
        FileNotFoundError: If the specified filepath does not exist.
    """
    if isinstance(filepath, str):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"No such file or directory: '{filepath}'")
        
        with open(filepath, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        return BeautifulSoup(html_content, "lxml")
    elif isinstance(filepath, list) and all(isinstance(f, str) for f in filepath):
        soups = []
        for path in filepath:
            if not os.path.exists(path):
                raise FileNotFoundError(f"No such file or directory: '{path}'")
            
            with open(path, "r", encoding="utf-8") as f:
                html_content = f.read()
            
            soups.append(BeautifulSoup(html_content, "lxml"))
        
        return soups
    else:
        raise TypeError("filepath must be a string or a list of strings")