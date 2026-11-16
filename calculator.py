# https://github.com/captainclashthe1-sudo/lab10-NW-CH
# Partner 1: Your name Eric Castro
# Partner 2: Partner's name Jackson Kokinda

import math


def square_root(a):
    if a < 0:
        raise ValueError('Cannot take the square root of a negative number')
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError('Cannot divide by zero')
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError('Invalid logarithm arguments')
    return math.log(b, a)


def exp(a, b):
    return a ** b


# Optional aliases for code written using the longer function names.
multiply = mul
divide = div
exponent = exp
