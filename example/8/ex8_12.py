l1 = ['m', 'a', 'r', 'i', 'n', 'a']
count = 0
for a1 in l1:
    l2 = list(l1)
    l2.remove(a1)
    for a2 in l2:
        l3 = list(l2)
        l3.remove(a2)
        for a3 in l3:
            l4 = list(l3)
            l4.remove(a3)
            for a4 in l4:
                l5 = list(l4)
                l5.remove(a4)
                for a5 in l5:
                    l6 = list(l5)
                    l6.remove(a5)
                    a6 = l6[0]
                    s = a1 + a2 + a3 + a4 + a5 + a6
                    print(s)
                    if a1 not in 'ai':
                        count += 1
print(count / 2)
