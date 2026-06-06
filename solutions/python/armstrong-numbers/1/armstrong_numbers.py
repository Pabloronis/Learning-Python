def is_armstrong_number(number):
    """Return True if a number is an Armstrong number."""
    digit = [int(x) for x in str(number)]
    result = [y ** len(digit) for y in digit] 
    return number == sum(result)