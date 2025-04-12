def append_to_txt(data: str, filename: str):
    """function to append the text to filename

    Args:
        data (str): data that should be appended
        filename (str): filepath where should be appended
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{data}\n")