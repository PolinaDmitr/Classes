for A in range(20, -1, -1):
    flag = True
    for x in range(1,50):
        for y in range(1,50):
            for z in range(1,50):
                if not((48 != (y + 2 * x + z)) or (A < x) or (A < y) or (A < z)):
                    flag = False
                    break
            if not flag:
                break
        if not flag:
            break
    if flag:
        print(A)
        break


for A in range(1000, 0, -1):
    flag = True
    for x in range(1, 1000):
        if (x % 18 == 0) and (x % A != 0) and (x % 12 == 0):
            flag = False
            break
    if flag:
        print(A)
        break


for A in range(1, 500):
    flag = True
    for x in range(0,500):
        for y in range(0, 500):
            if not(((2 * y + 5 * x) < A) or ((x + y) > 80)):
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)
        break



P_set = {1, 2, 3, 4, 5, 6}  #можно просто кортеж взять (не нужны особо преимущества множества)
Q_set = {3, 5, 15}


result_s = -1

for s in range(0, 10):

    if s < 2:
        continue
    A_candidate = {3, 5}
    flag = True
    for x in range(1, 20):
        x_in_A = x in A_candidate
        x_in_P = x in P_set
        x_in_Q = x in Q_set

        if (not x_in_A) and x_in_P and x_in_Q:

             flag = False
             break

    if flag:
        result_s = s
        break
print(result_s)



for a in range(1,500):
    flag = True
    for x in range(1, 700):
        if not(not((x % a == 0) and (x % 16 == 0)) or ((x % 16 != 0) or (x % 24 == 0))):
            flag = False
            break
    if flag:
        print(a)
        break


print(f'Ответ на  Задание 15.7: 14. Отрезок исходя из первого условия должен быть [-8, 8]. Исходя из второго условия, при решении неравенства у нас корни -6 и 8. Значит диапазон [-6;8]. Соответственно длина его 14')



for A in range(1, 1000):

    flag = True

    for X in range(1, 1000):
        cond1 = (X & 29 != 0)
        cond2 = (X & 17 == 0)
        cond3 = (X & A == 0)

        if cond1 and cond2 and cond3:
            flag = False
            break

    if flag:
        print(A)
        break


for a in range(1000, -1, -1):
    flag = True
    for x in range(1,1000):
        for y in range(1,1000):
            if not(((2 * y + 6 * x) != 2020) or (a < (x + 17)) or (a < (4 * y + 988))):
                flag = False
                break
        if not flag:
            break
    if flag:
        print(a)
        break




