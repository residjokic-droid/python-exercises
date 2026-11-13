cena_tekst = input("Kolika je cena?")
cena = int(cena_tekst)
kolicina_tekst = input("Kolika je kolicina?")
kolicina = int(kolicina_tekst)
ukupan_racun_tekst = (cena*kolicina)
ukupan_racun = int(ukupan_racun_tekst)
popust = float(ukupan_racun*10/100)
racun_sa_popustom_tekst = (ukupan_racun-popust)
racun_sa_popustom = int(racun_sa_popustom_tekst)
if ukupan_racun > 1000:
    print(f"Dobijas popust od {popust:.2f} dinara i placas {racun_sa_popustom:.2f} dinara")
else:
    print(f"Placas po punoj ceni od {ukupan_racun}")
