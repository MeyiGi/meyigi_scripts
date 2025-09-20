import os
import re
from colorama import Fore, Style, init
from datetime import datetime
init(autoreset=True)

def truncate_string(s: str, max_length: int, triple_dot: bool = True) -> str:
    """Truncates a string if it exceeds a given max length."""
    if triple_dot:
        return s[:max_length] + "..." if len(s) > max_length else s
    return s[:max_length] if len(s) > max_length else s

def clean_string(text: str) -> str:
    """
    Function which is deleting trash from the given string

    :params text: Initial string
    :return: cleaned text
    """
    
    cleaned_text = re.sub(r'[^a-zA-Zа-яА-Я0-9\s]', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    return cleaned_text

def generate_filename(filename: str, *, is_clean: bool = True) -> str:
    name, ext = os.path.splitext(filename)
    date = datetime.now().strftime("%y-%m-%d_%H:%M:%S") + f"_{datetime.now().microsecond // 1000:03d}ms"
    if is_clean: filename = clean_string(filename)
    return f"{name}{date}.{ext}"


class ColorPrinter:
    """
    A utility class for printing colored text to the terminal using colorama.

    Supported Colors:
        - black
        - red
        - green
        - yellow
        - blue
        - magenta
        - cyan
        - white
        - reset (restores default terminal color)

    Notes:
        - Color names are case-insensitive.
        - If an unsupported color is provided, the text will default to white.

    Example:
        >>> printer = ColorPrinter()
        >>> printer.cprint("Hello in red", "red")
        >>> printer.cprint("This will default to white", "notacolor")
    """

    color_map = {
        "black": Fore.BLACK,
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE,
        "reset": Fore.RESET
    }

    def cprint(self, content: str, color: str) -> None:
        """
        Print the given content in the specified color.

        Args:
            content (str): The text to print.
            color (str): The name of the color (case-insensitive). 
                         If the color is not recognized, defaults to white.

        Example:
        ```
        printer = ColorPrinter()
        printer.cprint("Success!", "green")
        printer.cprint("Warning!", "yellow")
        printer.cprint("Oops!", "invalidcolor")  # Will default to white
        ```
        """
        color_code = self.color_map.get(color.lower(), Fore.WHITE)
        print(f"{color_code}{content}{Style.RESET_ALL}")
