from itertools import *


k = 0
for i in permutations("0123456789", 6):
    s = ''.join(i)
    if s[0]== "0":
        continue
    if int(s) % 4 != 0:
        continue
    valid = True

    for p in range(5):
        if int(i[p]) % 2 == 0 and int(i[p+1]) % 2 == 0:
            valid = False
            break
    if valid:
        k+=1
print(k)



unique_codes = set()
glas = set("АИ")
for p in permutations('ПАРИЖАНКА'):
    s = "".join(p)
    cnt = 0
    for i in range(len(s) - 1):
        if s[i] in glas and s[i+1] in glas:
            cnt += 1
    if cnt == 1:
        unique_codes.add(s)

print(len(unique_codes))




counter = 0
for i in product(range(25), repeat=4):
    if i[0] == 0:
        continue

    even_count = sum(1 for d in i if d % 2 == 0)
    if even_count != 1:
        continue

    big_count = sum(1 for d in i if d > 15)
    if big_count > 2:
        continue

    counter += 1

print(counter)



k = 0
for i in set(product("ДИОНИСИЙ", repeat=6)):
    s = ''.join(i)
    if ('Д' in s) ^ ('Н' in s):
        if all(s[i] != s[i + 1] for i in range(len(s) - 1)):
            k += 1
print(k)


import itertools

def is_six_digit(n):
    return 100000 <= n <= 999999

max_k = None
chain_count_for_max_k = None


for k in range(1, 20):

    count = sum(1 for _ in combinations(range(20), k))
    if is_six_digit(count):
        max_k = k
        chain_count_for_max_k = count

print(chain_count_for_max_k)

k=0
for i in product(range(12), repeat=6):
    if i[0] == 0:
        continue
    if i.count(11) != 1:
        continue
    cnt = 0
    for p in i:
        if p % 2 == 0:
            cnt += 1
    nechet = 6 - cnt
    if cnt == nechet:
        k+=1

print(k)







