from playwright.sync_api import Page
from typing import Protocol

class BrowserProtocol(Protocol):
    def start(self) -> Page:
        # Реализация с обходом детектов
        pass

    def stop(self) -> None:
        pass