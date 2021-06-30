import pytest

# Resources - https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
def inc(x):
    return x + 1


def test_answer():
    assert inc(4) == 5
    
def test_testing():
    test = True
    assert test == True