# + 1 + 4 * 2   1 -> 50 (8/16/32)

def f(x, y, c):
    if x > y or (x in (8, 16, 32) and c):
        return 0
    if x in (8, 16, 32):
        c = True
    if x == y and c:
        return 1
    return f(x + 1, y, c) + f(x + 4, y, c) + f(x * 2, y, c)


print(f(1, 50, False))