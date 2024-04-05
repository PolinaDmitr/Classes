count = 0
for a1 in 'кидала':
    for a2 in 'кидала':
        for a3 in 'кидала':
            for a4 in 'кидала':
                for a5 in 'кидала':
                    s = a1 + a2 + a3 + a4 + a5
                    if s.count('к') == 1 and s.count('и') == 1 and s.count('д') == 1 \
                        and s.count('а') == 1 and s.count('л') == 1:
                        count += 1
                    if (s.count('к') == 1 or s.count('к') ==0) and (s.count('и') == 1 or s.count('и') ==0) and (s.count('д') == 1 or s.count('д') ==0)\
                        and (s.count('л') == 1 or s.count('л') ==0) and s.count('а') == 2:
                        count += 1
print(count)