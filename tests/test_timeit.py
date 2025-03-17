import time
import pytest
from functools import wraps
from meyigi_scripts.timeit import timeit

@timeit
def sample_function(n):
    return sum(range(n))

def test_sample_function():
    """Test that function return he correct sum"""
    assert sample_function(5) == sum(range(5))
    assert sample_function(25) == sum(range(25))


def test_timeout_decorator(capfd):
    sample_function(1000)
    captured = capfd.readouterr()
    assert "Function sample_function executed in " in captured.out