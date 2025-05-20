with open('24_1.txt') as file:
    s = file.readline()
    k_max = 1
    k = 1
    for i in range(len(s) - 1):
        if int(s[i]) % 2 != int(s[i + 1]) % 2:
            k += 1
            k_max = max(k_max, k)
        else:
            k = 1
    print(k_max)
