from math import cos, sin
from turtle import left, pendown, right, circle, forward, setpos, exitonclick, speed, seth, circle, penup

a = 100

for deg in range(0, 370,10):
    speed(50)
    seth(deg)
    forward(a)
    penup()
    seth(deg-180)
    forward(a)
    pendown()

for x in range (9)

exitonclick()



