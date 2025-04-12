#одна куча, уменьшение, // 3, -10, не более 20 1) есть неудачный ход Пети

from functools import lru_cache

def step(h):
    x, last = h
    a = []
    if x != '+1':
        a.append((x + 1, '+1'))
    if x != '*2':
        a.append((x * 2, '*2'))
    if x != '*3':
        a.append((x * 3))


@lru_cache(None)
def game(h):
    if h >= 140:
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