"""Function that calculates if a number is Armstrong or not."""


def is_armstrong_number(number):
    """Return True if a number is an Armstrong number."""
    digit = [int(algarismo_str) for algarismo_str in str(number)]
    result = [algarismo_int ** len(digit) for algarismo_int in digit] 
    return number == sum(result)