from itertools import *

#1

k = 0
for i in product("кон", repeat=5):
    s = ''.join(i)
    k+=1

k1 = 0
for i in product("конец", repeat=5):
    s = ''.join(i)
    k1+=1



k2 = 0
for i in product("дракон", repeat=5):
    s = ''.join(i)
    k2+=1

print('1:', (k1-k)+(k2-k))

#5

k = 0
for i in set(permutations("makaka")):
    s = "".join(i)
    # valid = True
    # for j in range(len(s) - 1):
    #     if s[j] == s[j+1]:
    #         valid = False
    #         break
    # if valid:
    #     k += 1
    if not 'aa' in s and not 'kk' in s:
        k += 1
print('5:', k)

#6
k = 0
for i in permutations("0123456789", 7):
    s = ''.join(i)
    valid = True
    if int(s[0]) == 0:
        valid = False
        continue
    for j in range(len(s) - 1):
        if int(s[j]) % 2 == int(s[j+1]) % 2:
            valid = False
            break
    if valid:
        k += 1
print('6:', k)


#7

k = 0
for i in product("ящер", repeat=5):
    s = ''.join(i)
    if  0 < s.count("е") <= 3:
        k += 1
print('7', k)

#8


def ubivanie(num_str):
    for i in range(1, len(num_str)):
        prev = int(num_str[i-1], 16)
        curr = int(num_str[i], 16)
        if prev <= curr:
            return False
    return True

k1 = 0
for i in permutations('0123456789ABCDEF', 3):
    s = ''.join(i)
    if s[0] == '0':
        continue

    if s[0] != '0' and ubivanie(s):
        k1 += 1

k2 = 0
for i in permutations('0123456789ABCDEF', 5):
    s = ''.join(i)
    if s[0] == '0':
        continue

    if s[0] != '0' and ubivanie(s):
        k2 += 1

print('8:', k1 + k2)


#9

k = 0
for i in product('012345678', repeat=5):
    s = ''.join(i)
    if s[0] == '0':
        continue
    if s.count('5') == 1:
        # f = True
        # for j in range(len(s) - 1):
        #     if s[j] == s[j + 1]:
        #         f = False
        # if f:
        #     k += 1
        if all(s[j] != s[j + 1] for j in range(4)):
            k += 1
print('9:', k)

#10

k = 0
for i in product('01234567', repeat=7):
    s = ''.join(i)
    if s[0] == '0':
        continue

    even_count = 0
    for digit in s:
        if int(digit) % 2 == 0:
            even_count += 1

    if even_count == 2:
        valid = True
        for j in range(len(s) - 1):
            if (int(s[j]) % 2 != 0 and s[j + 1] == '7') or (s[j] == '7' and int(s[j + 1]) % 2 != 0):
                valid = False
                break

        if valid:
            k += 1

print('10:', k)



