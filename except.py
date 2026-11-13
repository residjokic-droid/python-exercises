while True:
    try:
        cena = int(input("Kolika je cena: "))
        break
    except ValueError:
        print("Moras ukucati ceo broj")