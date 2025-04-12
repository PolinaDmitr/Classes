from ipaddress import *


#1
net = ip_network('143.168.72.213/255.255.255.240', strict=False)
last_usable_ip = net.broadcast_address - 1
print(str(last_usable_ip).replace('.', ''))



#2


net = ip_network("172.16.80.0/255.255.248.0")
l = []
for i in net:
    x_new = bin(int(i))[2:].zfill(32)
    if x_new.count('1') % 2 != 0:
        l.append(x_new)
print(len(l))


#3
net = ip_network("172.16.192.0/255.255.192.0")
l = []
for i in net:
    x_new = bin(int(i))[2:].zfill(32)
    if x_new.count('1') % 5 != 0:
        l.append(x_new)
print(len(l))


#4
net = ip_network('158.214.121.40/255.255.255.224', strict=False)
first_usable_ip = net.network_address + 1
print(first_usable_ip)
print(str(last_usable_ip).replace('.', ''))


#5

net = ip_network("218.194.82.148/255.255.255.192", strict=False)
last_usable_ip = net.broadcast_address - 1
print(str(last_usable_ip).replace('.', ''))


#6

net = ip_network("5.2.5.0/255.255.0.0", False)
l = []
for i in net:
    x_new = bin(int(i))[2:].zfill(32)
    if x_new.count('0') % 25 == 0:
        l.append(x_new)
print(len(l))


#7 - (20)


# ip1_str = "200.154.190.12"
ip2_str = "200.154.184.0"

# ip1_obj = IPv4Address(ip1_str)
ip2_obj = IPv4Address(ip2_str)

max_common_prefix = 0

for prefix_len in range(31, 1, -1):
    network = ip_network(f"200.154.190.12/{prefix_len}", strict=False)
    if ip2_obj in network and network.broadcast_address != ip2_obj and network.network_address != ip2_obj:
        max_common_prefix = prefix_len
        break


print(max_common_prefix)


#8
net = ip_network("192.168.248.176/28", strict=False)

l = []

for i in net:
    binary_ip = bin(int(i))[2:].zfill(32)

    if binary_ip.count('1') == 16:
        l.append(i)

print(len(l))



#9

net = ip_network("172.140.68.0/255.255.248.0", False)
l = []
for i in net:
    x_new = bin(int(i))[2:].zfill(32)
    if x_new.count('0')  > 15:
        l.append(x_new)
print(len(l))


#10
ip_node_str = "143.131.211.37"
target_count = 15
found_prefix = 0


for prefix_len in range(31, 0, -1):
    net = ip_network(f"{ip_node_str}/{prefix_len}", strict=False)

    count_matching_ips = 0


    for ip_addr in net:
        ip_int = int(ip_addr)
        binary_ip = bin(ip_int)[2:].zfill(32)


        if binary_ip.count('1') == 10:
            count_matching_ips += 1

    if count_matching_ips == target_count:
        found_prefix = prefix_len
        break
print(found_prefix)

