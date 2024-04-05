def f(n):
    n_bin = f'{n:b}'    #перевели в 2-ную систему
    if n % 2 == 0:  #проверка чётности
        n_bin = n_bin + '01'    #дописываем значения
    else:
        n_bin = n_bin + '10'
    return int(n_bin, 2)    #возвращаем в десятичной системе ответ


r_min = 1000
for n in range(1000):
    r = f(n)
    if r < r_min and r > 130:
        r_min = r

print(r_min)
