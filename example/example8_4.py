count = 0

for a1 in '1234567':
    for a2 in '01234567':
        for a3 in '01234567':
            for a4 in '01234567':
                s = a1 + a2 + a3 + a4
                s_dec = int(s, 8)
                if s_dec % 4 == 0:
                    count += 1
print(count)