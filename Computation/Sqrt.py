import timeit


def mySqrt(x):

    r = x/4
    prev = 0
    precision = 10 ** (-14)
    while abs(prev - r) > precision:
        prev = r
        r = (r + x / r) / 2

    return r


print("PySqrt      :", timeit.Timer(
    'sqrt(17)', 'from math import sqrt').timeit(100))
print("MySqrt     :", timeit.Timer(
    'f(17)', 'from __main__ import mySqrt as f').timeit(100))
