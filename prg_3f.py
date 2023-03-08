# prg_3_f - podminky

# U5
# - upravte skript pro vypocet korenu kvadraticke rovnice, tak aby umel resit vsechny mozne situace
# - na vstupu budou uzivatelem zadane parametry a,b,c
# - program na zaklade diskriminantu vyhodnoti jestli a pripadne kolik ma rce reseni
# - v pripade, ze nema zadne reseni, tak informuje uzivatele
# - ve zbylych pripadech vypocte koreny a vysledek vypise
# - predpokladejte, ze uzivatel zada vstupni hodnoty rozumne - budou to cisla
# - program by tedy NEMEL skoncit chybou

# - testovani: -2x^2 - 15x + 8 = 0, K = (-8, 0.5); 9y^2 + 12y + 4 = 0, K = (-0.6666); x^2 + x + 1 = 0, K = (nema v R reseni)

# vstupni hodnoty
a = ...
b = ...
c = ...

# diskriminant
d = (b**2)-(4*a*c)

# vyhodnoceni hodnoty d


# reseni
x_1 = (-b + d**0.5)/(2*a)
x_2 = (-b - d**0.5)/(2*a)

# tisk reseni
print(...)