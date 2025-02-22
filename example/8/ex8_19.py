from itertools import *

#all()
#долгое решение
k = 0
for i in product('12345678', repeat=9):
    if all(int(i[j]) % 2 != int(i[j + 1]) % 2 for j in range(8))\
            and not any(i.count(j) > 3 for j in i):
        k += 1
        print(i)
print(k)