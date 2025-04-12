from functools import lru_cache

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


@lru_cache(None)
def game(h):
    a, b = h
    if a + b <= 100:
        return 'W'
    if any(game(m) == 'W' for m in step(h)):
        return 'P1'
    if any(game(m) == 'P1' for m in step(h)):
        return 'V1'
    if any(game(m) == 'V1' for m in step(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in step(h)):
        return 'V2'


for s in range(53,500):
    h = (48, s)
    if game(h) == 'V1':
        print(game(h), s)

# for s in range(52, 500):
#     h = (48, s)
#     if game(h) == 'P2':
#         print(game(h), s)
#
# for s in range(52, 500):
#     h = (48, s)
#     if game(h) == 'V2':
#         print(game(h), s)