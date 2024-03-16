# максимальное и минимальное значение
a = int(input())
b = int(input())
d = int(input())
c = min(a, b, d)
print(c)
"""
комментарий
в две строки
"""

#типы данных
a = input()
print(type(a))
print(a + '67')
b = int(input())
print(type(b))
print(b + 67)
print(type(67), type(67.0))
print(type(65 // 5))
f = str(678)
print(type(f))
gg = float(f + '00')
print(gg, type(gg))
j = True
print(type(j), type(False))
print(bool(23), bool(0), bool(-564), bool('einfe'), bool(''))
print(None, bool(None))

#Перевод из систем счислений
a = bin(5)
print(a, type(a))
print(f'Печатаю текст, вставляю переменную {90:o} и дальше печатаю')
print('Печатаю текст, вставляю переменную', a, 'и дальше печатаю')
b = f'{5:b}'
print(b, oct(67), hex(789))
print(f'{67:o} {789:x}')
