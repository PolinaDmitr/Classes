counter = 0
for a1 in '1234567':
    for a2 in '01234567':
        for a3 in '01234567':
            for a4 in '01234567':
                s = a1 + a2 + a3 + a4
                n = int(s, 8)
                if n % 4 == 0:
                    counter += 1
print(counter)