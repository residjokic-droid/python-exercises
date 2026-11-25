import sys
def unesi_racunsku_operaciju(poruka):
    while True:
        operacija = input(poruka).lower()
        if operacija == "mnozenje" or operacija == "deljenje" or operacija == "sabiranje" or operacija == "oduzimanje":
            return operacija
        elif operacija == "ugasi":
            sys.exit()
        else:
            print("Morate uneti tacnu racunsku operaciju")
def unesi_broj(uneti):
    while True:
        try:
            broj = float(input(uneti))
            return broj
        except ValueError:
            print("Moras uneti broj, ne smes tekst!")
while True:
    racunske_operacije = unesi_racunsku_operaciju("Odaberi racunsku operaciju(ugasi za gasenje kalkulatora): ")
    broj_jedan = unesi_broj("Koliko iznosi prvi broj: ")
    broj_dva = unesi_broj("Koliko iznosi drugi broj: ")
    if racunske_operacije == "mnozenje":
        print(broj_jedan*broj_dva)
    elif racunske_operacije == "deljenje":
        if broj_dva == 0:
            print("Broj dva ne sme biti 0")
        else:
            print(broj_jedan/broj_dva)
    elif racunske_operacije == "sabiranje":
        print(broj_jedan+broj_dva)
    elif racunske_operacije == "oduzimanje":
        print(broj_jedan-broj_dva)
        

    
