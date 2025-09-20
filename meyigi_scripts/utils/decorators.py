import time
import functools
from functools import wraps

def retry(attempts=3, delay=1, exceptions=(Exception,)):
    """
    Decorator which is retriying function several times
    :params attempts: number of attems for function
    :params delay: sleep time before retriying of fucntion
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for i in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    print(f"Attemp number: {i}, fail: {e}, waiting {delay} sec")
                    time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator

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