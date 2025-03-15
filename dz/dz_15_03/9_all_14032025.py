f = list(open("9_2.txt"))
k = 0
for i in f:
    f_new = [int(x) for x in i.split()]
    rep = [f_new.count(p) for p in f_new]
    if rep.count(3) == 3 and rep.count(1) == 3:
        if max(f_new) ** 2 + min(f_new) ** 2 > (sum(f_new) - (max(f_new) + min(f_new))) ** 2:
            k += 1
print(k)

f = list(open("9_5.txt"))
k = 0

for i in f:
    f_new = [int(x) for x in i.split()]
    rep = [f_new.count(p) for p in f_new]
    if rep.count(3) == 3 and rep.count(1) == 4:
        nepov = []
        povt_num = 0
        for d in f_new:
            if f_new.count(d) == 3 and povt_num == 0:
                povt_num = d
            elif f_new.count(d) == 1:
                nepov.append(d)

        if sum(nepov) / len(nepov) <= povt_num:
            k += 1

print(k)


def arifm(l):
    l = sorted(l)
    return l[1] - l[0] == l[2] - l[1] == l[3] - l[2] != 0



import itertools
f = list(open("9_6.txt"))
k = 0

for i in f:
    f_new = [int(x) for x in i.split()]

    for combo in itertools.combinations(f_new, 4):
        if arifm(combo):
            k += 1
            break

print(k)


f = list(open("9_7.txt"))
k = 0

for i in f:
    f_new = [int(x) for x in i.split()]
    for p in f_new:
        if sum(f_new) / len(f_new) == p:
            k += 1
            break
print(k)



f = list(open("9_8.txt"))
k = 0
index = 0

for i in f:
    index += 1
    f_new = [int(x) for x in i.split()]
    rep = [f_new.count(p) for p in f_new]
    if rep == [1, 1, 1, 1]:
        if (max(f_new) + min(f_new)) ** 2 > sum(i ** 3 for i in f_new if i != max(f_new) and i != min(f_new)):
            k += index
print(k)




f = list(open("9_9.txt"))
k = 0
otv = 0
for i in f:
    k += 1
    f_new = [int(x) for x in i.split()]
    rep = [f_new.count(p) for p in f_new]
    if rep.count(3) == 6 and rep.count(1) == 1:
        pov = []
        for p in f_new:
            if f_new.count(p) > 1:
                pov.append(p)
        nepov = []
        for nep in f_new:
            if f_new.count(nep) == 1:
                nepov.append(nep)
        if (sum(pov)/len(pov)) < (sum(nepov)/len(nepov)):
            otv = k
print(otv)

f = list(open("9_10.txt"))
k = 0

for i in f:
    f_new = [int(x) for x in i.split()]
    rep = [f_new.count(p) for p in f_new]

    condition1 = rep.count(2) == 2 and rep.count(1) == 3

    even_sum = sum(x for x in f_new if x % 2 == 0)
    odd_sum = sum(x for x in f_new if x % 2 != 0)
    has_even = any(x % 2 == 0 for x in f_new)
    has_odd = any(x % 2 != 0 for x in f_new)

    condition2 = (even_sum > odd_sum) and has_even and has_odd


    if condition1 or condition2:
        k += 1

print(k)








