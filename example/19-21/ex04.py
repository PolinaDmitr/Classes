#одна куча, уменьшение, // 3, -10, не более 20 1) есть неудачный ход Пети

from functools import lru_cache

def step(h):
    a = []
    if h // 3 > 0:
        a.append(h // 3)
    if h - 10 > 0:
        a.append(h - 10)
    return a


@lru_cache(None)
def game(h):
    if h <= 10:
        return 'W'
    if any(game(m) == 'W' for m in step(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in step(h)):
    # if any(game(m) == 'P1' for m in step(h)):
        return 'V1'
    if any(game(m) == 'V1' for m in step(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in step(h)):
        return 'V2'


count = 0
for s in range(11, 200):
    if game(s) == 'V2':
        print(game(s), s)
        count+=1
print(count)