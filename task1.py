print('LLLL')
print()
print('GGGG', 'HHHH', end='\n', sep=',')
print('gggg')
# # \n \s \t \d \r \0 -- специальные символы
a = 7
print(a)
a = 90
a = 92
print(a)
a = 'wmpo'
print(a)
string = input()
a = int(string)
b = int(input())
print(a + b)
b = '7.8'
print(b * 2)
f = str(7.8)
print(f * 3)


#считать два числа и найти их среднее арифметическое

a = int(input())
b = int(input())
print(a + b)
a = 5
b = 6
print ((a + b) / 2) #просто деление
print((a + b) // 2) #целочисленное деление
print((a + b) % 5) #остаток от деления
print('-11 // 5 = ', -(a + b) // 5)
print('-11 % 5 =', -(a + b) % 5)
print('|-11| // 5 = ', abs(-(a + b)) // 5)
print('|-11| % 5 = ', abs(-(a + b)) % 5)

# 56 : 5 = 11 (ост.1) 11 * 5 + 1 = 56
# 11 / 5 = 2 (1) -11 / 5 = -3 (4) -- вот такая странная логика при делении отрицательных чисел
dig_max = max(a, b)
print(dig_max)
print(min(a, b))