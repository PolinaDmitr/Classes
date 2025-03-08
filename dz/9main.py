from random import shuffle
a = ['3'] * 10 + ['5'] * 10 + ['7'] * 10
for i in range(10):
    shuffle(a)
    s = '>' + ''.join(a)
    while '>3' in s or '>5' in s or '>7' in s:
        if '>3' in s:
            s = s.replace('>3', '55>', 1)
        elif '>5' in s:
            s = s.replace('>5', '5>3', 1)
        else:
            s = s.replace('>7', '3>5', 1)
    s = s.replace('>', '')
    print(sum(int(x) for x in s))
l = ''
if '222' in l:
    l = l.replace('222', '6', 1)
else:
    l = l.replace('6666', '2', 1)