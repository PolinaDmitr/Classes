from collections import Counter


def perevod(n):
    ost = ''
    while n > 0:
        ost = str(n%5) + ost
        n = n // 5
    return ost



# # l = []
# for x in range(2005, 0, -1):
#     s = 4 ** 163 * 5 + 12 ** 62 - x
#     s_5 = perevod(s)
#     if s_5.count('1') < s_5.count("4"):
#         # l.append(x)
#         print(x)
#         break
# # print(max(l))







# digits_42 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdef'
#
# def custom_int(s, base):
#     res = 0
#     for c in s:
#         res = res * base + digits_42.index(c)
#     return res

# for x_val in range(42):
#     # x_char = digits_42[x_val]
#     # num1 = custom_int(f'J569{x_char}', 42)
#     # num2 = custom_int(f'1{x_char}IA', 42)
#     num1 = 19 * 42 ** 4 + 5 * 42 ** 3 + 6 * 42 ** 2 + 9 * 42 + x_val
#     num2 = 1 * 42 ** 3 + x_val * 42 ** 2 + 18 * 42 + 10
#     total = num1 + num2
#     if total % 155 == 0:
#         otv = total // 155
#         print(otv)
#         break

#
# def to_decimal(s, x_val):
#     digits = "0123456789ABCDEFGH"
#     base = 18
#     num = 0
#     for c in s:
#         if c == 'x':
#             digit = x_val
#         else:
#             digit = digits.index(c)
#         num = num * base + digit
#     return num
#
# for x in range(18):
#     num1 = to_decimal("11Hx05", x)
#     num2 = to_decimal("3Fx54x8", x)
#     num3 = to_decimal("Gxxx9", x)
#     total = num1 + num2 + num3
#     if total % 14 == 0:
#         otv = total // 14
#         print(otv)
#         break

#
# def perevod(n):
#     ost = ''
#     while n > 0:
#         ost = str(n%4) + ost
#         n = n // 4
#     return ost
#
#
# def perevod_v2(n):
#     a = 0
#     b = 0
#     c = 0
#     while n > 0:
#         ost = n % 4
#         if ost in (1, 3):
#             b += 1
#         else:
#             a += 1
#
#         if ost == 2:
#             c += 1
#
#         n = n // 4
#     return a, b, c
#
#
# for x in range(2006, 0, -1):
#     s = 43 ** 56 + 113 ** 841 - x
#     s_4 = perevod(s)
#     chet = 0
#     nechet = 0
#     for i in s_4:
#         if int(i) % 2:
#             chet += 1
#         else:
#             nechet += 1
#     if chet % 2 == 0 and nechet % 2 == 0 and s_4.count('2') <= 712:
#         print(x)
#         break
#
# for x in range(2006, 0, -1):
#     s = 43 ** 56 + 113 ** 841 - x
#     s_4 = perevod(s)
#     a, b, c = perevod_v2(s) #если основание больше 10
#     if a % 2 == 0 and b % 2 == 0 and c <= 712:
#         print(x)
#         break
#
#
#
# s = 5 * 729**2024 + 3 * 243**1413 - 7 * 81**169 - 2 * 9**107 + 3017
#
# sum_even = 0
# while s > 0:
#     digit = s % 27
#     if digit <= 25 and digit % 2 == 0:
#         sum_even += digit
#     s //= 27
#
# print(sum_even)
#
#
l = []
l2 = []
digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for x in range(35):
    x_char = digits[x]
    s = int(f'6{x}QR{x}', 35) + int(f'{x}59SH',35) + int(f'PH{x}69YW',35)
    c = Counter(str(s))
    most = c.most_common()

    for i in range(len(most)):
        if int(most[i][0]) != 0 and s % (int(most[i][0])) ** 2 == 0:
            l.append(int(most[i][0]))
            if s % max(l) ** 2:
                l2.append(x)
s = int(f'6{max(l2)}QR{max(l2)}', 35) + int(f'{max(l2)}59SH',35) + int(f'PH{max(l2)}69YW',35)
c = Counter(str(s))
most=c.most_common()
l3 = []
for i in range(len(c)):
    l3.append(int(most[i][0]))
print(s/(max(l3) ** 2))





