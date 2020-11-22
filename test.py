from math import cos, radians, tan, sin
from turtle import screensize, speed, penup, pendown, setpos, seth, forward, exitonclick, circle, dot

# konstatna M - přepočet na milimetry
M = 100000

# TODO: Funkce pro jednotlivá zobrazení


def Marinovo(M, R, meritko):
    """ Vykreslí Marinovo zobrazení """
    list_poledniky = []
    list_rovnobezky = []

    # * Vzorce přepočteny na px a zaokrouhleny na 1 des. místo
    # poledniky
    for deg_x in range(-180, 190, 10):
        poledniky_x = round(R * (radians(deg_x)) * M / meritko / 3, 1)
        list_poledniky.append(poledniky_x)
    # rovnobezky
    for deg_y in range(-90, 100, 10):
        rovnobezky_y = round(R * (radians(deg_y)) * M / meritko / 3, 1)
        list_rovnobezky.append(rovnobezky_y)

    # * vykreslení zobrazení
    delka_polednik = abs(max(list_rovnobezky) - min(list_rovnobezky))
    delka_rovnobezka = abs(max(list_poledniky) - min(list_poledniky))
    speed(10)
    screensize(1260, 891)  # nastavení plátna
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
    """ Vykreslí zadané body do zobrazení. Vstupem seznamy souřadnic bodů."""

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

    # * Vzorce přepočteny na px a zaokrouhleny na 1 des. místo
    for deg_x in range(-180, 190, 10):
        poledniky_x = round(R * (radians(deg_x)) * M / meritko / 3, 1)
        list_poledniky.append(poledniky_x)

    for deg_y in range(-90, 100, 10):
        rovnobezky_y = round(R * (radians(deg_y)) * M / meritko / 3, 1)
        list_rovnobezky.append(rovnobezky_y)

    # * vykreslí zobrazení
    delka_polednik = abs(max(list_rovnobezky) - min(list_rovnobezky))
    speed(10)
    screensize(1260, 891)  # velikost plátna
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
    """ Vykreslí zadané body do zobrazení. Vstupem seznamy souřadnic bodů. """

    for p in range(len(body_X)):
        penup()
        setpos(body_X[p], body_Y[p])
        pendown()
        dot(10)
    exitonclick()

# ! TU
def Ptolemaiovo(R, meritko, M):

    ##########
    speed(10)
    for j in range(-90, 100, 10):
        penup()
        setpos(radians(30) - ( (R*M/meritko)*(1/tan(radians(30)))+(R*M/meritko)*(radians(30-j))) * cos((radians(-180)*sin(radians(30)))),
            ((R*M/meritko)*(1/tan(radians(30)))+(R*M/meritko)*(radians(30-j))) * sin((radians(-180)*sin(radians(30)))))
        pendown()
        for i in range(-180, 190, 10):
            setpos(radians(30) - ((R*M/meritko)*(1/tan(radians(30))) + (R*M/meritko)*(radians(30-j))) * cos((radians(i)*sin(radians(30)))), 
                   ((R*M/meritko)*(1/tan(radians(30)))+(R*M/meritko)*(radians(30-j))) * sin((radians(i)*sin(radians(30)))))
    for j in range(-180, 190, 10):
        penup() # !
        setpos(radians(30) - ((R*M/meritko)*(1/tan(radians(30))) + (R*M/meritko)*(radians(30-(-90)))) * cos((radians(j)*sin(radians(30)))),
            ((R*M/meritko)*(1/tan(radians(30)))+(R*M/meritko)*(radians(30-(-90)))) * sin((radians(j)*sin(radians(30)))))
        pendown()
        for i in range(-90, 100, 10):
            setpos(radians(30) - ((R*M/meritko)*(1/tan(radians(30))) + (R*M/meritko)*(radians(30-i))) * cos((radians(j)*sin(radians(30)))),
            ((R*M/meritko)*(1/tan(radians(30)))+(R*M/meritko)*(radians(30-i))) * sin(radians(j)*sin(radians(30))))
    
    exitonclick()

# ! TU

# TODO: Uživatelské vstupy
# * Výběr zobrazení
while True:
    zobrazeni_input = str(input('Nabízená zobrazení: \n'
                                ' Ma = Marinovo zobrazení (válcové)\n'
                                ' Po = Postelovo zobrazení (azimutální)\n'
                                ' Pt = Ptolemainovo zobrazení \n'
                                ' Sa = Sansonovo zobrazení \n'
                                '\nZadejte zkratku: '))
    if zobrazeni_input == "Ma" or zobrazeni_input == "Po" or zobrazeni_input == "Pt" or zobrazeni_input == "Sa":
        break
    else:
        print("!!! Nesprávný vstup, zadejte zobrazení z nabídky !!! \n")

# * Zadání poloměru
while True:
    R = float(
        input("\nZadejte poloměr Země (zadejte nulu pro výchozí poloměr 6371.11): \n"))
    if R < 0:  # chybně zadaný poloměr
        print("zadaný poměr je chybný, zkuste to znovu \n")
        continue
    elif R == 0:  # použití výchozího poloměru
        R = 6371.11
        break
    else:
        break

# * Zadání měřítka
while True:
    meritko = int(input("\nZadejte měřítko (pro výchozí 1:120 000 000 zadejte nulu): \n"
                        "1 : "))
    if meritko < 0:  # chybně zadané měřítko
        print("zadané měřítko je chybné, zkuste to znovu \n")
        continue
    elif meritko == 0:  # použití výchozího měřítka
        meritko = 120000000
        break
    else:
        break

# * Zadání bodů
body_X = []
body_Y = []

print("\nZadejte zeměpisnou šířku a výšku bodu, který chcete zaznamenat: \n"
      "(pro ukončení zadávání bodů napište souřadnice (0,0)\n")

while True:
    x = float(input("z. šířka bodu: "))
    y = float(input("z. výška bodu: "))

    # výpočet souřadnice bodu
    if zobrazeni_input == "Ma" or zobrazeni_input == "Po":
        if x > 0 or y > 0:
            souradnice_x = round(R * (radians(x)) * M / meritko / 3, 2)
            souradnice_y = round(R * (radians(y)) * M / meritko / 3, 2)
            print(
                "Přepočtené souřadnice: [", souradnice_x, ";", souradnice_y, "] \n")
            # přiřazení do seznamu (vstup pro vykreslení)
            body_X.append(souradnice_x)
            body_Y.append(souradnice_y)

        elif x == 0 and y == 0:  # opuštění cyklu souřadnicí (0,0)
            print("--konec zadávání bodů --")
            break
    else:
        break

# ! Volání funkcí:
if zobrazeni_input == "Ma":
    Marinovo(M, R, meritko)
    Marinovo_body(body_X, body_Y)

elif zobrazeni_input == "Po":
    Postelovo(M, R, meritko)
    Postelovo_body(R, meritko, body_X, body_Y)

elif zobrazeni_input == "Pt":
    Ptolemaiovo(R, meritko, M)

print("\n-- program byl úspěšně dokončen --")
