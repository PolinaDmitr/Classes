def f(x, a):
    return (x % a != 0) <= ((x % 28 == 0) <= (x % 49 != 0))


for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not f(x, a):
            flag = False
            break
    if flag:
        print(a)
