with open('24_10.txt') as file:
    s = file.readline()
    l = []
    for i in range(len(s)):
        if s[i] == 'F':
            l.append(i)
    print(s[:100])
    print(l[:50])
    m = 0
    for i in range(0, len(l) - 2):
        m = max(m, l[i + 2] - l[i] - 1)
    print(m)