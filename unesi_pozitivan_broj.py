def kvadrat(broj):    # def definiste kao funkciju, a broj kao ulaz neki
    return broj * broj  # return daje ono sto funkcija zadaje, ovde nema jednako znaci skracujes

x = kvadrat(5) + kvadrat(5) # 4 ulazi kao "broj", a 16 izlazi i ide u x, a imamo i situaciju kada je x = kvadrat 5 posebno plus kvadrat 5 posebno i onda je to 25 + 25 ovako bi bilo kad bi stavilo samo kvadrat 5 samo 25.
print(x) 
