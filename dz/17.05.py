from functools import lru_cache


def f(x,y):
    if x > y or x == 8:
        return 0

    if x == y:
        return 1

    return f(x+1, y) + f(x+2,y)+f(x*2,y)

print(f(3,14)*f(14,18))





def f(x,y):
    if x > y or x == 56:
        return 0

    if x == y:
        return 1

    return f(x+3, y) + f(x+7,y)+f(x*3,y)

print(f(12,40)*f(40,72)*f(72,89))



def f(x,y,a):
    if x > 36 or x < 0:
        return 0

    if x == y:
        return 1
    res = 0
    if a < 2:
        res += f(x - 1, y, a+1)

    res += f(x+5,y,0)+f(x*2,y,0)



    return res

print(f(5,34,0))




def f(x,y):
    if x == y:
        return 1

    if x < y or x == 24:
        return 0

    res = 0

    res = f(x-1,y)+f(int(x**0.5),y)
    if x > 9:
        res += f(int(str(x)[:-1]),y)
    return res


print(f(602,7))



def f(x,y):
    if x < y or x == 28:
        return 0

    if x == y:
        return 1
    res = 0
    res += f(x-2,y)
    if x % 2 == 0:
        res += f(x // 2, y)
    else:
        res += f(x - 3, y)
    return res

print(f(98,1))



def chet_custom(n):
    if n % 2 == 0:
        return n // 2
    else:
        return n - 7

def f(x: int,y:int=1,last:str='', c: int=0):
    if x < y:
        return 0

    if x == y:
        return 1

    res = 0
    if not (last == 'A' and c == 2):
        res += f(x - 2,y,'A', c + 1 if last == 'A' else 1)

    if not (last == 'B' and c == 2):
        res += f(chet_custom(x),y, 'B', c + 1 if last == 'B' else 1)
    return res


print(f(40,1))




def f(x,y,has20,has30):

    if x == y:
        return 1


    if x > y:
        return 0

    if has20 and has30:
        return 0

    new20 = has20 or (x == 20)
    new30 = has30 or (x == 30)

    return f(x + 2, y, new20, new30) + f(x + 3, y, new20, new30) + f(x * 2, y, new20, new30)


print(f(8,35,False,False))





def max_digit(n: int) -> int:
    return max(int(d) for d in str(n))


def f(x: int, y: int, has24: bool) -> int:
    if x == y:
        return 1 if has24 else 0

    if x > y:
        return 0

    new24 = has24 or (x == 24)

    return f(x + 3, y, new24) + f(x + max_digit(x), y, new24)


print(f(10, 41, False))














