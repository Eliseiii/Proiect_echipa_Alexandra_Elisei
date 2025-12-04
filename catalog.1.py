pycatalog = [] 

def adauga_nota():
    nume=input("nume elev: ")
    nota=float(input("nota: "))
    catalog.append((nume, nota))
    print("nota adaugata.\n")

def afiseaza_catalog():
    if not catalog:
        print("catalog gol.\n")
        return

    print("catalog elevi")
    for nume, nota in catalog:
        print(nume, nota, end=" ")

def cauta_elev():
    nume_cautat=input("nume elev cautat: ")
    gasit = False

    for nume, nota in catalog:
        if nume==nume_cautat:
            if not gasit:
                print(f"nume elev: {nume_cautat}")
                gasit = True
            print(f"nota: {nota}")

    if not gasit:
        print("elevul nu exista\n")

while True:
    print("1.adauga nota")
    print("2.afiseaza catalogul")
    print("3.cauta elev")
    print("4.terminat")
    opt=input("optiune: ")

    if opt=="1":
        adauga_nota()
    elif opt=="2":
        afiseaza_catalog()
    elif opt=="3":
        cauta_elev()
    elif opt=="4":
        break
    else:
        break

