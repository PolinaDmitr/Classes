from functools import cache


def step(h):
    return h - 2, h // 2

@cache
def game(s):
    if s <= 87:
        return 'W'
    if any(game(m) == 'W' for m in step(s)):
        return 'P1'
    if all(game(m) == 'P1' for m in step(s)):
        return 'V1'
    if any(game(m) == 'V1' for m in step(s)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in step(s)):
        return 'V2'

for i in range(88, 200):
    if game(i) == 'V1':
        print('19:', i)
        break


for i in range(88, 300):
    if game(i) == 'P2':
        print(game(i), i)

for i in range(88, 300):
    if game(i) == 'V2':
        print(game(i), i)
