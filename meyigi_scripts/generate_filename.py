
import os
from datetime import datetime
from meyigi_scripts import clean_string

def generate_filename(filename: str, *, is_clean: bool = True) -> str:
    name, ext = os.path.splitext(filename)
    date = datetime.now().strftime("%y-%m-%d_%H:%M:%S") + f"_{datetime.now().microsecond // 1000:03d}ms"
    if is_clean: filename = clean_string(filename)
    return f"{name}{date}.{ext}"