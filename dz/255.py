from ipaddress import *
# net = ip_network('143.168.72.213/255.255.255.240', 0)
# max_ip = [0, 0]
# for ip in net:
#     if ip != net[0] and ip != net[-1]:
#         if int(ip) > max_ip[0]:
#             max_ip = [int(ip), str(ip).replace('.', '')]
# print(max_ip[1])
#
# from ipaddress import *#?
# net = ip_network('172.16.80.0/255.255.248.0',0)
# c = 0
# for i in net:
#     if bin(int(i)).count('1') % 2 == 0:
#         c += 1
# print(c)
#
# from ipaddress import ip_network
# net = ip_network('172.16.192.0/255.255.192.0', 0)
# c = 0
# for i in net:
#     ip = f'{int(i):032b}'
#     if ip.count('1') % 5 != 0:
#         c += 1
# print(c)
#
# from ipaddress import *
# net = ip_network('158.214.121.40/255.255.255.224', 0)
# print(str(net[-2]).replace('.',''))
#
# from ipaddress import *
# net = ip_network('158.214.121.40/255.255.255.224', 0)
# print(str(net[1]).replace('.',''))
#
# from ipaddress import *
# net = ip_network('218.194.82.148/255.255.255.192', 0)
# print(str(net[-2]).replace('.',''))

# from ipaddress import *#?---
# net = ip_network('5.2.5.0/255.255.0.0',0)
# c = 0
# for i in net:
#     s = bin(int(i))[2:].zfill(32)
#     print(s)
#     if s.count('0') % 25 == 0:
#         c += 1
# print(c)

# a = 190
# b = 184
# a1 = bin(a)[2:]
# b1 = bin(b)[2:]
# print (a1,b1)#совпадение 5 цифр #19?
#
# from ipaddress import*
# net = ip_network('192.168.248.176/255.255.255.240',0)
# c = 0
# for i in net:
#     if bin(int(i))[2:].count('0') == bin(int(i))[2:].count('1'):
#         c += 1
# print(c)
#
# from ipaddress import *
# net = ip_network('172.140.68.0/255.255.248.0',0)
# c = 0
# for i in net:
#     if bin(int(i))[2:].count('0') > 15:
#         c += 1
# print(c)
# #хз
# a = 14313121137
# a1 = bin(a)[2:]
# print(a1)

# for m in range(31, 1, -1):
#     print(m)
#     net = ip_network(f'143.131.211.37/{m}', False)
#     c = 0
#     for i in net:
#         if bin(int(i)).count('1') == 10:
#             print(i)
#             c += 1
#     if c == 15:
#         print(m)
#         break

address1 = ip_address('200.154.190.12')
address2 = ip_address('200.154.184.0')

for m in range(31, 1, -1):
    net = ip_network(f'200.154.184.0/{m}', False)
    if address1 in net and address1 != net.network_address and address1 != net.broadcast_address \
            and address2 != net.network_address and address2 != net.broadcast_address:
        print(net, m)
        break
