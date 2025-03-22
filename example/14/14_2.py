from string import ascii_uppercase

alpha = '0123456789' + ascii_uppercase


for p in range(10, 36):
    for x in range(p):
        for y in range(p):
            a1 = int(f'24{alpha[x]}9', p)
            a2 = int(f'{alpha[y]}{alpha[x]}{alpha[y]}3', p)
            a3 = int(f'{alpha[x]}4{alpha[y]}0', p)
            if a1 + a2 == a3:
                print(x, y, int(f'{alpha[x]}{alpha[y]}{alpha[y]}', p))

for p in range(10, 36):
    for x in range(p):
        for y in range(p):
            a1 = 9 + x * p + 4 * (p ** 2) + 2 * (p ** 3)
            a2 = y * (p ** 3) + x * (p ** 2) + y * p + 3
            a3 = x * (p ** 3) + 4 * (p ** 2) + y * p
            if a1 + a2 == a3:
                print(x, y, x * (p ** 2) + y * p + y)
                break