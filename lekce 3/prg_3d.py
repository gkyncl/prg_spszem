# prg_3_d - vstup od uzivatele II

# U3
# - upravte skript na reseni kvadratickych rovnic z minula tak, aby vstupni hodnoty a, b, c byly zadany uzivatelem
# - testovani: -2x^2 - 15x + 8 = 0, K = (-8, 0.5)

# vstupni hodnoty
a = ...
b = ...
c = ...

# diskriminant
d = (b**2)-(4*a*c)

# reseni
x_1 = (-b + d**0.5)/(2*a)
x_2 = (-b - d**0.5)/(2*a)

# tisk reseni
print(...)