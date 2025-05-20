def f(x, k, c):
    print(k, '->', x)
    c.append(x)
    k += 1
    if k > 5:
        c.sort()
        print(c)
        return 1
    return f(x + 1, k, c) + f(x * 2, k, c)

f(3, 0, [])