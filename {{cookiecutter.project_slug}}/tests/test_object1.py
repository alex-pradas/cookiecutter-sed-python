import pytest
from sedlabdemo import hello

def test_sum():
    """provide more information here if required. For example, this test the sum"""

    # prepare inputs
    a = 1
    b = 2
    expected_result = 3

    # perform operation
    res = sum([a, b])

    # assert
    assert res == expected_result


def test_for_exception():
    """Ensure that the variable d will raise an exception"""
    d = {}
    with pytest.raises(KeyError):
        # include in this `with statement` the line that will raise the exception
        d["non_existing_key"]

def test_function_from_package():
    """Test a function from this package"""

    greeting = hello("Alex")

    assert greeting == "Hello Alex!"