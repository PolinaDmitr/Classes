

f = open('9_2.txt').read().splitlines()
c = 0

for st in f:
    # st = st.strip().replace('\t', ' ')
    a = st.split()

    if len(a) != 6:
        continue

    ch = list(map(int, a))


    uq = set(ch)


    if len(uq) != 4:
        continue

    cnt = []
    for x in uq:
        cnt.append(ch.count(x))
    cnt.sort()


    if cnt != [1, 1, 1, 3]:
        continue

    minim = min(ch)
    maxim = max(ch)


    tmp = ch.copy()
    tmp.remove(minim)
    tmp.remove(maxim)

    summa = sum(tmp)

    if minim ** 2 + maxim ** 2 >= summa ** 2:
        c += 1

print(c)



f = open('9_5.txt').read().splitlines()
k = 0

for st in f:
    st = st.strip().replace('\t', ' ')
    a = st.split()

    if len(a) != 7:
        continue

    ch = list(map(int, a))


    uq = list(set(ch))


    if len(uq) != 5:
        continue


    cnt = []
    for x in uq:
        cnt.append(ch.count(x))
    cnt.sort()


    if cnt != [1, 1, 1, 1, 3]:
        continue

    repeat = None
    non = []
    for x in uq:
        if ch.count(x) == 3:
            repeat = x
        else:
            non.append(x)
    if (sum(non)/len(non)) > repeat:
        continue
    k+=1
print(k)
