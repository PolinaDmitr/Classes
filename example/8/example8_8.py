count = 0
for a1 in 'кидал':
    for a2 in 'кидал':
        for a3 in 'кидал':
            for a4 in 'кидал':
                for a5 in 'кидал':
                    s = a1 + a2 + a3 + a4 + a5
                    if s.count('к') == 1 and s.count('и') == 1 and s.count('д') == 1 \
                        and s.count('а') == 1 and s.count('л') == 1:
                        print(1, s)
                        count += 1
                    if (s.count('к') <= 1) and (s.count('и') <= 1 ) and (s.count('д') <= 1)\
                        and (s.count('л') <= 1 ) and s.count('а') == 2 and s.count('аа') == 0:
                        print(2, s)
                        count += 1
print(count)