#ограниченное количество команд

def f(x, y, c):
    if x == y and c == 6:
        return 1
    if x > y:
        return 0
    return f(x + 1, y, c + 1) + f(x + 2, y, c + 1) + f(x * 2, y, c + 1)


print(f(1, 20, 0))