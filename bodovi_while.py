bodovi = 150
while bodovi <0 or bodovi >100:
    bodovi_tekst = input("Ukucaj broj bodova: ")
    bodovi = int(bodovi_tekst)
    if bodovi <0 or bodovi >100:
        print(f"Neispravan unos {bodovi} bodova, pokusajte ponovo")
if bodovi <=50:
    print(f"Dobio si ocenu 1, jer imas {bodovi} bodova")
elif bodovi <= 70:
    print(f"Dobio si ocenu 2, jer imas {bodovi} bodova")
elif bodovi <= 85:
    print(f"Dobio si ocenu 3, jer imas {bodovi} bodova")
else:
    print(f"Dobio si ocenu 4, jer imas {bodovi} bodova")

