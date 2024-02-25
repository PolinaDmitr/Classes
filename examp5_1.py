def f(x):
    string = f'{x:b}' + f'{(x % 4):b}'
    return int(string, 2)


l = []
for i in range(1, 10000):
    l.append(f(i))
b = [0] * (max(l) + 100)
for i in l:
    b[i] = 1

k = 0
for i in range(len(b) - 65):
    k = max(k, sum(b[i : i + 65]))
print(k)

