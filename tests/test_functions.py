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

def test_count_vowels():
    assert functions.count_vowels("hello") == 2
    assert functions.count_vowels("HELLO") == 2
    assert functions.count_vowels("Python") == 1
    assert functions.count_vowels("xyz") == 0

def test_calculate_factorial():
    assert functions.calculate_factorial(5) == 120
    assert functions.calculate_factorial(0) == 1
    assert functions.calculate_factorial(1) == 1

    # Ensure there is an error for negative input
    with pytest.raises(ValueError):
        functions.calculate_factorial(-1)