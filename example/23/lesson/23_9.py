# +1 +4 *3  1 -> 180 (krat3 == krat5)


def f(x, y, krat3, krat5):
    if x > y:
        return 0
    if x == y and krat3 == krat5:
        return 1

    if x % 3 == 0:
        krat3 += 1
    if x % 5 == 0:
        krat5 += 1
    
    return f(x + 1, y, krat3, krat5) + f(x + 4, y, krat3, krat5) + f(x * 3, y, krat3, krat5)



s = f(1, 180, 0, 0)
print(s)
print(sum(int(x) for x in str(s)))
