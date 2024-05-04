def f(x, a):
    return (x & 29 != 0) <= ((x & 17 == 0) <= (x & a != 0))


for a in range(1, 100):
    flag = True
    for x in range(1, 2000):
        if not f(x, a):
            flag = False
            break
    if flag:
        print(a)