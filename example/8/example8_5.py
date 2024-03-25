count = 0
for a1 in 'калий':
    for a2 in 'калий':
        for a3 in 'калий':
            for a4 in 'калий':
                for a5 in 'калий':
                    for a6 in 'калий':
                        s = ''.join([a1, a2, a3, a4, a5, a6])
                        if (s.count('й') <= 1 and s[0] != 'й' and s[5] != 'й'
                            and s.count('йи') == 0 and s.count('ий') == 0):
                            count += 1
print(count)
