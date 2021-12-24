from common import *


class Jacobi:

    @staticmethod
    def get_x1(x, A, b):
        return -((1 / A[0][0]) * (A[0][1] * x[1] + A[0][2] * x[2] - b[0]))

    @staticmethod
    def get_x2(x, A, b):
        return -((1 / A[1][1]) * (A[1][0] * x[0] + A[1][2] * x[2] - b[1]))

    @staticmethod
    def get_x3(x, A, b):
        return -((1 / A[2][2]) * (A[2][0] * x[0] + A[2][1] * x[1] - b[2]))

    @staticmethod
    def solve():
        A = [
            [0.84, 0.32, -0.10],
            [-0.36, -0.50, -0.14],
            [-0.04, 0.20, 1.66],
        ]
        b = (2.54, -2.36, 2.18)
        x0 = (3, 4, 1)
        current_x = x0
        iteration = 0
        next_x = x0
        while (1):
            iteration += 1
            current_x = next_x
            next_x = (
                Jacobi.get_x1(current_x, A, b), Jacobi.get_x2(current_x, A, b),
                Jacobi.get_x3(current_x, A, b))
            if norm(next_x, current_x) <= epsilon:  # т.к (1-q) /q = 1
                break
        return next_x, iteration

# не рабочий, просто опроверялся
class Seidel:

    @staticmethod
    def get_x1(x, A, b):
        return -((1 / A[0][0]) * (A[0][1] * x[1] + A[0][2] * x[2] - b[0]))

    @staticmethod
    def get_x2(x, A, b, x1):
        return -((1 / A[1][1]) * (A[1][0] * x1 + A[1][2] * x[2] - b[1]))

    @staticmethod
    def get_x3(A, b, x1, x2):
        return -((1 / A[2][2]) * (A[2][0] * x1 + A[2][1] * x2 - b[2]))

    @staticmethod
    def solve():
        A = [
            [0.84, 0.32, -0.10],
            [-0.04, 0.20, 1.66],
            [-0.36, -0.50, -0.14]
        ]
        b = (2.54, 2.18, -2.36)
        x0 = (3, 4, 1)
        current_x = x0
        iteration = 0
        next_x = x0
        while (1):
            iteration += 1
            current_x = next_x
            x1 = Seidel.get_x1(current_x, A, b)
            x2 = Seidel.get_x2(current_x, A, b, x1)
            x3 = Seidel.get_x3(A, b, x1, x2)
            next_x = (x1, x2, x3)
            if norm(next_x, current_x) <= epsilon:
                break
        return next_x, iteration
