#семизначные числа в 9-ой системе, 2,4,6 не в начале
#не заканчивается на 3 одинаковых
l = []
for a1 in '13578':
    for a2 in '012345678':
        for a3 in '012345678':
            for a4 in '012345678':
                for a5 in '012345678':
                    for a6 in '012345678':
                        for a7 in '012345678':
                            s = a1 + a2 + a3 + a4 + a5 + a6 + a7
                            if not(a5 == a6 and a6 == a7):
                                l.append(s)
print(len(l))