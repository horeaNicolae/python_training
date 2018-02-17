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

printNumarInvers()
