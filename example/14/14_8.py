from string import ascii_uppercase

#функция для поиска последнего максимума
def f(l : list):
    l_max = l[0]
    ind_max = 0
    for i in range(len(l)):
        if l[i] >= l_max:
            l_max = l[i]
            ind_max = i
    return ind_max


def rep_f(n : int):
    l = [0] * 35
    while n > 0:
        ost = n % 35
        l[ost] += 1
        n //= 35
    return l

print(int('60QR0', 35) + int('59SH', 35) + int('PH069YW', 35))
al = '0123456789' + ascii_uppercase
print('R', al.index('R'))
print('Q', al.index('Q'))
print('S', al.index('S'))
print('H', al.index('H'))
print('P', al.index('P'))
print('Y', al.index('Y'))
print('W', al.index('W'))
#0123456789ABCDEFGHIJK(20)LMNOPQRSTU(30)VWXYZ
#0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
for x in range(34, -1, -1):
    #6xQRx+x59SH+PHx69YW,
    n1 = x + (27 * 35) + (26 * 35 ** 2) + (x * 35 ** 3) + (6 * 35 ** 4)
    n2 = 17 + (28 * 35) + (9 * 35 ** 2) + (5 * 35 ** 3) + (x * 35 ** 4)
    n3 = 32 + (34 * 35) + (9 * 35 ** 2) + (6 * 35 ** 3) + (x * 35 ** 4) + (17 * 35 ** 5) + (25 * 35 ** 6)
    n = n1 + n2 + n3
    l = rep_f(n)
    l_max = f(l)
    print(l, l_max, n)
    if n % (l_max ** 2) == 0:
        #в чём дело?
        print(x, n / l_max ** 2)

