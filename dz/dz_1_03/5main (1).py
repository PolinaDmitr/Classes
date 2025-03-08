from itertools import  product
k = 0
for i in product('ДИОНСЙ',repeat = 6):
    s = ''.join(i)
    if('Д'in s and'Н' not in s) or ('Н'in s and'Д' not in s):
        if all([s[q] != s [q + 1] for q in range (0,len(s) - 1)]):
            k += 1
print(k)