for x in range(0, 9):
    for y in range(0, 9):
        number = 8 * (9 ** 4) + 8 * (9 ** 3) + x * (9 ** 2) + 4 * 9 + y \
            + 7 * (11 ** 4) + x * (11 ** 3) + 4 * (11 ** 2) + 4 * 9 + y
        if number % 61 == 0:
            print(x, y, number / 61)
