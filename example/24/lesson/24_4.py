with open('24_4.txt') as file:
    s = file.readline()
    print(s[:100])
    s = s.replace('A', 'X').replace('E', 'X')
    print(s[:100])
    s = s.replace('B', 'Y').replace('C', 'Y').replace('D', 'Y').replace('F', 'Y').replace('G', 'Y').replace('H', 'Y')
    print(s[:100])
    s = s.replace('YYX', '@')
    print(s[:100])
    print(s[-100:])
    l = s.split('@')
    print(l[:10])
    print(max(len(i) for i in l) + 6)

