def f(n):
    n_bin = f'{n:b}' #bin() -> 0b11
    if n % 2 != 0:
        n_bin = '1' + n_bin + '0'
    else:
        n_bin = '11' + n_bin + '11'
    n_dec = int(n_bin, 2)
    return n_dec


def f1(n):
    n_bin = f'{n:b}' #bin() -> 0b11
    if n % 2 != 0:
        n_bin = '10' + n_bin + '11'
    else:
        n_bin = '1' + n_bin + '00'
    n_dec = int(n_bin, 2)
    return n_dec


def invert(x):
    string = "1"
    for i in range(1, len(x)):
        if x[i] == '1':
            string = string + '0'
        else:
            string = string + '1'
    return string


def f2(n):
    n_bin = f'{n:b}'
    n_inv = invert(n_bin)
    return n + int(n_inv, 2)


result = 0
for n in range(100_000):
    a = f(n)
    if result < a < 126:
        result = a
print(result)

result = 100_000
for n in range(100_000):
    a = f1(n)
    if 1023 < a < result:
        result = a
print(result)

for n in range(1, 10_000, 2):
    result = f2(n)
    if result > 99:
        print(n)
        break


