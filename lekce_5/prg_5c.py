# prg_5b - tvorba funkci
# funkce - logicke bloky kodu, ktere slouzi k vykonani urcite operace
# vyhody pouziti:
# 1) srozumitelnost
# 2) opakovane pouziti
# 3) snadnejsi sprava kodu
# 4) efektivnost

# zapis funkce:
# zacina klicovym slovem "def"
# pote nasleduje nazev funkce + v kulatych zavorkach definice jejich vstupnich parametru + nakonec je potreba dvoujtecka
# na dalsim radku (+ tab) je definovano telo funkce
# na konci funkce je klicove slovo "return" a seznam navratovych hodnot oddelenych carkou
# funkce nemusi nutne vracet hodnoty, tak jako nemusi mit nutne vstupni parametry

# s ohledem na to, jak pracuje python, je nutne mit funkci definovanou drive nez je pouzita

# priklad: funkce ktera vraci soucet dvou cisel

def soucet(a, b):
    s = a + b
    return s

# priklady:
# 0) priklady z prechoziho souboru jako funkce
# 1) absolutni hodnota cisla
# 2) prumer hodnot z listu
# 3) prevod uhlovych jednotek grad2deg, deg2rad...
# 4) prevod uhlu v stupnich, minutach, vterinach do nonagezimalni miry
# 5)