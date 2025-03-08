from itertools import permutations
k = 0
for i in set(permutations ('ПАРИЖАНКА')):
    s = ''.join(i)
    s = s.replace('И','А')
    if not 'ААА' in s and s.count('АА') == 1:
        k += 1
print(k)