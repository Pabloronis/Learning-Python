"""Module to calculate the number of grains of wheat on a chessboard."""

    
def square(number):
    """Return the number of grains in a single chessboard square.
    
    This function calulates the number of grains in single square, with square 1
    having 1 grain and all the other squares having twice as many grains as the
    previous one.
     - Square 1 = 1 grain, square 2 = 2 grains, square 3 = 4 grains, etc.
    """
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)

    
def total():
    """Return the total number of grains on the entire chessboard."""
    return 2 ** 64 - 1