#4
# with open ('17_2_4.txt')as file:
#     num = [int(x) for x in file]
#     k = []
#     m43 = max([x for x in num if abs(x) % 100 == 43])
#     for i in range (len(num) - 2):
#         if 100000 >  num[i] >9999 or 100000 >  num[i+1] >9999 or 100000 >  num[i+2] >9999:
#             s = num[i] + num[i + 1] +num[i+2]
#             if s > m47:
#                 k.append(s)
# print(len(k),min(k))
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
# с = 0
# max_sum = -float('inf')
# for i in range (len(num) - 2):
#     if sum(str(x).count('0') == 0 for x in i) > 1 and sum(i) < max2:
#         с += 1
#         max_sum = max(max_sum, sum(i))
# print(с, max_sum)

# num = [int(x) for x in open('17_2_7.txt')]
# maxi = max(num)
# mini = min(num)
# count = 0
# mal = -1000000
# for i in range(len(num)-1):
#     if (num[i] % 3 == maxi % 3) or (num[i + 1] % 3 == maxi % 3):
#         if (num[i] % 7 == mini % 7) or (num[i + 1] % 7 == mini % 7):
#                 count += 1
#                 mal = max(mal, num[i] + num[i+1])
# print(count, mal)

# num = [int(x) for x in open('17_2_8.txt')]
# maxi = max(num) % 10
# s = len(num)
# с = 0
# min_m = 100000000
# for i in range(s - 1):
#     if (2 * i + 3) % 10 == maxi:
#         с += 1
#         min_m = min(min_m, abs(num[i] + num[i+1] - (2 * i + 3)))
# print(с, min_m)