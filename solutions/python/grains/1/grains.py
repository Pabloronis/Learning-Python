def square(number):
    if number == 1:
        return 1
    if 2 <= number <= 64:
        number = 2 ** (number -1)
        return number
    else:
        raise ValueError("square must be between 1 and 64")
    
def total():
    return (2 ** 64) - 1