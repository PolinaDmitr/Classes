#(x > A) ∨ (y > A) ∨ (x + 2y < 80)

def f(x, y, a):
    return (x > a) or (y > a) or (x + 2 * y < 80)

for a in range(30, 1, -1):
    flag = True
    for x in range(10000):
        for y in range(10000):
            if not f(x, y, a):
                flag = False
                break
        if not flag:
            break
    if flag:
        print(a)
