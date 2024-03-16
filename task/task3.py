#ветвление
a = int(input())
b = int(input())
if a > b:
    print("Наибольшее 1:", a)
else:
    if a == b:
        print("Равны")
    else:
        print("Наибольшее 2:", b)

if a > b:
    print("Наибольшее 1:", a)
elif a == b:
    print("Равны")
else:
    print("Наибольшее 2:", b)

if a == b:
    print('Да, они равны')

if 8 <= 9:
    print('nk')
if 90 >= 100:
    print('nione')
if 9 != 10:
    print('lll')

# число является чётным и кратным либо 3, либо 7
g = int(input())
if (g % 2 == 0) and (g % 3 == 0 or g % 7 == 0):
    print('yes')
else:
    print('no')

# число является кратным 4 или кратным 7
# и не оканчивается на 8
