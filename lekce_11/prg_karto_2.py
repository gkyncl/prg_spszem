# prg_karto_2
import math
import matplotlib.pyplot as plt

PI = math.pi
R = 6371.11

# vykreslete sit pro Lambertovo valcove tecne zobrazeni
# zaroven vykreslete kontinenty - viz prilozene soubory
# rovnobezky i poledniky kreslete po 10 stupnich

# marinovo
#x = r*arc lam
#y = r*arc fi

def lambert(u,v):
    u_rad = u * PI / 180
    v_rad = v * PI / 180
    #x = R * v_rad
    #y = R * u_rad
    x = R * v_rad
    y = R * math.sin(u_rad)
    return x,y

def draw_continent(txt_file):
    kont_X = []
    kont_Y = []
    with open(txt_file) as file:
        for row in file:
            a = row.split()
            u = float(a[0])
            v = float(a[1])
            x, y = lambert(u, v)
            kont_X.append(x)
            kont_Y.append(y)
    plt.plot(kont_X, kont_Y, color="red")

# rovnobezky
# u - konst. <-90;90> po 10 st.
# v <-180;180> po 10 st.
#[u, -180], [u, -170]
#[u, u, u, ]
#[-180, -170, ...]

rovn_X = []
rovn_Y = []

v_list = [v for v in range(-180,181,10)]
for u_i in range(-90,91,10):
    u_list = [u_i for j in range(-180,181,10)]

    # aplikace zobrazeni
    for ix in range(len(v_list)):
        x,y = lambert(u_list[ix], v_list[ix])
        rovn_X.append(x)
        rovn_Y.append(y)
    plt.plot(rovn_X, rovn_Y, color="black")
    rovn_X = []
    rovn_Y = []

# poledniky
u_list = [v for v in range(-90,91,10)]
for v_i in range(-180,181,10):
    v_list = [v_i for j in range(-90,91,10)]

    # aplikace zobrazeni
    for ix in range(len(v_list)):
        x,y = lambert(u_list[ix], v_list[ix])
        rovn_X.append(x)
        rovn_Y.append(y)
    plt.plot(rovn_X, rovn_Y, color="black")
    rovn_X = []
    rovn_Y = []

draw_continent("afrika.txt")
draw_continent("eurasie.txt")





plt.axis("equal")
plt.show()



