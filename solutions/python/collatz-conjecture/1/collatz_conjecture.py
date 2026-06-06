"""Function returns number os steps to 1 based on Collatz Conjecture."""

def steps(number):
    """Return the total ammount of steps to reach 1.

    Rules according to Collatz Conjecture:
    - If it's even, divide it by 2.
    - If it's odd, multiply it by 3 and add 1.
    """
    total = 0
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    if number == 1:
        return 0
    while number != 1:
        total = total + 1 
        if number % 2 == 0:
            number = number // 2
        elif number % 2 != 0:
            number = (number * 3) + 1
    return total