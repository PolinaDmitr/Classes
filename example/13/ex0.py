from ipaddress import *

net = ip_network('202.75.38.160/255.255.255.240')
for i in net:
    add = bin(int(i))[2:].zfill(32)
    if '111' in add:
        print(i, add)