import math
# все значения либо константы либо высислялись в отчете по лабораторной работе
e = math.e
(a, b) = (0.5, 0.6)
x0 = 0.6
epsilon = 5e-06

m = 1.6487212707


def ln(x):
    return math.log(x)


def f(x):
    return (e ** x) - 2.1 + (x ** 2)


def df(x):
    return e ** x + 2 * x


def ddf(x):
    return e ** x + 2


def fi(x):
    return ln((2.1 - x ** 2))
