import numpy as np


# f = open('souradnice.csv', 'w')
#
# f.write('cb;y;x\n')
#
# for i in range(50):
#
#     y = 745100 + np.random.random()*50
#     x = 1045300 + np.random.random()*50
#
#     f.write('{};{};{}\n'.format(4001+i, y, x))

# f = open('mereni.csv', 'w')
#
# f.write('stanovisko;orientace;bod;delka;uhel\n')
#
# for i in range(100):
#
#     st = np.random.randint(4001, 4050)
#     ori = np.random.randint(4001, 4050)
#
#     delka = np.random.random()*50+20
#     uhel = np.random.random()*400
#
#     f.write('{};{};{};{};{}\n'.format(st, ori, i+1, delka, uhel))

def nactiBody(soubor: str) -> dict:

    body = {}

    with open(soubor, 'r') as f:
        for line in f.read().splitlines():
            if line[0] != 'c':
                cb, y, x = line.split(';')

                bod = {}

                bod['y'] = float(y)
                bod['x'] = float(x)

                body[cb] = bod

    return body

def nactiMereni(soubor: str) -> list:

    mereni = []

    with open(soubor, 'r') as f:
        for line in f.read().splitlines():
            if line[0] != 's':
                stanovisko, orientace, bod, delka, uhel = line.split(';')

                zamera = {}

                zamera['stanovisko'] = stanovisko
                zamera['orientace'] = orientace
                zamera['bod'] = bod
                zamera['delka'] = float(delka)
                zamera['uhel'] = float(uhel)

                mereni.append(zamera)

    return mereni

def grady2rad(uhel: float) -> float:
    return uhel*np.pi/200

def rad2grady(uhel: float) -> float:
    return uhel*200/np.pi

def smernik(stanovisko: dict, cil: dict) -> float:

    dy = cil['y'] - stanovisko['y']
    dx = cil['x'] - stanovisko['x']

    w = np.arctan2(dy, dx)

    if w < 0:
        w += 2*np.pi

    return w

def rajon(stanovisko: dict, orientace: dict, delka: float, uhel: float) -> dict:

    w = smernik(stanovisko, orientace)

    y = stanovisko['y'] + delka*np.sin(uhel+w)
    x = stanovisko['x'] + delka*np.cos(uhel+w)

    bod = {}
    bod['y'] = y
    bod['x'] = x

    return bod


body = nactiBody('souradnice.csv')

for zamera in nactiMereni('mereni.csv'):

    stanovisko = body[zamera['stanovisko']]

    orientace = body[zamera['orientace']]

    bod = rajon(stanovisko, orientace, zamera['delka'], zamera['uhel'])

    body[zamera['bod']] = bod
