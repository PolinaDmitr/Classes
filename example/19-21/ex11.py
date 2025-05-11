from functools import cache
# from sys import *
# setrecursionlimit(3000)


def step(h):
    a, b = h
    l = []
    if a - 3 > 0 and b - 3 > 0:
        l.append((a - 3, b - 3))
    if a // 2 > 0:
        l.append((a // 2, b))
    if b // 2 > 0:
        l.append((a, b // 2))
    return l

@cache
def game(s):
    print(s)
    a, b = s
    if a + b <= 100:
        return 'W'
    if any(game(m) == 'W' for m in step(s)):
        return 'P1'
    if any(game(m) == 'P1' for m in step(s)):
        return 'V1'
    if any(game(m) == 'V1' for m in step(s)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in step(s)):
        return 'V2'


a = 48
# for i in range(53, 300):
#     h = (a, i)
#     if game(h) == 'V1':
#         print('19', i)
# print(game((a, 107)))


# for i in range(53, 400):
#     g = (a, i)
#     if game(g) == 'P2':
#         print(game(g), i)
# #
# for i in range(53, 400):
#     g = (a, i)
#     if game(g) == 'V2':
#         print(game(g), i)
