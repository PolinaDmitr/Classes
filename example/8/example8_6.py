count = 0
for a1 in 'асин':
    for a2 in 'асин':
        for a3 in 'асин':
            for a4 in 'асин':
                for a5 in 'асин':
                    for a6 in 'асин':
                        for a7 in 'асин':
                            s = ''.join([a1, a2, a3, a4, a5, a6, a7])
                            if (s.count('а') == 2 and s.count('с') == 3
                                and s.count('н') == 1 and s.count('и') == 1):
                                count += 1
print(count)