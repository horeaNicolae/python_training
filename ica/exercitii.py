#!/usr/bin/env python


def printNumarInvers():

    numar = int(input("Introduceti numarul:"))

    listaCifre = []

    #ultima cifra dintr-un numar e restul impartirii numarului la 10
    #ex. 951 / 10 = 95 rest 1 => 1 ii ultima cifra
    #aflam ultima cifra, o punem intr-o lista, si o taiem din numarul initial
    #repetam pana cand numarul initial nu mai exista :D
    while numar > 0:
        ultimaCifra = numar % 10
        listaCifre.append(ultimaCifra)
        numar = numar // 10

    print(listaCifre)


def printNumarPeUnitati():

    numar = int(input("Introduceti numarul:"))

    listaCifre = []

    #ultima cifra dintr-un numar e restul impartirii numarului la 10
    #ex. 951 / 10 = 95 rest 1 => 1 ii ultima cifra
    #aflam ultima cifra, o punem intr-o lista (mereu pe indexul 0), si o taiem din numarul initial
    #repetam pana cand numarul initial nu mai exista :D
    while numar > 0:
        ultimaCifra = numar % 10
        listaCifre.insert(0, ultimaCifra)
        numar = numar // 10

    print(listaCifre)

printNumarInvers()

printNumarPeUnitati()






# 7. You look at the clock and it is exactly 2pm. You set an alarm to go off in 51 hours. At
# what time does the alarm go off? (Hint: you could count on your fingers, but this is not
# what we’re after. If you are tempted to count on your fingers, change the 51 to 5100.)

# 8. Write a Python program to solve the general version of the above problem. Ask the user
# for the time now (in hours), and ask for the number of hours to wait. Your program
# should output what the time will be on the clock when the alarm goes off.





import turtle
window = turtle.Screen()
alex = turtle.Turtle()

alex.forward(50)
alex.left(90)
alex.forward(30)

window.mainloop()
