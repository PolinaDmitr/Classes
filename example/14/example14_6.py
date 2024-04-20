def f(x):
    s = ""
    while x > 0:
        s = str(x % 5) + s
        x = x // 5
    return s


for x in range(4, 10):
    number = (4 * (26 ** 3) + x * (26 ** 2) + 11 * 26 + 5) * \
             (2 * ((x + 1) ** 2) + x * (x + 1) + 3)
    numb_5 = f(number)
    summ = 0
    for i in numb_5:
        summ = summ + int(i)
    if summ == 19:
        print(numb_5, x, numb_5.count('4'), number)
