# #11
# a = int(input())
# b = int(input())
# c = 0
# for i in range (a, b):
#     if (i ** 3) % 10== 4 or (i ** 3) % 10== 9:
#         c += 1
# print (c)
# #12
# n = int(input())
# c = 0
# for i in range (11, n):
#      if (i ** 2) % 10== 2.52 or (i ** 3) % 10== 5 or (i ** 3) % 10== 88:
#          c += 1
# print (c)
# #13
# n = int(input())
# f = 1
# while n > 1:
#     f = f * n
#     n = n - 1
# print(f)
# #14
# n = int(input())
# p = 0
# for i in range(1, n+1):
#     if (n % i) == 0:
#         p = p + i
# print(p)
# #15
# n1 = int(input())
# a = 0
# b = 0
# for i in range (n1):
#     n2 = int(input())
#     if n2 > a:
#         a = b
#         a = n2
#     else:
#         n2 > b
#         b = a
#         b = n2
# print (a)
# #16
# a = 0
# for i in range(10):
#     n = int(input())
#     if n % 2 == 0:
#         a += 1
# if a == 10:
#     print('YES')
# else:
#     print('NO')
# print (a)
# #17
# n = int(input())
# a = 1
# b = 1
# for i in range(1 , n):
#     c = a + b
#     a = b
#     b = c
# print (c)
# #18
# n = int(input())
# c = 0
# while n >= 0:
#     c += n
#     n = int(input())
# print (c)
# #19
# a = int(input())
# c = 0
# while 11 <= a <= 55:
#     a = int(input())
#     if a == 5:
#             c += 1
# print(c)
#20
a = int(input())
c = 0
for i in [25, 10, 5, 1]:
    c += a // i
    a = a % i
print(c)