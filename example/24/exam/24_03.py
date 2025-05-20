
with open('24_18029.txt') as file:
    s = file.readline()
    count = 0
    ly = 0
    for l in s.split('X'):
        k = l.count('Y')
        if k > count:
            count = k
            ly = len(l)
        elif k == count:
            ly = min(ly, len(l))
    print(ly + 2) #тк дропнули x
