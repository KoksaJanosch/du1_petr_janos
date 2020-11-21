from math import radians
from turtle import screensize, speed, penup, pendown, setpos, seth, forward, exitonclick, circle

# konstatna MM - přepočet na milimetry



# TODO: Funkce pro jednotlivá zobrazení
def Marinovo(R, meritko):
    """ Vytvoří seznam souřadnic k Marinovu zobrazení """
    MM = 10000000 # km » mm: 1.000.000 + převod měřítka: *10
    list_poledniky = []
    list_rovnobezky = []


    # poledniky
    for deg_x in range(-180, 190, 10):
        poledniky_x = round(R * (radians(deg_x)) * MM / meritko / 3, 1)
        list_poledniky.append(poledniky_x)
    
    # rovnobezky
    for deg_y in range(-90, 100, 10):
        rovnobezky_y = round(R * (radians(deg_y)) * MM / meritko / 3, 1)
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
    exitonclick()


def Postelovo(R, meritko):
    """ Vykreslí Postelovo zobrazení """
    MM = 10000000  # km » mm: 1.000.000 + převod měřítka: *10
    list_poledniky = []
    list_rovnobezky = []


    for deg_x in range(-180, 190, 10):
        poledniky_x = round(R * (radians(deg_x)) * MM / meritko / 3, 1)
        list_poledniky.append(poledniky_x)

    for deg_y in range(-90, 100, 10):
        rovnobezky_y = round(R * (radians(deg_y)) * MM / meritko / 3, 1)
        list_rovnobezky.append(rovnobezky_y)

    # * KRESLENÍ
    delka_polednik = abs(max(list_rovnobezky) - min(list_rovnobezky))
    print("delka poledniku", delka_polednik)
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
        setpos(0,list_poledniky[x])
        pendown()
        circle(list_poledniky[x]) 
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
        input("\nZadejte poloměr Zěmě (zadejte nulu pro výchozí poloměr 6371.11): \n"))
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

# ! volaní funkcí def
if zobrazeni_input == "Ma":
    print(Marinovo(R, meritko))

elif zobrazeni_input == "Po":
    print(Postelovo(R, meritko))
