for n in range(4, 10000):
    s = '1' + '2' * n
    while '12' in s or '322' in s or '222' in s:
        s = s.replace('12', '2', 1)
        s = s.replace('322', '21', 1)
        s = s.replace('222', '3', 1)
    # a = 0
    # for i in s:
    #     a += int(i)
    a = sum(int(x) for x in s)
    if a == 15:
        print(n)
        break