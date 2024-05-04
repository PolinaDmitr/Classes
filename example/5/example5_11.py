def f(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x //= 3
    return s


def algo(n):
    n_3 = f(n)
    if n % 7 == 0:
        n_3 = n_3 + n_3[-2:]
    else:
        n_ost = f((n % 7) * 3)
        n_3 = n_3 + n_ost
    return int(n_3, 3)

l = []
for n in range(1, 1000):
    r = algo(n)
    if 369 < r:
        l.append(r)

print(min(l))
