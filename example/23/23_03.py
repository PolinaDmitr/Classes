# +1, +7, не содержит цифру 7

def f(x, y):
    if x > y or '7' in str(x):
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x +7, y)


print(f(1, 61))