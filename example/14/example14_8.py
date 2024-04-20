for p in range(10, 100):
    for x in range(p):
        for y in range(p):
            numb1 = 2 * (p ** 3) + 4 * (p ** 2) + x * p + 9 + y * (p ** 3) + \
                x * (p ** 2) + y * p + 3
            numb2 = x * (p ** 3) + 4 * (p ** 2) + y * p + 0
            if numb1 == numb2:
                print(p, x, y, x * (p ** 2) + y * p + y)