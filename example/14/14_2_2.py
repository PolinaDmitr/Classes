for p in range(1001, 10000):
    if p % 10 == 0:
        continue
    q = int(str(p)[::-1])
    n1 = p + 4 * p + 4 * p ** 2
    n2 = 4 + 4 * q + q ** 2
    if n1 == n2:
        print(p, q)