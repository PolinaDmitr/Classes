from itertools import *

def f(a: tuple, x):
    return (not (x in a)) <= ((not (x in (1, 2, 3, 4, 5, 6)) and (x in (3, 5, 15))) or not (x in (3, 5, 15)))


for k in range(1, 7):
    seq = combinations((1, 2, 3, 4, 5, 6, 15), k)
    for a in seq:
        flag = True
        for x in range(-10, 20):
            if not f(a, x):
                flag = False
                break
        if flag:
            print(a)


print(39 & 51)  #поразрядная конъюнкция