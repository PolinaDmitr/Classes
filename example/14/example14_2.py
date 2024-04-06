def f(x):
    result = ''
    while x > 0:
        result = str(x % 7) + result
        x //= 7
    return result


number = 49 ** 12 - 7 ** 10 + 7 ** 8 - 49
l = f(number)
print(l.count('6'))