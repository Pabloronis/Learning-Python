"""Function that calculates if a number is Armstrong or not."""


def is_armstrong_number(number):
    """Return True if a number is an Armstrong number."""
    digit = [int(i) for i in str(number)]
    result = [y ** len(digit) for y in digit] 
    return number == sum(result)