from itertools import  product
k = 0
for i in product('0123456789AB',repeat = 5):
    s = ''.join(i)
    if s [0]!= '0'and s.count('7')==1 and s.count('9')+s.count('b')<=3:
        k += 1
print(k)