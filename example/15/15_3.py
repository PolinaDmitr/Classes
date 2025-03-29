def f(a, x):
    return (x % 18 == 0) <= ((x % a != 0) <= (x % 12 != 0))


for a in range(100, 0, -1):
    flag = True
    for x in range(1000):
        if not f(a, x):
            flag = False
            break

    if flag:
        print(a)
        break