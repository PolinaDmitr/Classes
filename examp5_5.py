def f(n):
    n_bin = f'{n:b}'
    n_sum = 0
    for i in n_bin:
        n_sum += int(i)

    if n_sum % 2 == 0:
        n_bin = n_bin[1:]
    else:
        n_bin = '1' + n_bin + '00'

    n_sum = 0
    for i in n_bin:
        n_sum += int(i)

    if n_sum % 2 == 0:
        n_bin = n_bin[1:]
    else:
        n_bin = '1' + n_bin + '00'
    return int(n_bin, 2)


for n in range(11, 10_000):
    r = f(n)
    if r > 100:
        print(n, r)
        break

