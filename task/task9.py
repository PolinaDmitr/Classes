
a = set()
for n in range(4, 10_000):
    s = '7' + '6' * n
    while '766' in s or '667' in s:
        s = s.replace('766', '67', 1)
        s = s.replace('667', '7', 1)
    a.add(s)
print(len(a))
