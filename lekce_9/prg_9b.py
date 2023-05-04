# Napiste kod, ktery spocita zapisnik mereni ze souboru 'mereni.csv'
# Souradnice stanovisek a orientaci jsou v souboru 'souradnice.csv'

# pro vypocet bude vyuzito co nejvice struktury slovniku

import math

def nactiBody(soubor: str) -> dict:

    body = {}

    with open(soubor, 'r') as f:

        for radek in f.read().splitlines():
            if radek[0] != 'c':

                cb, y, x = radek.split(';')

                bod = {}
                bod['y'] = float(y)
                bod['x'] = float(x)

                body[cb] = bod

    return body

def nactiMereni(soubor: str) -> list:

    mereni = []

    with open(soubor, 'r') as f:
        for radek in f.read().splitlines():
            if radek[0] != 's':

                stanovisko, orientaci, bod, delka, uhel = radek.split(';')

                zamera = {}

                zamera['stanovisko'] = stanovisko
                zamera['orientace'] = orientaci
                zamera['bod'] = bod
                zamera['delka'] = float(delka)
                zamera['uhel'] = float(uhel)

                mereni.append(zamera)

    return mereni

def smernik(stanovisko: dict, cil: dict) -> float:

    dy = cil['y'] - stanovisko['y']
    dx = cil['x'] - stanovisko['x']

    w = math.atan2(dy, dx)

    if w < 0:
        w += math.pi

    return w

def grady2rad(uhel: float) -> float:
    return uhel*math.pi/200

def rad2grady(uhel: float) -> float:
    return uhel*200/math.pi

def rajon(stanovisko: dict, orientace: dict, delka: float, uhel: float) -> dict:

    w = smernik(stanovisko, orientace)

    y = stanovisko['y'] + delka*math.sin(w+uhel)
    x = stanovisko['x'] + delka*math.cos(w+uhel)

    bod = {}
    bod['y'] = y
    bod['x'] = x

    return bod

body = nactiBody('souradnice.csv')

mereni = nactiMereni('mereni.csv')

for zamera in mereni:

    stanovisko = body[zamera['stanovisko']]

    orientace = body[zamera['orientace']]

    uhel_rad = grady2rad(zamera['uhel'])

    bod = rajon(stanovisko, orientace, zamera['delka'], uhel_rad)

    body[zamera['bod']] = bod


for bod, souradnice in body.items():
    print('Souradnice bodu {} jsou y={:.3f}, x={:.3f}'.format(bod, souradnice['y'], souradnice['x']))
