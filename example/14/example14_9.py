for x in range(39):
    for y in range(39):
        numb = 5 * (39 ** 8) + 8 * (39 ** 7) + x * (39 ** 6) + 7 * (39 ** 5) + \
            2 * (39 ** 4) + 3 * (39 ** 3) + y * (39 ** 2) + 4 * 39 + 9
        yx = (y * 39 + x)
        yx2 = yx ** 0.5
        if (numb % 38 == 0) and (yx2 == int(yx2)):
            print(x, y, yx)