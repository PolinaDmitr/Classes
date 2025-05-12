# +1 +3 * 2 *3  1 -> 9999


def f(x, y, c):
    if x > y:
        return 0
    if x == y:
        return 1

    if c:
        return f(x * 2, y, False) + f(x * 3, y, False)
    else:
        return f(x + 1, y, True) + f(x + 3, y, True)


print(f(1, 9999, True) + f(1, 9999, False))