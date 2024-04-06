for n in range(8, 15):
    result = int('221', n) + int('34', 8) == int('180', n + 2)
    print(n, result)

for x in range(0, 8):
    oct_x = int(f'4{x}2', 8)
    print(hex(oct_x), f'{oct_x:x}')