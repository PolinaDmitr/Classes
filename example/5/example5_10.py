def f(n):
    n_bin = f'{n:b}'
    n_bin2 = n_bin + n_bin[-1]
    if n_bin2.count('1') % 2 == 0:
        n_bin2 = n_bin2 + '0'
    else:
        n_bin2 = n_bin2 + '1'

    if n_bin2.count('1') % 2 == 0:
        n_bin2 = n_bin2 + '0'
    else:
        n_bin2 = n_bin2 + '1'
    return int(n_bin2, 2)


r_min = 1000
for n in range(1000):
    r = f(n)
    if 114 < r < r_min:
        r_min = r
print(r_min)