cena_tekst = input("Kolika je cena?")
cena = int(cena_tekst)
kolicina_tekst = input("Kolika je kolicina?")
kolicina = int(kolicina_tekst)
ukupan_racun = int(cena*kolicina)
manji_popust = (ukupan_racun*10/100)
racun_sa_manjim_popustom = (ukupan_racun-manji_popust)
veci_popust = (ukupan_racun*20/100)
racun_sa_vecim_popustom = (ukupan_racun-veci_popust)
if ukupan_racun <=1000:
    print(f"Ne dobijate popust i Vas racun je {ukupan_racun} dinara")
elif ukupan_racun <=3000:
    print(f"Dobijate popust od {manji_popust:.2f} i vas racun iznosi {racun_sa_manjim_popustom:.2f} dinara")
else: 
    print(f"Dobijate popust od {veci_popust:.2f} i  Vas racun iznosi {racun_sa_vecim_popustom:.2f} dinara")