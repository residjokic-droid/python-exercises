import sys
def unesi_pozitivan_broj(poruka):
    while True:
        try:
            broj = int(input(poruka))
            if broj <= 0:
                print("Broj mora biti veci od 0!")
            else:
                return broj
        except ValueError:
            print("Moras uneti ceo broj i ne smes tekst!")
ukupan_racun = 0
stavke = []
while True:
    stavka = input("Ukucaj naziv stavke (odustani za izlaz, gotovo za kraj):")
    if stavka.lower() == "odustani":
        sys.exit()
    if stavka.lower() == "gotovo":
        break
    cena = unesi_pozitivan_broj(f"Kolika je cena za {stavka}: ")
    kolicina = unesi_pozitivan_broj(f"Kolika je kolicina za {stavka}: ")
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