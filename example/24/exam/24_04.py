from re import *

s = open('24_22359.txt').readline() #будто бы не хочется так
reg = r'[1-9A-E][0-9A-E]+[05A]'
# m = max((x.group() for x in finditer(reg,s)),key=lambda x: int(x,15))
c = 0
m = ''
for i in finditer(reg,s):
    x = i.group()   #что делает
    a = int(x, 15)
    if a > c:
        c = a
        m = x

print(s.find(m)+len(m)-1)