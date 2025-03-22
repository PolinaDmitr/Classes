f = open("17_2_3.txt")
string=[int(x) for x in f]
k = 0
l = []
kol_n_7 = sum(1 for x in string if abs(x) % 10 == 7)
for i in range(len(string) - 1):
    if ((string[i] == abs(string[i])) and (string[i+1] != abs(string[i+1]))) or ((string[i] != abs(string[i])) and (string[i+1] == abs(string[i+1]))):
        if (string[i] + string[i+1]) < kol_n_7:
            k += 1
            l.append(string[i] + string[i+1])


print(k, max(l))


f = open("17_2_4.txt")
string=[int(x) for x in f]
k = 0
max_el = []
otv_2 = []
for x in string:
    if abs(x) % 100 == 43 and len(str(abs(x))) == 5:
        max_el.append(x)

for i in range(len(string) - 2):
    #дешевле и понятнее будет двойное неравенство 10000 <= x <= 99999
    if (((len(str(abs(string[i]))) == 5) and (abs(string[i]) % 100 == 43)) or ((len(str(abs(string[i+1]))) == 5) and (abs(string[i+1]) % 100 == 43)) or ((len(str(abs(string[i+2]))) == 5) and (abs(string[i+2]) % 100 == 43))):

        sum_three_2 = string[i] ** 2 + string[i+1] ** 2 + string[i+2] ** 2
        if sum_three_2 < max(max_el) ** 2:
            k += 1
            otv_2.append(sum_three_2)

print(k, min(otv_2))


f = open("17_2_5.txt")
string=[int(x) for x in f]
k = 0
l = []
for i in range(len(string) - 1):
    if string[i] % 43 == min(string) and string[i+1] % 43 == min(string):
        k += 1
        l.append(abs(string[i] - string[i+1]))
print(k, max(l))


f = open("17_2_6.txt")
string=[int(x) for x in f]
k = 0
otv_2 = []
for i in range(len(string) - 2):
    l = []  #тут же можно было взять переменную, как счётчик, её итерировать
    #список используем для зранения значений, которые нам могут понадобиться, а не для "счётчика"
    for x in (string[i], string[i+1], string[i+2]):
        if str(x).count('0') == 0:
            l.append(1)
    if l.count(1) >= 2:
        if string[i] + string[i+1] + string[i+2] < max(string) / 2: #через and объединить
            k += 1
            otv_2.append(string[i] + string[i+1] + string[i+2])
print(k, max(otv_2))






f = open("17_2_7.txt")
string=[int(x) for x in f]
k = 0
otv_2 = []

for i in range(len(string) - 1):
    if (string[i] % 3 == max(string) % 3) or (string[i+1] % 3 == max(string) % 3):
        if (string[i] % 7 == min(string) % 7) or (string[i+1] % 7 == min(string) % 7):
            k += 1
            otv_2.append(string[i] + string[i+1])
print(k, max(otv_2))

f = open("17_2_8.txt")
string = [int(x) for x in f]

max_val = max(string)
k = 0
otv_2 = []

for i in range(len(string) - 1):
    curr_index = i + 1
    next_index = i + 2

    if (curr_index + next_index) % 10 == max_val % 10:
        k += 1

        sum_elements = string[i] + string[i + 1]
        sum_indices = curr_index + next_index

        diff = abs(sum_elements - sum_indices)
        otv_2.append(diff)
print(k, min(otv_2))



f = open("17_2_9.txt")
string = [int(x) for x in f]
k = 0
otv_2 = []
l_13 = []

for x in string:    #лучше так вообще не называть, выглядит как резервное имя
    if abs(x) % 10 == 3 and len(str(abs(x))) == 3:
        l_13.append(x)

max_el = max(l_13)  #нам этот список никак не нужен, можно было через переменную, которую перезаписывать с max()

for i in range(len(string) - 2):
    #там условие для одного числа
    if (abs(string[i]) % 10 == 3 and len(str(abs(string[i]))) == 3) or (abs(string[i+1]) % 10 == 3 and len(str(abs(string[i+1]))) == 3) or (abs(string[i+2]) % 10 == 3 and len(str(abs(string[i+2]))) == 3):
        if (string[i] + string[i+1] + string[i+2]) < max_el:
            k+=1
            otv_2.append(string[i] + string[i+1] + string[i+2])
print(k, max(otv_2))



f = open("17_2_10.txt")
string = [int(x) for x in f]
k = 0
otv_2 = []
l_min = []
for x in string:
    if len(str(x)) == 2 and (x % sum(int(p) for p in str(x))) == 0:
        l_min.append(x)
min_el = min(l_min)


for i in range(len(string) - 1):
    if string[i] % min_el == 0 or string[i+1] % min_el == 0:
        k += 1
        otv_2.append(string[i] + string[i+1])
print(k, max(otv_2))












