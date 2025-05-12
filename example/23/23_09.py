#больше умножения, чем сложения (возьмём одну переменную для этого)

def f(x, y, k):
    if x > y:
        return 0
    if x == y:
        return 1 if k > 0 else 0
    return f(x + 1, y, k - 1) + f(x * 2, y, k + 1) + f(x * 3, y, k + 1)


print(f(1, 157, 0))