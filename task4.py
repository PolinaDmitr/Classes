# циклы
# цикл со счётчиком

for i in (1, 2, 3, 4, 5, 6, 7, 8):
    print(i)

# от 0 (по умолчанию) до значения 10, шаг 1
print('------')
for i in range(10):
    print(i)
# от значения 2 до значения 10, шаг 1
print('------')
for i in range(2, 10):
    print(i)
# от значения 2 до значения 10 с шагом 2
print('------')
for i in range(2, 10, 2):
    print(i)

# цикл while
print('----')
a = 1
while a % 15 != 0:
    print(a)
    a += 1