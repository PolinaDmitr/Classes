from math import prod

l = '4' * 10 + '<'
while '4' in l:
    l = l.replace('4', '5', 1)
l = l.replace('<', '')
print(l)
print(prod(int(i) for i in l))

l = '1' * 10 + '<'
while '11' in l:
    l = l.replace('11', '9', 1)
l = l.replace('<', '')
print(l)
print(prod(int(i) for i in l))

l = '0' * 10 + '<'
while '00' in l:
    l = l.replace('00', '92', 1)
l = l.replace('<', '')
print(l)
print(prod(int(i) for i in l))