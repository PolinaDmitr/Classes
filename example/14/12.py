from string import ascii_uppercase, digits

alph = (digits + ascii_uppercase)[:20]
print(alph)
x_max = '-1'
for x in alph:
    flag = True
    for y in alph:
        num = int(f'5{y}4{x}{y}4HJ4', 20) + int(f'4{y}6B{y}{x}1', 20)
        if num % 15 != 0:
            flag = False
            break
    if flag:
        x_max = x
print(x_max, int(f'584{x_max}84HJ4', 20) + int(f'486B8{x_max}1', 20))
