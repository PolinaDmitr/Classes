l = []
for i in range(100100):
    n = f'{i:o}'
    if len(n) == 5 and n[0] == '4' and n.count('7') == 2:
        l.append(n)
l.sort()
print(l)
print(int(l[-1], 8))