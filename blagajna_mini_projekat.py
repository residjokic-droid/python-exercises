import sys
ukupan_racun = 0
stavke = []
while True:
    stavka = input("Ukucaj naziv stavke (odustani za izlaz, gotovo za kraj):")
    if stavka.lower() == "odustani":
        sys.exit()
    if stavka.lower() == "gotovo":
        break
    cena = 0
    while cena <=0:
        cena_tekst = input(f"Kolika je cena {stavka}: ")
        try:
            cena = int(cena_tekst)
            if cena <=0:
                print(f"Neispravan unos cene za {stavka}")
        except ValueError:
            print(f"Moras uneti ceo broj za cenu")
    kolicina = 0
    while kolicina <=0:
        kolicina_tekst = input(f"Kolika je kolicina za {stavka}: ")
        try:
            kolicina = int(kolicina_tekst)
            if kolicina <=0:
                print(f"Uneli ste neispravan unos za kolicinu")
        except ValueError:
            print(f"Morate uneti ceo broj za kolicinu")
    stavke.append({"naziv": stavka, "cena": cena, "kolicina": kolicina})
    racun = (cena*kolicina)
    print(f"Racun za {stavka} iznosi: {racun}")
    ukupan_racun = (ukupan_racun+racun)
manji_popust = (ukupan_racun*10/100)
veci_popust = (ukupan_racun*20/100)
ukupan_racun_manji_popust = (ukupan_racun-manji_popust)
ukupan_racun_veci_popust = (ukupan_racun-veci_popust)
for pice in stavke:
    iznos = pice["cena"] * pice["kolicina"]
    print(f"{pice['naziv']}: {pice['cena']} * {pice['kolicina']} = {iznos}")
if ukupan_racun <=1000:
    print(f"Ne dobijate popust, Vas iznos za placanje iznosi: {ukupan_racun:.2f}")
elif ukupan_racun <=3000:
    print(f"Dobijate popust od {manji_popust:.2f} na Vas racun od {ukupan_racun:.2f}, Vas iznos za placanje iznosi: {ukupan_racun_manji_popust:.2f}")
else:
    print(f"Dobijate popust od {veci_popust:.2f} na Vas racun od {ukupan_racun:.2f}, Vas iznos za placanje iznosi: {ukupan_racun_veci_popust:.2f}")