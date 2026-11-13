bodovi_tekst = input("Koliko imam bodova?")
bodovi = int(bodovi_tekst)
minimalno_bodova = 0
maksimalno_bodova = 100
if bodovi <50:
    print(f"Dobio si ocenu 5, jer imas {bodovi} bodova")
elif bodovi <=59:
    print(f"Dobio si ocenu 6, jer imas {bodovi} bodova")
elif bodovi <=69:
    print(f"Dobio si ocenu 7, jer imas {bodovi} bodova")
elif bodovi <=79:
    print(f"Dobio si ocenu 8, jer imas {bodovi} bodova")
elif bodovi <=89:
    print(f"Dobio si ocenu 9, jer imas {bodovi} bodova")
else:
    print(f"Dobio si ocenu 10, jer imas {bodovi} bodova")
if bodovi <0 or bodovi >100:
    print(f"Minimalno bodova je {minimalno_bodova}, a maksimalno {maksimalno_bodova}")