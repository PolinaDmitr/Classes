l = set()
for x in range(10, 67):
    for y in range(0, x):
        number = 7 * (67 ** 4) + 3 * (67 ** 3) + x * (67 ** 2) + 67 + y + 4 * (x ** 3) + 9 * (x ** 2) + \
            y * x + 6
        l.add(number)
print(len(l))