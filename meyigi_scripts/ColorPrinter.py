from colorama import Fore, Style, init

init(autoreset=True)

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
