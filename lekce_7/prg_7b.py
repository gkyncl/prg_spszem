# prg_7_b - cyklus while

"""
cyklus while
- vyuziva se tehdy, neni-li predem znan pocet opakovani
- pocet opakovani je rizen definovanou podminkou

syntaxe:
while podminka:

    ...
    kod uvnitr probiha dokud zadana podminka plati
    ...

"""

# priklad - vypis cisel od 1 do 10 vcetne

a = -1
cislo = 4
while a != cislo:
    a = int(input("hádej číslo: "))

print("uhodl jsi číslo!")
