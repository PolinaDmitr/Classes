l = '1' * 2019 + '3' * 2119

while '11' in l:
    l = l.replace('11', '2', 1)
    l = l.replace('22', '3', 1)
    l = l.replace('33', '1', 1)
print(l)
