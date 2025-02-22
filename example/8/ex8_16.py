from itertools import *

k = 0
for i in set(permutations('кидала', r=5)):
    s = ''.join(i)
    if s.count('а') == 1:
        k += 1
    elif s.count('аа') == 0:
        k += 1
print(k)

k = 0
for i in permutations('kaif'):
    s = ''.join(i)
    if s[-1] != 'i' and s.count('kf') == 0:
        k += 1
print(k)