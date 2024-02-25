from string import digits, ascii_uppercase


def f(x):
    for i in range(1, 11):
        print(x, '*', i, '=', x * i)


def h():
    a = 56 * 93534
    b = 6739823 - 238974932 + 384
    return a, b


def lll(x):
    return x ** x + 10


def f_bin(x):
    string = ""
    while x != 0:
        ost = x % 2
        string = str(ost) + string
        x = x // 2
    return string


def f_12(x):
    string = ""
    alpha = digits + ascii_uppercase
    while x != 0:
        ost = x % 12
        string = alpha[ost] + string
        x = x // 12
    return string


print('Наш код')
f(5)
print()
f(8)
print(h())
print(lll(7), 7 ** 7)
print(f_bin(5))
print(f_12(35))
print(digits, ascii_uppercase)
