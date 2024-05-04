from ipaddress import *

net = ip_network('192.168.32.48/255.255.255.192', 0)
count = 0
for i in net:
    print(i)
    if bin(int(i))[2:].zfill(32).count('1') % 5 != 0:
        print(i)
        count += 1
print(count)