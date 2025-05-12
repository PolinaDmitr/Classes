# -1 +2 *2  3 -> 40 (30, not 20), нельзя 2 раза подряд команду А, нельзя 2 раза перейти конечное число

def f(x, y, a, k, has30):
    if (x > y and k >= 2) or x == 20:
        return 0
    if x == y and k < 2 and has30:
        return 1
    if x > y:
        k += 1
    if x == 30:
        has30 = True
    if a:
        return f(x + 2, y, False, k, has30) + f(x * 2, y, False, k, has30)
    else:
        return f(x - 1, y, True, k, has30) + f(x + 2, y, False, k, has30) + f(x * 2, y, False, k, has30)


print(f(3, 40, False, 0, False))