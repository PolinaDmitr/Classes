l = []
for a1 in 'мрн':
    for a2 in 'мрина':
        for a3 in 'мрина':
            for a4 in 'мрина':
                for a5 in 'мрина':
                    for a6 in 'мрина':
                        s = ''.join([a1, a2, a3, a4, a5, a6])
                        # s = a1 + a2 + a3 + a4 + a5 + a6
                        if (s.count('м') == 1 and s.count('а') == 2
                            and s.count('р') == 1 and s.count('и') == 1
                                and s.count('н') == 1):
                            l.append(s)
print(len(l))