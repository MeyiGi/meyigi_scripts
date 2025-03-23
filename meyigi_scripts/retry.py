import time
import functools

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