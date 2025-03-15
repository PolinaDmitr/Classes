with open("files/17_2_2.txt") as file:
    num = [int(x) for x in file]
    print(num)
    ost_min = (min(num)) % 3
    ost_max = (max(num)) % 7
    k = []
    for i in range(len(num) - 2):
        l = [x % 3 for x in (num[i], num[i + 1], num[i + 2])]
        m = [x % 7 for x in (num[i], num[i + 1], num[i + 2])]
        if l.count(ost_min) == 1 and m.count(ost_max) >= 2:
            k.append(num[i] + num[i + 1] + num[i + 2])
    print(len(k), max(k))
