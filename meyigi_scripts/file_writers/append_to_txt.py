def append_to_txt(data: str | list[str], filename: str):
    """function to append the text to filename

    Args:
        data (str): data that should be appended
        filename (str): filepath where should be appended
    """
    with open(filename, "a", encoding="utf-8") as file:
        if isinstance(data, str):
            file.write(f"{data}\n")
        elif isinstance(data, list) and all([isinstance(item, str) for item in data]):
            for item in data:
                file.write(f"{item}\n")