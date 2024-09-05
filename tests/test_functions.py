import pytest
import sys
import os

#Add the root directory(parent of the current directory) to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
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


def test_apply_decorator(capfd):
    
    def simple_func():
        print("Original function called")
        return "Function result"
    
    # Apply the decorator using the student's function
    decorated_func = functions.apply_decorator(simple_func)
    result = decorated_func()

    # Capture the output 
    out, _ = capfd.readouterr()

    # Check if the decorator applied correctly
    assert "Decorator Applied" in out
    assert "Original function called" in out
    assert result == "Function result"

def test_sort_by_age():
    people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    sorted_people = functions.sort_by_age(people)
    assert sorted_people == [("Bob", 25), ("Alice", 30), ("Charlie", 35)]

    # Test with a different List
    people = [("Tom",50),("Jerry",30),("Spike",70)]
    sorted_people = functions.sort_by_age(people)
    assert sorted_people == [("Jerry",30),("Tom",50),("Spike",70)]

def test_merge_dicts():
    dict1 = {'a':1, 'b':2}
    dict2 = {'b':3, 'c':4}
    merged_dict = functions.merge_dicts(dict1, dict2)
    assert merged_dict == {'a':1, 'b':5, 'c':4}

    # Test with empty dictionaries
    dict1 = {}
    dict2 = {}
    merged_dict = functions.merge_dicts(dict1, dict2)
    assert merged_dict == {}

    # Test with no overlapping keys
    dict1 = {'x':10}
    dict2 = {'y': 20}
    merged_dict = functions.merge_dicts(dict1, dict2)
    assert merged_dict == {'x':10, 'y':20}

def test_function_names():
    requirerd_functions = [
        "add_numbers",
        "is_even",
        "reverse_string",
        "count_vowels",
        "calculate_factorial",
        "apply_decorator",
        "sort_by_age",
        "merge_dicts",
    ]

    for func_name in requirerd_functions:
        assert hasattr(functions, func_name), f"Function '{func_name}' is missing or incorrectly named."

# Run the tests
if __name__ == "__main__":
    pytest.main()