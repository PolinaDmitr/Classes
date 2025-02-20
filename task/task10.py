#сравнение дробных чисел
a = int(input())    #число
b = int(input())    #куб числа
delta = 0.0000000000001
a_cub = a ** (1 / 3)  #то, что нам нужно
print(a_cub)
print (abs(b - a_cub) < delta)
print(abs(a_cub - int(a_cub + delta)) < delta)
