def f(a, x, y, z):
    return (a < x) or (a < y) or (a < z) or (48 != y + 2 * x + z)


for a in range(48, 0, -1):
    flag = True
    for x in range(100):
        for y in range(100):
            for z in range(100):
                if not f(a, x, y, z):
                    flag = False
                    break
            if not flag:
                break
        if not flag:
            break

    if flag:
            print(a)
            break