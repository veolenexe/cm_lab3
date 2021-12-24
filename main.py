from algo import *

# метод половинного деления(дихотомии)
result, iteration = Dichotomies().solve()
print(result)
print(iteration)

# метод Ньютона
result, iteration = Newton().solve()
print(result)
print(iteration)

# метод модифицированный Ньютона
result, iteration = ModNewton().solve()
print(result)
print(iteration)

# метод хорд
result, iteration = Chord().solve()
print(result)
print(iteration)

# метод подвижных хорд
result, iteration = MovChord().solve()
print(result)
print(iteration)

# метод простой итерации
result, iteration = SipleIteration().solve()
print(result)
print(iteration)
