#одна куча, +1, *2, *3, больше/равно 36, но меньше/равно 60

from functools import lru_cache

def step(s):
    return s + 1, s * 2, s * 3


@lru_cache(None)
def game(s):
    if s > 60:
        return 'P1' #выигрывает оппонент (то есть через ход, потому что я уже проиграл)
    if s >= 36:
        return 'W'
    if any(game(m) == 'W' for m in step(s)):
        return 'P1'
    if all(game(m) == 'P1' for m in step(s)):
        return 'V1'
    if any(game(m) == 'V1' for m in step(s)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in step(s)):
        return 'V2'


for h in range(1, 36):
    if game(h) == 'V1':
        print(h, game(h))

for h in range(1, 36):
    if game(h) == 'P2':
        print(h, game(h))

for h in range(1, 36):
    if game(h) == 'V2':
        print(h, game(h))