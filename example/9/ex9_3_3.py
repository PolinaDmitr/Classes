from itertools import combinations

def f(a: list) -> bool:
    for i in combinations(a, 3):
        a = list(i)
        a.sort()
        if (a[1] / a[0] == a[2] / a[1]) and a[1] / a[0] != 1:
            print(i)
            return True
    return False


with open('files/9_3.txt') as file:
    k = 0
    for i in file:
        l = [int(x) for x in i.split()]
        if f(l):
            k += 1
    print(k)