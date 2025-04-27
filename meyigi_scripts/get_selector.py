from enum import Enum
from typing import Type, Optional

def get_selector(enum_cls: Type[Enum], name: str) -> Optional[str]:
    try:
        return enum_cls[name].value
    except KeyError:
        return None