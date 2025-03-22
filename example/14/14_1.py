for x in '01234567':
    a1 = int(x + '1' + x, 16)
    a2 = int(f'{x}3{x}3', 8)
    a_sum = a1 + a2
    if a_sum ** 0.5 == int(a_sum ** 0.5):
        print(x)