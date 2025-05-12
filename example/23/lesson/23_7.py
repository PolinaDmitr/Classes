# + 3 * 5 * 7  1 -> 1000 (not b after a)

def f(x, y, a):
    if x > y:
        return 0
    if x == y:
        return 1
    if a:
        return f(x + 3, y, True) + f(x * 7, y, False)
    else:
        return f(x + 3, y, True) + f(x * 5, y, False) + f(x * 7, y, False)


print(f(1, 1000, False))