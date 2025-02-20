count = 0
a = set()
for a1 in 'kon':
    for a2 in 'kon':
        for a3 in 'kon':
            for a4 in 'kon':
                for a5 in 'kon':
                    a.add(a1 + a2 + a3 + a4 + a5)
                    count += 1
print(count)
print(len(a))

print(5 ** 5 + 6 ** 5 - count * 2)