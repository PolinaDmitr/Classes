from itertools import *
 #1
k = 0
for i in product("0123456", repeat=5):
    s = "".join(i)
    if s[0] == '0':
        continue
    for j in range(len(s) - 2):
        if int(s[j]) % 2 == int(s[j+1]) % 2 and not(int(s[j]) % 2 == int(s[j+1]) % 2 == int(s[j+2]) % 2):
            k += 1
print(k)

 #2
k = 0
for i in product("0123456789", repeat=6):

    s = ''.join(i)
    if s[0] == '0':
        continue
    if int(s) % 4:
        for d in range(len(s) - 1):
            if s[d] % 2 == s[d+1] % 2:


