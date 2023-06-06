# prg_karto_1

# U1: Vytvorte jednoduchou funkci, ktera vykresli pomoci
# knihovny matplotlib kruznici o zadanem polomeru
import math
import matplotlib.pyplot as plt
PI = math.pi

RO = 5
eps = [i*PI/180 for i in range(361)]

X = [RO*math.cos(e) for e in eps]
Y = [RO*math.sin(e) for e in eps]

plt.plot(X,Y)
plt.axis("equal")
plt.show()






print(eps)