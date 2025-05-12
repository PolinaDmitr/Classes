#что-то интересное с двоичными числами (обнулить разряды)

def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    if bin(x).count('1') == 1:
        return f(x - 1, y)
    return f(x - 1, y) + f(int('1' + bin(x)[3:].replace('1', '0'), 2), y)


print(f(int('10001', 2), 1))