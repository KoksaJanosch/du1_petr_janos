from math import radians 
from turtle import screensize, speed, penup, pendown, setpos, seth, forward, exitonclick, circle

poledniky_list = []
rovnobezky_list = []


# TODO: X 
def poledniky(R, meritko, zobrazeni_input):
    """ Vypíše seznam poledníků zvoleného zobrazení """

    # poledníky v rozsahu -180 až po 180, po 10
    for poledniky_deg in range(-180, 190, 10):
        if zobrazeni_input == "Ma" or zobrazeni_input == "Po": # ! Marinovo
            poledniky_x = round(R * (radians(poledniky_deg)) * 1000000 / meritko, 1)
        elif zobrazeni_input == "La": # ! Lambertovo: kuželové
            pass
        elif zobrazeni_input == "Sa": # ! Sansonovo: nepravé 
            pass
        else:
            exit()

        # přidá souřadnici do seznamu
        poledniky_list.append(poledniky_x)

    # vrátí konečný seznam s poledníky
    return(poledniky_list)

# TODO: Y
def rovnobezky(R, meritko, zobrazeni_input):
    """ Vypíše seznam rovnoběžek voleného zobrazení """
    
    # rovnoběžky v rozsahu -90 až 90
    for rovnobezky_deg in range(-90, 100, 10):
        if zobrazeni_input == "Ma" or zobrazeni_input == "Po": # ! Marinovo / Postelovo
            rovnobezky_y = round(R * (radians(rovnobezky_deg)) * 1000000 / meritko, 1)
        else:
            quit()

        # přidá souřadnici do seznamu
        rovnobezky_list.append(rovnobezky_y)

    # vrátí konečný seznam s rovnoběžkami
    return (rovnobezky_list)



# TODO: Gafika
def grafika(rovnobezky_list, poledniky_list, zobrazeni_input):
    delka_polednik = abs(max(rovnobezky_list) - min(rovnobezky_list))
    delka_rovnobezka = abs(max(poledniky_list) - min(poledniky_list))
    speed(200)
    screensize(1260, 891)

    if zobrazeni_input == "Ma":
        for i in range(37):
            penup()
            setpos(poledniky_list[i], rovnobezky_list[0])
            seth(90)
            pendown()
            forward(delka_polednik)
            penup()
        for j in range(19):
            setpos(poledniky_list[0], rovnobezky_list[j])
            seth(0)
            pendown()
            forward(delka_rovnobezka)
            penup()
        exitonclick()
    elif zobrazeni_input == "Po":
        for deg in range(0, 370, 10):
            seth(deg)
            forward(delka_polednik)
            penup()
            seth(deg-180)
            forward(delka_polednik)
            pendown()
        for x in range(19):
            penup()
            setpos(0,poledniky_list[x])
            pendown()
            circle(poledniky_list[x]) 
        exitonclick()
    else:
        pass



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

# Poloměra
while True:
    R = float(input("\nZadejte poloměr Zěmě (zadejte nulu pro výchozí poloměr 6371.11): \n"))
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
        meritko = int(input("\nZadejte měřítko (pro výchozí 1 : 100000000 zadejte nulu): \n"
        "1 : "))
        if meritko < 0:
            print("zadané měřítko je chybné, zkuste to znovu \n")
            continue
        elif meritko == 0:
            meritko = 100000000
            break
        else:
            break
        

# TODO: Volání funkcí
poledniky(R, meritko, zobrazeni_input)
rovnobezky(R, meritko, zobrazeni_input)
grafika(rovnobezky_list, poledniky_list, zobrazeni_input)
