import math

# все значения либо константы либо высислялись в отчете по лабораторной работе
e = math.e
epsilon = 5e-05


def norm(x1, x2):
    return abs((x1[0] - x2[0])) + abs((x1[1] - x2[1])) + abs((x1[2] - x2[2]))
