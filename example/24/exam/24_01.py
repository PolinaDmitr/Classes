with open('24.23_19887.txt') as file:
    line = file.readline()
    c = cmax = 1
    for i in range(len(line) - 1):
        if int(line[i]) % 2 != int(line[i + 1]) % 2:
            c += 1
            cmax = max(c, cmax)
        else:
            c = 1
print(cmax)