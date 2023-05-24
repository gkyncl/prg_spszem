import matplotlib.pyplot as plt
import random
import time
import numpy as np


p = plt
lim = 7.5
p.axis('equal')
alfa_mesic = 0
alfa_zeme = 0
mesic_x = []
mesic_y = []
zeme_x = []
zeme_y = []
a = 5
b = 5
while True:
    p.clf()
    p.ylim([-lim, lim])
    p.xlim([-lim, lim])

    xzeme = a*np.cos(alfa_zeme)
    yzeme = b*np.sin(alfa_zeme)

    zeme_x.append(xzeme)
    zeme_y.append(yzeme)

    xmesic = xzeme + 2*np.cos(alfa_mesic)
    ymesic = yzeme + 2 * np.sin(alfa_mesic)

    mesic_x.append(xmesic)
    mesic_y.append(ymesic)

    alfa_mesic += 0.09
    alfa_zeme += 0.01

    p.scatter(xzeme, yzeme, s=250, c='b')
    p.scatter(xmesic, ymesic, s=80, c='k')
    p.scatter(0, 0, s=500, c='y')
    p.plot(mesic_x, mesic_y, '+k')
    p.plot(zeme_x, zeme_y, '+b')
    # p.axis('equal')
    p.pause(0.01)
p.show()








# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

# # Načtení obrázku
# image_path = 'earth.jpg'  # Změňte cestu a název souboru na váš obrázek
# img = mpimg.imread(image_path)
#
# # Vytvoření grafu
# fig, ax = plt.subplots()
#
# # Vykreslení obrázku na souřadnicích
# x = [1, 2, 3]  # Souřadnice x
# y = [2, 3, 1]  # Souřadnice y
#
# # Vykreslení obrázku na zadaných souřadnicích
# for i in range(len(x)):
#     ax.imshow(img, extent=(x[i]-0.5, x[i]+0.5, y[i]-0.5, y[i]+0.5), aspect='auto')
#
# # Nastavení popisků os
# plt.xlabel('x')
# plt.ylabel('y')
#
# # plt.ylim([-1000, 1000])
#
# # Zobrazení grafu
# plt.show()


