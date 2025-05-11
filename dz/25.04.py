from functools import lru_cache


def step(n):
    return n + 1, n + 4, n * 2

@lru_cache(None)
def game(s):
    if s >= 51:
        return 'W'

    if any(m >= 51 for m in step(s)):
        return 'P1'

    if all(game(m) == 'P1' for m in step(s)):
        return 'V1'

    if any(game(m) == 'V1' for m in step(s)):
        return 'P2'
    if all(game(m) in ('P1', 'P2') for m in step(s)):
        return 'V2'

for i in range(1,60):
    if game(i) == 'V1':
        print(i)
        break
l = []
for i in range(1,60):
    if game(i) == 'P2':
        l.append(i)
l.sort()
print(l[0], l[1])

for i in range(1,60):
    if game(i) == 'V2':
        print(i)
        break



def step(n):
    return n + 3, n + 6, n * 3

@lru_cache(None)
def game(s):
    if s >= 132:
        return 'W'

    if any(m >= 132 for m in step(s)):
        return 'P1'

    if all(game(m) == 'P1' for m in step(s)):
        return 'V1'

    if any(game(m) == 'V1' for m in step(s)):
        return 'P2'
    if all(game(m) in ('P1', 'P2') for m in step(s)):
        return 'V2'

for i in range(1,132):
    if game(i) == 'V1':
        print(i)
        break
l = []
for i in range(1,132):
    if game(i) == 'P2':
        l.append(i)
l.sort()
print(l[0], l[1])

for i in range(1,132):
    if game(i) == 'V2':
        print(i)
        break

import sys
from functools import lru_cache



WIN_SCORE = 666

def step(s):
    return s * 3, s + 3, s + s ** 2

@lru_cache(None)
def game(s):
    if s >= WIN_SCORE:
        return 'W'

    possible_moves = step(s)

    if any(m >= WIN_SCORE for m in possible_moves):
        return 'P1'

    results = [game(m) for m in possible_moves]

    if all(res == 'P1' for res in results):
        return 'V1'

    if any(res == 'V1' for res in results):
        return 'P2'

    if all(res in ('P1', 'P2') for res in results):
        return 'V2'



for s in range(1, WIN_SCORE):
    if game(s) != 'P1':
        possible_moves_s = step(s)
        can_make_bad_move = False
        for m in possible_moves_s:
            if m < WIN_SCORE and game(m) == 'P1':
                can_make_bad_move = True
                break
        if can_make_bad_move:
            print(s)
            break


l = []
for i in range(1, WIN_SCORE):
    if game(i) == 'P2':
        l.append(i)

if l:
    l.sort()
    print(l[0], l[-1])

max_s_v2 = -1
for i in range(1, WIN_SCORE):
    if game(i) == 'V2':
        max_s_v2 = i

if max_s_v2 != -1:
    print(max_s_v2)



import sys
from functools import lru_cache


WIN_SCORE_THRESHOLD = 87

def step(s):
    return s - 2, s // 2

@lru_cache(None)
def game(s):
    if s <= WIN_SCORE_THRESHOLD:
        return 'W'

    possible_moves = step(s)

    if any(m <= WIN_SCORE_THRESHOLD for m in possible_moves):
        return 'P1'

    results = [game(m) for m in possible_moves]

    if all(res == 'P1' for res in results):
        return 'V1'

    if any(res == 'V1' for res in results):
        return 'P2'

    if all(res in ('P1', 'P2') for res in results):
        return 'V2'


s = 89
while True:
    if game(s) == 'V1':
        print(s)
        break
    s += 1

p2_list = []
s = 89
while len(p2_list) < 2:
    if game(s) == 'P2':
        p2_list.append(s)
    s += 1
print(p2_list[0], p2_list[1])

s = 89
while True:
    if game(s) == 'V2':
        print(s)
        break
    s += 1
