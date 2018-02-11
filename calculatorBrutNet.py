#!/usr/bin/env python


def calculatorBrutNet():
    #Functie get Salariu Brut
    def getSalariuBrut():
        salariuBrut = int(input("Salariul brut este de: "))
        return salariuBrut

    salariuBrut = getSalariuBrut()

    #Formula calculare deducerePersonala
    if salariuBrut <= 1950:
        dedPers = 510
    elif salariuBrut > 1950 and salariuBrut < 3600:
        dedPers = 345
    else:
        dedPers = 0

    # Valoare taxe CAS+CASS
    cas = 0.25
    cass = 0.10
    asig = cas + cass

    # Calculare venit impozabil
    venitImpoz = salariuBrut - (dedPers + asig * salariuBrut)
    impVenit = 0.10 * venitImpoz

    # Calculare salariu net
    salariuNet = (salariuBrut - asig * salariuBrut) - impVenit

    # Calculare contributie asiguratorie pentru munca
    capm = 0.0225 * salariuBrut

    #Printare informatii in fisier
    f = open("testfile.txt", "w+")
    f.write("Salariu brut: %d\r\n\r\n" % salariuBrut)
    f.write("Salariu net: %d\r\n\r\n" % salariuNet)

    f.write("Valoare CAS platit: %.2f.\r\n" % (cas * salariuBrut))
    f.write("Valoare CASS platit: %.2f.\r\n" % (cass * salariuBrut))

    f.write("\r\nValoarea deducerii personale este de %d.\r\n\r\n" % dedPers)
    f.write("Venit impozabil: %d\r\n" % venitImpoz)
    f.write("Impozitul pe venit: %d\r\n" % impVenit)

    f.write("Contributie asiguratorie pentru munca (angajator): %d\r\n" % capm)
    f.write("Costul total al angajatului pentru angajator: %d\r\n" % (salariuBrut + capm))

    f.close

    #Printare informatii in linia de comanda

    #print ('Salariul net este de: ' + salariuNet)
    print("salariul net este %s" %salariuNet)
    print("cass platit este %s" %cass*salariuBrut)

    print('\r\nSalariul net este de {}\r\n'.format(salariuNet))
    print('Valoare CAS platit este de: {}'.format(cas*salariuBrut))
    print('Valoare CASS platit este de: {}\r\n'.format(cass*salariuBrut))
    print('Valoarea deducerii personale este de: {}\r\n'.format(dedPers))
    print('Venit impozabil: {}'.format(venitImpoz))
    print('Impozitul pe venit: {}'.format(impVenit))
    print('Contributie asiguratorie pentru munca (angajator): {}'.format(capm))
    print('Costul total al angajatului pentru angajator: {}'.format(salariuBrut + capm))






# def calculatorNetBrut():
#     def getSalariuNet():
#         salariuNet = float(raw_input("Salariul net  | "))
#         return salariuNet
#
#     salariuNet = getSalariuNet()
#
#     #Formula calculare deducerePersonala
#     # if salariuBrut <= 1950:
#     #     dedPers = 510
#     # elif salariuBrut > 1950 and salariuBrut < 3600:
#     #     dedPers = 345
#     # else:
#     #     dedPers = 0
#
#     # Valoare taxe CAS+CASS
#     cas = 0.25
#     cass = 0.10
#     asig = cas + cass
#
#     # Calculare venit impozabil
#     venitImpoz = salariuBrut - (dedPers + asig * salariuBrut)
#     impVenit = 0.10 * venitImpoz
#
#     # Calculare salariu net
#     salariuNet = (salariuBrut - asig * salariuBrut) - impVenit
#
#     # Calculare contributie asiguratorie pentru munca
#     capm = 0.0225 * salariuBrut


calculatorBrutNet()
