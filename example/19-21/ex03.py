#две кучи, +1, *2, больше/равно 83 1) есть неудачный ход Пети

from functools import lru_cache

def step(h):
    a, b = h
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)


@lru_cache(None)
def game(h):
    a, b = h
    if a + b >= 83:
        return 'W'
    if any(game(m) == 'W' for m in step(h)):
        return 'P1'
    # if any(game(m) == 'P1' for m in step(h)):   #если говорится про неудачный ход Пети
    if all(game(m) == 'P1' for m in step(h)):
        return 'V1'
    if any(game(m) == 'V1' for m in step(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in step(h)):
        return 'V2'


for s in range(1, 74):
    h = (9, s)
    if game(h) == 'V2':
        print(game(h), s)