l = '1' + '2' * 51

while '12' in l or '1' in l:
    if '12' in l:
        l = l.replace('12', '2221', 1)
    else:
        l = l.replace('1', '222222', 1)

print(l)
print(l.count('2'))

