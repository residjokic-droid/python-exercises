import sys
def unesi_racunsku_operaciju(poruka):
    while True:
        operacija = input(poruka)
        if operacija == "mnozenje" or operacija == "deljenje" or operacija == "sabiranje" or operacija == "oduzimanje":
            return operacija
        elif operacija == "ugasi":
            sys.exit()
        else:
            print("Morate uneti tacnu racunsku operaciju")
while True:
    racunske_operacije = unesi_racunsku_operaciju("Odaberi racunsku operaciju(odustani za gasenje kalkulatora): ")
    broj_jedan_tekst = input("Koliko iznosi prvi broj: ")
    broj_dva_tekst = input("Koliko iznosi drugi broj: ")
    broj_jedan = float(broj_jedan_tekst)
    broj_dva = float(broj_dva_tekst)
    if racunske_operacije.lower() == "mnozenje":
        print(broj_jedan*broj_dva)
    elif racunske_operacije.lower() == "deljenje":
        print(broj_jedan/broj_dva)
    elif racunske_operacije.lower() == "sabiranje":
        print(broj_jedan+broj_dva)
    elif racunske_operacije.lower() == "oduzimanje":
        print(broj_jedan-broj_dva)
        

    
