c = 0
for a1 in '1357':
    for a2 in '2468':
        for a3 in '1357':
            for a4 in '2468':
                for a5 in '1357':
                    for a6 in '2468':
                        for a7 in '1357':
                            for a8 in '2468':
                                for a9 in '1357':
                                    s = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9
                                    f = True
                                    for i in s:
                                        if s.count(i) > 3:
                                            f = False
                                            break
                                    if f:
                                        c += 1
for a1 in '2468':
    for a2 in '1357':
        for a3 in '2468':
            for a4 in '1357':
                for a5 in '2468':
                    for a6 in '1357':
                        for a7 in '2468':
                            for a8 in '1357':
                                for a9 in '2468':
                                    s = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9
                                    f = False
                                    for i in s:
                                        if s.count(i) > 3:
                                            f = True
                                            break
                                    if not f:
                                        c += 1
print(c)