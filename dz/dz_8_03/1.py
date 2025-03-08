from  itertools import *

k=5**5 + 6**5 - 2*3**5
print(k)
#10)
k =0
l = ('71', '17', '37', '73', '57', '75', '77')
for i in product('01234567', repeat = 7):
    num = ''.join(i)
    if num [0] != '0':
        if len ([x for x in num if x in '02468'])==2:
            if all (not p in l for p in num):
                k +=1
print(k)
#9)
k = 0
alp = '012345678'
for i in product(alp, repeat=5):    
    s = ''.join(i)
    if s[0] != s[1] and s[1] != s[2] and s[2] != s[3] and s[3] != s[4]:
        break
    k +=1
    print (k)
    
#8)

from itertools import product 
alp = '0123456789ABCDEF'
a=[]
for i in product(alp, repeat=6):    
    if i[0] > i[1] > i[2] > i[3]> i[4]> i[5]:
        a.append(i)
print(len(a))

from itertools import product 
alp = '0123456789ABCDEF'
a=[]
for i in product(alp, repeat=6):    
    if i[0] > i[1] > i[2] > i[3]:
        a.append(i)
print(len(a))