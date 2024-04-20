def f(a, x, y, z):
    return (48 != y + 2 * x + z) or (a < x) or (a < y) or (a < z)

for a in range(100):
    flag = True
    for x in range(70):
        for y in range(70):
            for z in range(70):
                if not f(a, x, y, z):
                    flag = False
                    break

    if flag:
        print(a)
