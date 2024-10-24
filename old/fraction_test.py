import numpy as np
from fraction import Fraction

a = Fraction(1, 2)


def send(a, b: int) -> Fraction:
    return Fraction(a, b)


c = send(1, 2)
print(type(c))
d = c.numerator / c.denominator
print(type(d), d)

print(type(a))

arr = np.array([1, send(1, 2).denominator])
print(arr)
