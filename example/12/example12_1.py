l = '9' * 79

while '2222' in l or '9999' in l:
    if '2222' in l:
        l = l.replace('2222', '99', 1)
    else:
        l = l.replace('9999', '22', 1)

print(l)