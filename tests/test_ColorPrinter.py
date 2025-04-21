import pytest
from colorama import Fore, Style
from meyigi_scripts import ColorPrinter

@pytest.fixture
def printer():
    return ColorPrinter()

@pytest.mark.parametrize("code,expected_code", [
    ("black", Fore.BLACK),
    ("red", Fore.RED),
    ("green", Fore.GREEN),
    ("blue", Fore.BLUE),
    ("magenta", Fore.MAGENTA),
    ("cyan", Fore.CYAN),
    ("white", Fore.WHITE),
    ("reset", Fore.RESET)
])
def test_print_with_valid_colors(printer, capsys, code, expected_code):
    test_string = "hello"
    printer.cprint(test_string, code)
    captured = capsys.readouterr()
    assert captured.out == f"{expected_code}{test_string}{Style.RESET_ALL}\n"

def test_print_with_invalid_colores(printer, capsys):
    test_string = "hello"
    printer.cprint(test_string, "motherfucker")
    captured = capsys.readouterr()
    assert captured.out == f"{Fore.WHITE}{test_string}{Style.RESET_ALL}\n"