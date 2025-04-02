import time
from functools import wraps

def timeit(func):
    """Decorator which is measuring time to executed 

    Args:
        func (_type_): taking a function to measure
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper