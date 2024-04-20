for x in range(110, -1, -1):
    number = x * (111 ** 3) + 3 * (111 ** 2) + 2 * 111 + 1 + \
        1 * (211 ** 3) + 7 * (211 ** 2) + x * 211 + 4

    if number % 111 == 0:
        print(x, number / 111)