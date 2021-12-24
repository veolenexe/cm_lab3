from algo import *

#Якоби
result, iteration = Jacobi().solve()
print(result)
print(iteration)

# метод Гауса-Зейделя не работает, так как сх нет там бесконечный цикл

#result, iteration = Seidel().solve()
#print(result)
#print(iteration)