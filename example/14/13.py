from string import digits, ascii_uppercase
def f(x):
    alph = (digits + ascii_uppercase)[:25] #01234...9ABCD...
    s = ''
    while x > 0:
        s = alph[x % 25] + s
        x //= 25
    return s


numb = 4 * 3125 ** 2019 + 3 * 625 ** 2020 - 2 * 125 ** 2021 + 25 ** 2022 - 4 * 5 ** 2023 - 2024
numb_25 = f(numb)
k = 0
for i in numb_25:
    if i > 'A':
        k += 1
print(k)