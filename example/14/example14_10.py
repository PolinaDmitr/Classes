def f5(x):
    s = ''
    while x > 0:
        s = str(x % 5) + s
        x = x // 5
    return s


numb5_50 = 5 ** 50
numb5_30 = 5 ** 30
for x in range(1, 50):
    for y in range(1, 50):
        numb = numb5_50 + numb5_30 - 5 ** x - y - 5 ** y - x
        numb_5 = f5(numb)
        if numb_5.count('0') == 10:
            print(x, y, numb_5, x * y)
