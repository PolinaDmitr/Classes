a1 = (0, 2, 4, 6, 8)
a2 = (1, 3, 5, 7, 9)
counter = 0

#чнчнчн
for b1 in a1:
    for b2 in a2:
        for b3 in a1:
            for b4 in a2:
                for b5 in a1:
                    for b6 in a2:
                        if (b1 > b2 > b3 > b4 > b5 > b6) \
                            and (b1 % 2 == b3 % 2 == b5 % 2) \
                            and (b2 % 2 == b4 % 2 == b6 % 2) \
                            and (b1 % 2 != b2 % 2):
                            print(b1, b2, b3, b4, b5, b6, sep='')
                            counter += 1
for b1 in a2:
    for b2 in a1:
        for b3 in a2:
            for b4 in a1:
                for b5 in a2:
                    for b6 in a1:
                        if (b1 > b2 > b3 > b4 > b5 > b6) \
                            and (b1 % 2 == b3 % 2 == b5 % 2) \
                            and (b2 % 2 == b4 % 2 == b6 % 2) \
                            and (b1 % 2 != b2 % 2):
                            print(b1, b2, b3, b4, b5, b6, sep='')
                            counter += 1
print(counter)
