import wget

def download_file(filename: str, url: str) -> None:
    wget.download(url, filename)