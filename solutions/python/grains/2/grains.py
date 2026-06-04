"""Module providing a function printing python version."""

import sys

def print_python_version():
    print(sys.version)

    
def square(number):
    if number == 1:
        return 1
    if 2 <= number <= 64:
        number = 2 ** (number -1)
        return number
    raise ValueError("square must be between 1 and 64")
    
def total():
    return (2 ** 64) - 1