import random
# prg_7_c - cyklus while priklady

"""
U3
Vytvorte program - hru, kdy uzivatel hada cislo.
Program vybere nahodne cislo od 0 do 20.
Nasledne uzivatel tipuje, dokud cislo neuhodne. Pokud uhodne, program vypise, ze cislo bylo uhodnuto.

generovani nahodnych cisel - knihovna random
import random
a = random.randint(0,20)
"""
"""
cislo = random.randint(0,20)
a = -1
while a != cislo:
    a = int(input("hádej číslo: "))
    if a > cislo:
        print("hledej menší")
    elif a < cislo:
        print("hledej větší")
    else:
        print("uhodl jsi číslo!")


#print("uhodl jsi číslo!")
"""

"""
U4
Upravte program tak, ze uzivatel bude hadat cislo v rozmezi 0 az 100. 
Program uzivatele pri kazdem pokusu informuje, jestli je jeho tip vetsi/mensi nez zadane cislo.
"""

"""
U5
Upravte uvodni program pro hledani delitelu, aby mohl uzivatel zadat libovolny pocet cisel.
Pokud bude chtit uzivatel se zadanim cisel skoncit, zada hodnotu -1 a program vypise vysledky.

"""
while True:
    a = int(input("číslo: "))
    if a == -1:
        break
    else:
        print(a)