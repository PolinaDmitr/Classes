#список
l1 = []
l2 = list()
l3 = [0] * 10
print(l1, l2, l3)

sqr = []
for i in range(10):
    sqr.append(i ** 2)  #добавить в список
print(sqr)
for i in range(10, 15):
    sqr.insert(0, i ** 2)   #вставить на конкретную позицию
print(sqr)

print(sqr.count(4))     #найти вхождение
print(max(sqr), min(sqr), len(sqr), sum(sqr))
sqr.sort()      #сортировка по возрастанию
print(sqr)
sqr.sort(reverse=True)      #сортировка по убыванию
print(sqr)
sqr.append(986)
print(sqr)
sqr.reverse()           #перевернуть список
print(sqr)

s1 = ['eneio', 'woedjwpoe', 'weiohiowe', 'wnjw']
print(s1)
print((s1[0])[1])
s1.append(s1[0] + s1[1])
print(s1)