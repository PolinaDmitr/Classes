def f(x, a):
    return ((x % a == 0) and (x % 16 == 0)) <= ((x % 16 != 0) or (x % 24 == 0))


for a in range(1, 200):
    flag = True
    for x in range(1, 10000):
        if not f(x, a):
            flag = False
            break
    if flag:
        print(a)