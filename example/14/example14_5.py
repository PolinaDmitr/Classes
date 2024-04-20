for p in range(10, 50):
    for x in range(0, p):
        for y in range(0, p):
            numb1 = 3 * (p ** 3) + 4 * (p ** 2) + x * p + 5 + x * (p ** 3) + 9 * (p ** 2) + \
                x * p + 3
            numb2 = y * (p ** 3) + y * (p ** 2) + 6 * p + 8

            if numb2 == numb1:
                print(p, x, y)
                print(y * (p ** 3) + x * (p ** 2) + x * p + y)