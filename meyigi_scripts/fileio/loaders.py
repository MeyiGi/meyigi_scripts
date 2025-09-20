import os

def load_html_files(filepath: str) -> list[str]:
    """function to get all html files from provided directory

    Args:
        filepath (str): filepath where containing html files

    Returns:
        list[str]: html pathes
    """
    return [f for f in os.listdir(filepath) if f.endswith(".html")]
    