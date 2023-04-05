# prg_7_a - priklad na procviceni, vylepseny vypis


"""
U1
Vytvorte program, ktery pro uzivatelem zadane cislo vypise seznam vsech jeho prirozenych delitelu v mezich 1-10 vcetne.
Program se uzivatele zepta na cislo a nasledne vypise vsechny jeho prirozene delitele.

Vypis bude mit nasledujici format:
zadané číslo: X \t vypis cisel oddeleny mezerami

Pro cislo 50 bude vypis nasledujici:
zadané číslo: 50	1 2 5 10

napoveda k vypisu:
print("zadané číslo: {}".format(n), end="\t")
print(i, end=' ')
"""
def delitel(num):
    for i in range(1, 11):
        if num % i == 0:
            print(i, end=" ")

pocet = int(input("zadej počet čísel: "))

hodnoty = []
for j in range(pocet):
    a = int(input("zadej {}. číslo: ".format(j+1)))
    hodnoty.append(a)

#print(hodnoty)

for h in hodnoty:
    print("zadané číslo: {}".format(h), end="\t")
    delitel(h)
    print()





#print("zadané číslo: {}".format(n), end="\t")









"""
U2
Upravte program tak, aby uzivatel mohl na zacatku zadat vice cisel, pro ktere chce najit delitele.
Program bude fungovat tak, ze uzivatel nejprve zada pocet cisel, pro ktere bude chtit vypocet provest.
Nasledne bude programem vyzvan, aby zadal postupne jednotliva cisla.
Po zadani daneho poctu hodnot program vypise najednou cele reseni ve stejnem formatu jako vyse.
Cast pro hledani delitelu implementujte jako funkci, jejimz vstupnim parametrem je dane cislo.
"""






