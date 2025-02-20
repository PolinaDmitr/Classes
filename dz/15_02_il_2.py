#1
for n in range(4,10000):
    s = "1" + "2" * n
    while "12" in s or "322" in s or "222" in s:
        s = s.replace("12", "2", 1)
        s = s.replace("322", "21", 1)
        s = s.replace("222", "3", 1)
    summa = sum(int(i) for i in s)
    if summa == 15:
        print(n)
        break
        # Ответ: 37

#2

"""
Решил аналитически:
Если у нас 200 звездочек и каждая четверка заменяется на вопросительный знаки получается:
200/4 = 50
50 * 3 = 150 (3 - это тройка вопросительных знаков, которые появляются вместо четверок звездочек
Ответ: 150
"""

#3

for n in range(3,10000):
    s = "59" + "8" * n
    while "68" in s or "988" in s or "888" in s:
        s = s.replace("68", "8", 1)
        s = s.replace("988", "86", 1)
        s = s.replace("888", "9", 1)
    summa = sum(int(i) for i in s)
    if summa ** (1/3) == int(summa ** (1/3)):
        print(n)
        break
    # Ответ: 7

#5

for n in range(9999, 3, -1):
    s = "2" + "7" * n
    while "27" in s or "777" in s or "377" in s:
        s = s.replace("27", "7", 1)
        s = s.replace("777", "3", 1)
        s = s.replace("377", "72", 1)
    l = [int(i) for i in s]
    proizv = 1
    for i in s:
        proizv *= int(i)
    if proizv % 3 == 0 and proizv % 10 == 1:
        print(n)
        break

#6

s = '6' * 666
while "666" in s or "111" in s:
    if "666" in s:
        s = s.replace('66', "1", 1)
    else:
        s = s.replace("111", "6", 1)
print(s)

#7

s = "9" * 136
while "9999" in s or "22222" in s:
    if "22222" in s:
        s = s.replace("22222", "99", 1)
    else:
        s = s.replace("9999", "2", 1)

int_9_count = 136
final_9_count = s.count("9")
removed_9 = int_9_count - final_9_count

print(removed_9)


#8

s = '8' * 140
while '888' in s or "2222" in s:
    if "2222" in s:
        s = s.replace('2222', "88")
    else:
        s = s.replace("888", "22")
print(s)







