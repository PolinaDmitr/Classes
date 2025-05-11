from functools import cache

@cache
def f(n):
    if n < 20:
        return n
    return (n - 6) * f(n - 7)

#прогреть кэш
for i in range(47900):
    f(i)

print((f(47872) - 290 * f(47865))/f(47858))