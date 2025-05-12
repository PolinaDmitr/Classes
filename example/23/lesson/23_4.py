# +1 +2 +3   5 -> (7) -> 11

def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y) + f(x + 3, y)


print(f(5, 7) * f(7, 11))