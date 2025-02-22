from itertools import *

for i in product('12345', repeat=3):
    print(i)
    s = ' '.join(i)
    print(s)
#аналогия
print()
for a1 in '12345':
    for a2 in '12345':
        for a3 in '12345':
            print(a1 + a2 + a3)

print('-------------')
for i in combinations('1234', 3):
    print(i)

print('--------')
for i in combinations_with_replacement('1234', 3):
    print(i)

print('------')
for i in product('ABC', '123', repeat=2):
    print(i)
#аналогия
for i in 'ABC':
    for j in '123':
        print(i, j)

print('------')
k = 0
for i in permutations('ABCD'):
    print(''.join(i))
    k += 1
print(k)
k = 0
for i in set(permutations('ABCA')):
    print(''.join(i))
    k += 1
print(k)

#множество
s = set()
s.add('4')
print(s)
s.add('4')
print(s)

for i in permutations('ABCD', 2):
    print(''.join(i))