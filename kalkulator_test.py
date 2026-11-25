def unesi_broj(poruka):
    while True:
        try:
            broj = int(input(poruka))
            if broj == broj:
                continue
            else:
                return broj
        except ValueError:
            print("Moras uneti broj, ne smes tekst!")