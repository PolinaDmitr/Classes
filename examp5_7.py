def f(n):
    n_str = str(n)[::-1]
    s1 = 0
    for i in n_str:
        if i in '02468':
            s1 += int(i)
    s2 = 0
    for i in range(0, len(n_str), 2):
        s2 += int(n_str[i])

    return abs(s1 - s2)


for n in range(10_000_000):
    result = f(n)
    if result == 26:
        print(n)
        break

# задание 7
print('решение из разборов')
for n in range(1,100000000):
    s = str(n) [::-1]
    s1 = sum([int(i) for i in s if int(i) % 2 == 0])
    s2 = sum([int(s[i]) for i in range(0, len(s), 2)])
    if abs(s1 - s2) == 26:
        print(n)
        break