# Сеть, в которой содержится узел с IP-адресом 116.242.A.26,
# задана маской сети 255.255.255.224,
# где A - некоторое допустимое для записи IP-адреса число.
# Определите максимальное значение A, для которого для всех IP-адресов этой сети
# в двоичной записи IP-адреса суммарное количество единиц в левых двух байтах не
# меньше суммарного количества единиц в правых двух байтах
from ipaddress import *


max_a = -1
for a in range(256):
    net = ip_network(f'116.241.{a}.26/255.255.255.224', 0)
    flag = True
    for n in net:
        add = bin(int(n))[2:].zfill(32)
        if add[:16].count('1') < add[16:].count('1'):
            flag = False
    if flag:
        max_a = max(max_a, a)
print(max_a)
print(f'{116:b}'.zfill(8), f'{241:b}'.zfill(8), f'{240:b}'.zfill(8), f'{26:b}'.zfill(8), sep='.')
print(bin(224))

