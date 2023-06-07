import math
import matplotlib.pyplot as plt

# TODO:
# - kresba rovnobezek a poledniku do oddelenych funkci, vhodne definovat meze pro kresbu site a kontinentu
# - jednotliva zobrazeni do dilcich funcki v ramci modulu - proj_tools.py
#   - parametrem funkce bude i zobrazeni
#       >>> proj = globals()[sys.argv[5]]
# - import modulu s funkcemi pro zobrazeni
# - vytvorit program pro prikazovy radek - import modulu sys
# - prace s parametry prikazove radky
# - doplnit azimutalni zobrazeni - gnomonicka a stereograficka projekce

# co bude zde:
# - import knihoven, modulu
# - zpracovani parametru prikazove radky
# - volani potrebnych funkci pro vykresleni site a kontinentu
# - vykresleni grafu
"""
prikazy pro vykresleni

if proj in [stereo, gnom]:
    x_m, y_m = proj(u_min, v_min)
    x_min = -x_m
    x_max = x_m
    y_min = -x_m
    y_max = x_m
else:
    x_min, y_min = proj(u_min, v_min)
    x_max, y_max = proj(u_max, v_max)

plt.axis([x_min, x_max, y_min, y_max])
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
"""

