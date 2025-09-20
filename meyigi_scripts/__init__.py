# meyigi_scripts/__init__.py

# Explicitly import the public API from the new structure
from .ai.chatgpt import chatgpt_get_response
from .ai.gemini import generate

from .fileio.excel import append_to_excel
from .fileio.json import append_to_json
from .fileio.text import append_to_txt, load_txt
from .fileio.loaders import load_html_files

from .scraping.network import get_requests, get_random_headers
from .scraping.parsers import get_item, get_attribute, get_selector
from .scraping.browser import PlaywrightUndetected, wait_for_min_elements, setup_browser

from .system.human_like_scroll_to_bottom import human_like_scroll_bottom_hits
from .system.init_project import init_project
from .system.prevent_sleep import prevent_sleep

from .utils.decorators import timeit, retry
from .utils.text import clean_string, truncate_string, generate_filename, ColorPrinter
from .utils.random import random_delay, random_proxy


# Define public API for 'from meyigi_scripts import *'
__all__ = [
    # ai
    "chatgpt_get_response",
    "generate",

    # fileio
    "append_to_excel",
    "append_to_json",
    "append_to_txt",
    "load_txt",
    "load_html_files",

    # scraping
    "get_requests",
    "get_random_headers",
    "get_item",
    "get_attribute",
    "get_selector",
    "PlaywrightUndetected",
    "wait_for_min_elements",
    "setup_browser",

    # system
    "human_like_scroll_bottom_hits",
    "init_project",
    "prevent_sleep",

    # utils
    "timeit",
    "retry",
    "clean_string",
    "truncate_string",
    "random_delay",
    "random_proxy",
    "generate_filename",
    "ColorPrinter",
]
