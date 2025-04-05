from ipaddress import *

add = ip_address('151.168.147.193')
for m in range(31, -1, -1):
    net = ip_network(f'151.168.147.128/{m}', False)
    print(net)
    if add in net:
        print(net, m)
        break