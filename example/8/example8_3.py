l = []
for a1 in 'кусат':
    for a2 in 'кусать':
        for a3 in 'кусать':
            for a4 in 'кусать':
                for a5 in 'кусать':
                    s = ''.join([a1, a2, a3, a4, a5])
                    # s = a1 + a2 + a3 + a4 + a5 + a6
                    if (s.count(s[0]) == 1 and s.count(s[1]) == 1
                            and s.count(s[2]) == 1 and s.count(s[3]) == 1
                            and s.count(s[4]) == 1 and s.count('сук') == 0):
                        l.append(s)
print(len(l))