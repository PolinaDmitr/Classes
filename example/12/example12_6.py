count = 0
s = '*' * 200
while '****' in s or '???' in s:
    if '****' in s:
        s = s.replace('****', '???', 1)
        count += 3
    s = s.replace('??', '*', 1)
print(count)