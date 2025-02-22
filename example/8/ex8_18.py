from itertools import *

k = 0
for i in set(permutations('kidala', 5)):
    s = ''.join(i)
    if s.count('aa') == 0:
        k += 1
print(k)
