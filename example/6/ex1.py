# Повтори 8 [Вперёд 16 Направо 90 Вперёд 22 Направо 90]
# Поднять хвост
# Вперёд 5 Направо 90 Вперёд 5 Налево 90
# Опустить хвост
# Повтори 8 [Вперёд 52 Направо 90 Вперёд 77 Направо 90]
from turtle import *

screensize(2000, 2000)  #для ползунков на экране
tracer(0)   #не было отрисовки
k = 20  #управляемый масштаб
left(90)    #изначальное направление в задании

for _ in range(8):
    forward(16 * k)
    right(90)
    forward(22 * k)
    right(90)
up()
forward(5 * k)
right(90)
forward(5 * k)
left(90)
down()
for _ in range(8):
    forward(52 * k)
    right(90)
    forward(77 * k)
    right(90)

#отрисовка координатной плоскости
up()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(5)



done()  #не завершаем