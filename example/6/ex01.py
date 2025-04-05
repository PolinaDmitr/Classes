from turtle import *

tracer(0)
k = 15
screensize(3000, 3000)

left(90)
for i in range(9):
    forward(27 * k)
    right(90)
    forward(30 * k)
    right(90)
up()
forward(3 * k)
right(90)
forward(6 * k)
left(90)
down()
for i in range(9):
    forward(77 * k)
    right(90)
    forward(66 * k)
    right(90)
up()

for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(5)
done()
