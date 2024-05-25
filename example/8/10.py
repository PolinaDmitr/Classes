count = 0
for a1 in '123456789ABCDEFG':
    for a2 in '0123456789ABCDEFG':
        for a3 in '0123456789ABCDEFG':
            for a4 in '0123456789ABCDEFG':
                for a5 in '0123456789ABCDEFG':
                    s = a1 + a2 + a3 + a4 + a5
                    if s.count('1') <= 2:
                        for i in '3579BDF':
                            s = s.replace(i, '*')
                        if '11' not in s and '1*' not in s and '*1' not in s:
                            count += 1
                            # print(s)
print(count)