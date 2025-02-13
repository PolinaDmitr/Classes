s = '6' * 666
while '666' in s or '111' in s:
    if '666' in s:
        s = s.replace('66', '1', 1)
    else:
        s = s.replace('111', '6', 1)
print(s)