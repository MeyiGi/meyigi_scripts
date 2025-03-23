import pytest
import time
from meyigi_scripts.retry import retry  # Replace 'your_module' with the actual module name

# Helper function to count calls
class CallCounter:
    def __init__(self, fail_times, exception=ValueError):
        self.fail_times = fail_times
        self.calls = 0
        self.exception = exception

    def __call__(self, x):
        self.calls += 1
        if self.calls <= self.fail_times:
            raise self.exception(f"Failed attempt {self.calls}")
        return x * 2

def test_retry_success():
    """Test that the function succeeds after a few failures."""
    counter = CallCounter(fail_times=2)
    
    @retry(attempts=5, delay=0)
    def func(x):
        return counter(x)
    
    assert func(3) == 6
    assert counter.calls == 3  # Should fail twice, then succeed

def test_retry_failure():
    """Test that the function raises the exception after all attempts fail."""
    counter = CallCounter(fail_times=5)
    
    @retry(attempts=3, delay=0)
    def func(x):
        return counter(x)
    
    with pytest.raises(ValueError, match="Failed attempt 3"):
        func(3)
    
    assert counter.calls == 3  # Should fail three times and then stop

def test_retry_no_failures():
    """Test that the function works without any failures."""
    @retry(attempts=3, delay=0)
    def func(x):
        return x * 2
    
    assert func(4) == 8  # Should return the result immediately

def test_retry_different_exception():
    """Test that the function retries on the specified exception only."""
    counter = CallCounter(fail_times=2, exception=KeyError)
    
    @retry(attempts=5, delay=0, exceptions=(KeyError,))
    def func(x):
        return counter(x)
    
    assert func(3) == 6
    assert counter.calls == 3  # Should retry twice on KeyError and then succeed

def test_retry_does_not_retry_on_unexpected_exception():
    """Test that the function does not retry on unexpected exceptions."""
    counter = CallCounter(fail_times=1, exception=TypeError)
    
    @retry(attempts=5, delay=0, exceptions=(ValueError,))  # Not handling TypeError
    def func(x):
        return counter(x)
    
    with pytest.raises(TypeError, match="Failed attempt 1"):
        func(3)
    
    assert counter.calls == 1  # Should fail once and stop immediately
