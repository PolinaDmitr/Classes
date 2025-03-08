# простое открытие
f = open("files/9_1.txt", "r")
print(f.readlines())
f.close()
print('-----')

f = open("files/9_1.txt", "r")
c = 0
for i in f:
    l = [int(x) for x in i.split()]
    rep = [l.count(j) for j in l]
    if 1 in rep and sum(rep) > 7 \
        and l.count(max(l)) == 1:
        not_rep_sum = sum(l[x] for x in range(7) if rep[x] == 1)
        rep_sum = sum(l) - not_rep_sum
        if not_rep_sum >= rep_sum * 3:
            c += 1
    print(l, rep)
print(c)
f.close()