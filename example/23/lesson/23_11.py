# +1 +3 * 2 *3  1 -> 9999


def f(x, y, c):
    if x > y:
        return 0
    if x == y:
        return 1
    count = 0
    if c != '1':
        count += f(x * 2, y, '1') + f(x * 3, y, '1')
    if c != '2':
        count += f(x + 1, y, '2') + f(x + 3, y, '2')
    return count


print(f(1, 9999, '0'))