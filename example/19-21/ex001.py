from functools import lru_cache

def step(h):
    return h + 1, h * 2


@lru_cache(None)
def game(h):
    if h >= 29:
        return 'W'
    if any(game(m) == 'W' for m in step(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in step(h)):
        return 'V1'
    if any(game(m) == 'V1' for m in step(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in step(h)):
        return 'V2'


for s in range(1, 29):
    if game(s) == 'V1':
        print('V1', s)

for s in range(1, 29):
    if game(s) == 'P2':
        print('P2', s)

for s in range(1, 29):
    if game(s) == 'V2':
        print('V2', s)
