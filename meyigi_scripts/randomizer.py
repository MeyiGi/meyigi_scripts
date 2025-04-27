import time
import random
from typing import Iterable, Optional

def random_delay(min_delay: float, max_delay: float) -> None:
    time.sleep(random.uniform(min_delay, max_delay))

def random_proxy(proxies: Iterable[str]) -> Optional[str]:
    return random.choice(proxies) if proxies else None