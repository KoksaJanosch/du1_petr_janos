from math import radians
from turtle import screensize, speed, penup, pendown, setpos, seth, forward, exitonclick, circle, dot

# konstatna M - přepočet na milimetry
M = 10000000

# TODO: Funkce pro jednotlivá zobrazení


def Marinovo(M, R, meritko):
    """ Vytvoří seznam souřadnic k Marinovu zobrazení """
    list_poledniky = []
    list_rovnobezky = []

    # poledniky
    for deg_x in range(-180, 190, 10):
        poledniky_x = round(R * (radians(deg_x)) * M / meritko / 3, 1)
        list_poledniky.append(poledniky_x)
    # rovnobezky
    for deg_y in range(-90, 100, 10):
        rovnobezky_y = round(R * (radians(deg_y)) * M / meritko / 3, 1)
        list_rovnobezky.append(rovnobezky_y)

    # * KRESLENÍ
    delka_polednik = abs(max(list_rovnobezky) - min(list_rovnobezky))
    delka_rovnobezka = abs(max(list_poledniky) - min(list_poledniky))
    speed(10)
    screensize(1260, 891)
    for i in range(37):
        penup()
        setpos(list_poledniky[i], list_rovnobezky[0])
        seth(90)
        pendown()
        forward(delka_polednik)
        penup()
    for j in range(19):
        setpos(list_poledniky[0], list_rovnobezky[j])
        seth(0)
        pendown()
        forward(delka_rovnobezka)
        penup()


def Marinovo_body(body_X, body_Y):
    M = 10000000  # km » mm: 1.000.000 + převod měřítka: *10

    for p in range(len(body_X)):
        penup()
        setpos(body_X[p], body_Y[p])
        pendown()
        dot(10)
    exitonclick()


def Postelovo(M, R, meritko):
    """ Vykreslí Postelovo zobrazení """
    list_poledniky = []
    list_rovnobezky = []

    for deg_x in range(-180, 190, 10):
        poledniky_x = round(R * (radians(deg_x)) * M / meritko / 3, 1)
        list_poledniky.append(poledniky_x)

    for deg_y in range(-90, 100, 10):
        rovnobezky_y = round(R * (radians(deg_y)) * M / meritko / 3, 1)
        list_rovnobezky.append(rovnobezky_y)

    # * KRESLENÍ
    delka_polednik = abs(max(list_rovnobezky) - min(list_rovnobezky))

    speed(10)
    screensize(1260, 891)
    for deg in range(0, 370, 10):
        seth(deg)
        forward(delka_polednik)
        penup()
        seth(deg-180)
        forward(delka_polednik)
        pendown()
    for x in range(19):
        penup()
        setpos(0, list_poledniky[x])
        pendown()
        circle(list_poledniky[x])


def Postelovo_body(body_X, body_Y):

    for p in range(len(body_X)):
        penup()
        setpos(body_X[p], body_Y[p])
        pendown()
        dot(10)
    exitonclick()


# TODO: Uživatelské vstupy
# Zobrazení
while True:
    zobrazeni_input = str(input('Nabízená zobrazení: \n'
                                ' Ma = Marinovo zobrazení \n'  # ? válcová tečná
                                ' Po = Postelovo zobrazení \n'  # ? azimutální
                                ' La = Lambertovo zobrazení \n'  # ? kuželová
                                ' Sa = Sansonovo zobrazení \n'  # ? nepravá
                                '\nZadejte zkratku: '))
    if zobrazeni_input == "Ma" or zobrazeni_input == "Po" or zobrazeni_input == "La" or zobrazeni_input == "Sa":
        break
    else:
        print("Nesprávný vstup, zadejte zobrazení z nabídky:")

# Poloměr
while True:
    R = float(
        input("\nZadejte poloměr Země (zadejte nulu pro výchozí poloměr 6371.11): \n"))
    if R < 0:
        print("zadaný poměr je chybný, zkuste to znovu \n")
        continue
    elif R == 0:
        R = 6371.11
        break
    else:
        break

# Měřítko
while True:
    meritko = int(input("\nZadejte měřítko (pro výchozí 1: 120 000 000 zadejte nulu): \n"
                        "1 : "))
    if meritko < 0:
        print("zadané měřítko je chybné, zkuste to znovu \n")
        continue
    elif meritko == 0:
        meritko = 120000000
        break
    else:
        break

# ! body
body_X = []
body_Y = []

print("Zadejte zeměpisnou šířku a výšku bodu, který chcete zaznamenat: \n"
      "(pro ukončení zadávání bodů napište souřadnice (0,0)")

while True:
    x = float(input("z. šířka bodu: "))
    y = float(input("z. výška bodu: "))

    if zobrazeni_input == "Ma" or zobrazeni_input == "Po":
        if x > 0 or y > 0:
            souradnice_x = round(R * (radians(x)) * M / meritko / 3, 2)
            souradnice_y = round(R * (radians(y)) * M / meritko / 3, 2)
            print(
                "Přepočtené souřadnice: [", souradnice_x, ";", souradnice_y, "] \n")
            body_X.append(souradnice_x)
            body_Y.append(souradnice_y)

        elif x == 0 and y == 0:
            print("--konec zadávání bodů --")
            break
    else:
        break

# ! volaní funkcí def
if zobrazeni_input == "Ma":
    print(Marinovo(M, R, meritko))
    print(Marinovo_body(body_X, body_Y))

elif zobrazeni_input == "Po":
    print(Postelovo(M, R, meritko))
    print(Postelovo_body(R, meritko, body_X, body_Y))
