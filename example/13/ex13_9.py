from ipaddress import *


net = ip_network("112.208.0.0/255.255.128.0")
k = 0
for n in net:
    ip_bin = bin(int(n))[2:]
    if ip_bin.count('1') % 11 == 0:
        k = k + 1
print(k)