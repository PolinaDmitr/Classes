def f(x, n):
    return ((x < 32 or x > 46) <= (x < 27 or x > 54)) and ((x < n or x > 70) <= (32 <= x <= 46))


for n in range(-100, 70):
    count = 0
    for x in range(-101, 75):
        if f(x, n):
            count += 1
    if count > 25:
        print(n)
