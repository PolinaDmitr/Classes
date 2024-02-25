def f(n):
    n_bin = f'{n:b}'
    if n % 3 == 0:
        n_bin = n_bin.replace('0', '11')
    else:
        n_bin = n_bin.replace('1', '10')
    return int(n_bin, 2)


res = 0
for n in range(1000_000):
    a = f(n)
    if res < a <= 161:
        res = a
print(res)