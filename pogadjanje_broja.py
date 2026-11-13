import random
broj = random.randint(1,100)
pokusaji = 0
while True:
    pogodi_broj_tekst = input("Pogodi broj: ")
    pogodi_broj = int(pogodi_broj_tekst)
    pokusaji = pokusaji + 1
    if pogodi_broj>broj:
        print(f"Previse")
    elif pogodi_broj<broj:
        print(f"Premalo")
    elif pogodi_broj==broj:
        print(f"Pogodio si")
        break
print(f"Ukucao si {pokusaji} puta")
 
