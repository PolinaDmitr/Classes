from itertools import  product
k = 0
for i in product(range(12), repeat = 6):
    if i[0] > 0 and i.count(11) ==1 and  sum (j % 2 for j in i) == 3:
        k +=1
print(k)