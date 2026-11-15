stavke = []
stavke.append({"naziv": "kafa", "cena": 120, "kolicina": 2})
stavke.append({"naziv": "sok", "cena": 85, "kolicina": 2})

for proizvod in stavke:
    iznos = proizvod["cena"] * proizvod["kolicina"]
    print(f"{proizvod['naziv']}: {proizvod['cena']} * {proizvod['kolicina']} = {iznos}")