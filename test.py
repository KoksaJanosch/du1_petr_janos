from math import cos, radians, sin, pi
from turtle import left, pendown, right, circle, forward, setpos, exitonclick, speed, seth, circle, penup

R = 6371.11
meritko = 120000000
M = 10000000

konst = R * M /meritko / 3


""" 
# Y: výpočet rovnoběžek
for deg_y in range (-90, 100, 10):
    rovnobezky_y = round(R * radians(deg_y) * 10000000 / meritko / 3, 1)
    print(rovnobezky_y)

# X: výpočet poledníků
for deg_x in range(-180, 190, 10):
    poledniky_x = R * deg_x * cos()

 """


def sanson_print_parallel(u, ky):
    for v in range(0, 180, 10):
        if v == 0:
            penup()
        else:
            pendown()
        y = (R * radians(u))
        x = (R * radians(v) * cos(radians(u)))
        setpos(x, ky*y)
        setpos(-x, ky*y)


def sanson_print(v, kx, ky):
    for u in range(0, 100, 10):
        if u == 0:
            penup()
        else:
            pendown()
        y = (R * radians(u))
        x = (R * radians(v) * cos(radians(u)))
        setpos((kx*x), (ky*y))


def sanson(R):
    """FUNKCE PRO KRESBU SANSONOVA NEPRAVÉHO ZOBRAZENÍ"""
    for u in range(0, 90, 10):
        sanson_print_parallel(u, 1)
    for u in range(0, 90, 10):
        sanson_print_parallel(u, -1)
    for v in range(0, 180, 10):
        sanson_print(v, 1, 1)
        sanson_print(v, -1, 1)
        sanson_print(v, 1, -1)
        sanson_print(v, -1, -1)
