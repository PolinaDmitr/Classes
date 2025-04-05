# Повтори 2 [Вперёд 24 Направо 90 Вперёд 10 Направо 90]
# Вперёд 3 Налево 90 Вперёд 13 Направо 90
# Повтори 2 [Вперёд 9 Направо 90 Вперёд 32 Направо 90]
from turtle import *


tracer(0)
screensize(2000, 2000)
k = 25

left(90)
for i in range(2):
    forward(24 * k)
    right(90)
    forward(10 * k)
    right(90)
forward(3 * k)
left(90)
forward(13 * k)
right(90)
for i in range(2):
    forward(9 * k)
    right(90)
    forward(32 * k)
    right(90)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(3)
done()