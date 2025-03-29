def f(x, y, a):
    return (x > a) or (y > a) or (x + 2 * y < 80)


for a in range(30, 20, -1):
    print(a)
    flag = True
    for x in range(0, 10000):
        for y in range(0, 10000):
            if not f(x, y, a):
                flag = False
                break
        if not flag:
            break
    if flag:
        print('yes', a)
        break