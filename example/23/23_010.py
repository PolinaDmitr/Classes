#нет двух подряд идущих команд

def f(x, y, c):
    if x > y:
        return 0
    if x == y:
        return 1
    if not c:
        return f(x + 1, y, not c) + f(x + 3, y, not c)
    return f(x * 2, y, not c) + f(x * 3, y, not c)


print(f(1, 9999, True) + f(1, 9999, False))


#можно типо с переключателем

def f1(x, y, c):
    if x > y:
        return 0
    if x == y:
        return 1
    count = 0
    if c != 1:
        count += f1(x + 1, y, 1) + f1(x + 3, y, 1)
    if c != 2:
        count += f1(x * 2, y, 2) + f1(x * 3, y, 2)
    return count


#тип в первый раз будет сумма общая
print(f1(1, 9999, 0))

