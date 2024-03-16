def f(n):
    n_bin = f'{n:b}'
    if '0' not in n_bin:
        return -1
    for i in range(len(n_bin) - 1, -1, -1):
        if n_bin[i] == '0':
            n_bin = n_bin[:i] + n_bin[:2] + n_bin[i + 1:]
            break
    n_bin = n_bin[::-1]
    return int(n_bin, 2)


for i in range(10_000):
    if f(i) == 123:
        print(i)
        break

