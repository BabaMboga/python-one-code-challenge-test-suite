import pytest
# import the student functions.py
import functions

def test_add_numbers():
    assert functions.add_numbers(5, 10) == 15
    assert functions.add_numbers(-3, 7) == 4
    assert functions.add_numbers(0, 0) == 0

def test_is_even():
    assert functions.is_even(4) is True
    assert functions.is_even(7) is False
    assert functions.is_even(0) is True

def test_reverse_string():
    assert functions.reverse_string("hello") == "olleh"
    assert functions.reverse_string("Python") == "nohtyP"
    assert functions.reverse_string("") == ""