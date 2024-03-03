def f(n):
    n_bin = f'{n:b}'
    n_sum = 0
    for i in n_bin:
        n_sum += int(i)
    if n_sum % 2 == 0:
        n_bin = n_bin + '0'
        n_bin = '10' + n_bin[2:]
    else:
        n_bin = n_bin + '1'
        n_bin = '11' + n_bin[2:]
    return int(n_bin, 2)


# стрезы в строке
s = '0123456789'
print(s)
print(s[:5], s[2:], s[2:6], s[0])
print(s, s[::-1], s[-1], s[len(s) - 1], s[::2])

for n in range(10_000):
    r = f(n)
    if r > 40:
        print(n, r)
        break

