for n in range(6, 36):
    l = 7 ** 500 - 5 * n + 3
    if l % 6 == 0:
        print(n)
        break
