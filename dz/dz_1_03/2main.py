from itertools import  product
k = 0
for i in product('01234',repeat = 9):
    s = ''.join(i)
    if s[0] != '0':
        s = s.replace('0','*').replace('2','*').replace('4','*')
        if s.count('**') == 2 and '***' not in s:
            k += 1
            print(k,s)