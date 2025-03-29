#4
with (open ('17_2_4.txt') as file):
    num = [int(x) for x in file]
    k = []
    m43 = max([x for x in num if (9999 < x < 100000) and (abs(x) % 100 == 43)]) ** 2
    for i in range (len(num) - 2):
        if  (9999 < abs(num[i]) < 100000 and abs(num[i]) % 100 == 43) \
            or (9999 < abs(num[i + 1]) < 100000 and abs(num[i + 1]) % 100 == 43) \
            or (9999 < abs(num[i + 2]) < 100000 and abs(num[i + 2]) % 100 == 43):
            print(num[i], num[i + 1], num[i+2])
            s = num[i] ** 2 + num[i + 1] ** 2 + num[i+2] ** 2
            if s <= m43:
                k.append(s)
print(len(k),min(k))
#хз
# with open ('17_2_5.txt')as file:
#     num = [int(x) for x in file]
#     k =0
#
#     for i in range(len(num) - 1):
#         if (num[i] + num[i + 1]) % 43 == min(num):
#             k +=1
#             maxi = max(int(num[i] - num[i + 1] or num[i + 1] - num[i]))
# print (k, maxi)

# with open ('17_2_6.txt')as file:
#     num = [int(x) for x in file]
#     max2 = max(num) / 2
# c = 0
# max_sum = -float('inf')
# for i in range (len(num) - 2):
#     if sum(str(x).count('0') == 0 for x in i) > 1 and sum(i) < max2:
#         c += 1
#         max_sum = max(max_sum, sum(i))
# print(c, max_sum)

num = [int(x) for x in open('17_2_7.txt')]
maxi = max(num)
mini = min(num)
count = 0
mal = -1000000
for i in range(len(num)-1):
    if (num[i] % 3 == maxi % 3) or (num[i + 1] % 3 == maxi % 3):
        if (num[i] % 7 == mini % 7) or (num[i + 1] % 7 == mini % 7):
                count += 1
                mal = max(mal, num[i] + num[i+1])
print(count, mal)

num = [int(x) for x in open('17_2_8.txt')]
maxi = max(num) % 10
s = len(num)
c = 0
min_m = 100000000
for i in range(s - 1):
    if (2 * i + 3) % 10 == maxi:
        c += 1
        min_m = min(min_m, abs(num[i] + num[i+1] - (2 * i + 3)))
print(c, min_m)