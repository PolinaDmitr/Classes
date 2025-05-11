from functools import cache


def step(h):
    a, b = h
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)

@cache
def game(s):
    a, b = s
    if a + b >= 81:
        return 'W'
    if any(game(m) == 'W' for m in step(s)):
        return 'P1'
    if all(game(m) == 'P1' for m in step(s)):
        return 'V1'
    if any(game(m) == 'V1' for m in step(s)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in step(s)):
        return 'V2'


a = 7
# for i in range(1, 73):
#     h = (a, i)
#     if game(h) == 'V1':
#         print('19', i)


for i in range(1, 73):
    g = (a, i)
    if game(g) == 'P2':
        print(game(g), i)

for i in range(1, 73):
    g = (a, i)
    if game(g) == 'V2':
        print(game(g), i)
