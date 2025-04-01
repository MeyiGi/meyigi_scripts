import wget

def download_file(filename: str, url: str) -> None:
    """Downloding file on url to filename

    Args:
        filename (str): Filename to save the data
        url (str): Url content to save in filename
    """
    wget.download(url, filename)