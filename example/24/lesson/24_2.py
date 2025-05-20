with open('24_2.txt') as file:
    s = file.readline()
    m = 0
    l = 0
    k = 0
    for r in range(3, len(s)):
        if s[r - 3] + s[r - 2] + s[r - 1] + s[r] == 'FSRQ':
            k += 1
        while k > 80:
            if s[l] + s[l + 1] + s[l + 2] + s[l + 3] == 'FSRQ':
                k -= 1
            l += 1
        if k == 80:
            m = max(m, r - l + 1)

    print(m)

