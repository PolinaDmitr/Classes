def f(x, a1, a2):
    return ((a1 <= x <= a2) <= (x ** 2 <= 64)) and ((x ** 2 - 48 <= 2 * x) <= (a1 <= x <= a2))


for a1 in range(-120, 120):
    for a2 in range(a1 + 1, 200):
        flag = True
        for x in range(-200, 300):
            if not f(x, a1, a2):
                flag = False
                break
        if flag:
            print(a1, a2, a2 - a1)