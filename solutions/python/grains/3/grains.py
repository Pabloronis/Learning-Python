"""Module providing a function printing python version."""

import sys

def print_python_version():
    """Function printing python version."""
    print(sys.version)

    
def square(number):
    """Function provides numer of grains in square"""
    if number == 1:
        return 1
    if 2 <= number <= 64:
        number = 2 ** (number -1)
        return number
    raise ValueError("square must be between 1 and 64")
    
def total():
    """Function gives total ammount of grains amongs all squares"""
    return (2 ** 64) - 1