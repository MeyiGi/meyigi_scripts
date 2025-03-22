import re

def clean_string(text: str) -> str:
    """
    Function which is deleting trash from the given string

    :params text: Initial string
    :return: cleaned text
    """
    
    cleaned_text = re.sub(r'[^a-zA-Zа-яА-Я0-9\s]', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    return cleaned_text