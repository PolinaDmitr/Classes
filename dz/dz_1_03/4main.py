from itertools import  product
k = 0
for i in product([i for i in range(25)],repeat = 4):
    if i[0] == 0:
        continue
    if sum(j % 2 for j in i) == 3 and sum(1 for j in i if j > 15) <= 2:
        k += 1
print(k)

k = 0
for i in product([i for i in range(25)],repeat = 4):
    if i[0] == 0:
        continue
    c = 0
    for j in i:
        if j % 2 == 0:
            c += 1
    if c != 1:
        continue
    c = 0
    for j in i:
        if j > 15:
            c += 1
    if c <= 2:
        k += 1
print(k)