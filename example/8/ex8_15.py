from itertools import *

c = 0
for a1 in (2, 4, 6, 8, 10, 12, 14, 16, 18):
    for a2 in (1, 3, 5, 7, 9, 11, 13, 15, 17, 19):
        for a3 in (0, 2, 4, 6, 8, 10, 12, 14, 16, 18):
            for a4 in (1, 3, 5, 7, 9, 11, 13, 15, 17, 19):
                for a5 in (0, 2, 4, 6, 8, 10, 12, 14, 16, 18):
                    if a1 + a5 == 26:
                        c += 1

for a1 in (1, 3, 5, 7, 9, 11, 13, 15, 17, 19):
    for a2 in (0, 2, 4, 6, 8, 10, 12, 14, 16, 18):
        for a3 in (1, 3, 5, 7, 9, 11, 13, 15, 17, 19):
            for a4 in (0, 2, 4, 6, 8, 10, 12, 14, 16, 18):
                for a5 in (1, 3, 5, 7, 9, 11, 13, 15, 17, 19):
                    if a1 + a5 == 26:
                        c += 1

print(c)

#второй вариант

k = 0
for i in product([y for y in range(20)], repeat=5):
    if i[0] != 0 and all(i[j] % 2 != i[j + 1] % 2 for j in range(4)) and i[0] + i[4] == 26:
        k += 1
print(k)