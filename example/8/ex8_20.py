from itertools import *

k = 0
for i in product('012345678', repeat=5):
    if i[0] != '0' and i.count('5') == 1:
        f = True
        for j in range(4):
            if i[j] == i[j + 1]:
                f = False
        if f:
            k += 1
print(k)

k = 0
for i in product('012345678', repeat=5):
    if i[0] != '0' and i.count('5') == 1 \
        and all(i[j] != i[j + 1] for j in range(4)):
        k += 1
print(k)
