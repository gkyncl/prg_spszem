# Napiste kod, ktery spocita zapisnik mereni ze souboru 'mereni.csv'
# Souradnice stanovisek a orientaci jsou v souboru 'souradnice.csv'

# pro vypocet bude vyuzito co nejvice struktury slovniku

import math
import matplotlib.pyplot as plt

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
        w += 2*math.pi

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

body = nactiBody(r'c:\Users\Jakub\Desktop\prg_spszem\lekce_10\orientace.csv')

mereni = nactiMereni(r'c:\Users\Jakub\Desktop\prg_spszem\lekce_10\mereni.csv')

for zamera in mereni:

    stanovisko = body[zamera['stanovisko']]

    orientace = body[zamera['orientace']]

    uhel_rad = grady2rad(zamera['uhel'])

    bod = rajon(stanovisko, orientace, zamera['delka'], uhel_rad)

    body[zamera['bod']] = bod

def separovat_souradnice(body, seznam_bodu):

    x = []
    y = []

    for cb in body:
        bod = seznam_bodu[cb]

        x.append(-bod['y'])
        y.append(-bod['x'])

    return x, y


def polohopis(soubor: str):

    mapa = plt
    mapa.axis('equal')

    with open(soubor, 'r') as f:

        for radek in f.read().splitlines():

            cisla_bodu = radek.split(',')

            if cisla_bodu[0] == 'dum':

                obvod = cisla_bodu[1:]
                obvod.append(cisla_bodu[1])
                x, y = separovat_souradnice(obvod, body)

                mapa.plot(x, y, '-r')

            if cisla_bodu[0] == 'lampa':

                lampy = cisla_bodu[1:]

                x, y = separovat_souradnice(lampy, body)

                mapa.plot(x, y, '*b')

            if cisla_bodu[0] == 'cesta':

                cesta = cisla_bodu[1:]

                x, y = separovat_souradnice(cesta, body)

                mapa.plot(x, y, '-k')

            if cisla_bodu[0] == 'orientace':

                ori = cisla_bodu[1:]

                x, y = separovat_souradnice(ori, body)

                mapa.plot(x, y, '--or')

                for j in range(len(x)):
                    mapa.text(x[j]-0.7, y[j]+0.6, ori[j], color='r')

            print(radek)

    mapa.show()

polohopis(r'c:\Users\Jakub\Desktop\prg_spszem\lekce_10\kody.txt')




# for bod, souradnice in body.items():
#     print('Souradnice bodu {} jsou y={:.3f}, x={:.3f}'.format(bod, souradnice['y'], souradnice['x']))



























# import numpy as np
#
#
# # f = open('souradnice.csv', 'w')
# #
# # f.write('cb;y;x\n')
# #
# # for i in range(50):
# #
# #     y = 745100 + np.random.random()*50
# #     x = 1045300 + np.random.random()*50
# #
# #     f.write('{};{};{}\n'.format(4001+i, y, x))
#
# # f = open('mereni.csv', 'w')
# #
# # f.write('stanovisko;orientace;bod;delka;uhel\n')
# #
# # for i in range(100):
# #
# #     st = np.random.randint(4001, 4050)
# #     ori = np.random.randint(4001, 4050)
# #
# #     delka = np.random.random()*50+20
# #     uhel = np.random.random()*400
# #
# #     f.write('{};{};{};{};{}\n'.format(st, ori, i+1, delka, uhel))
#
# def nactiBody(soubor: str) -> dict:
#
#     body = {}
#
#     with open(soubor, 'r') as f:
#         for line in f.read().splitlines():
#             if line[0] != 'c':
#                 cb, y, x = line.split(';')
#
#                 bod = {}
#
#                 bod['y'] = float(y)
#                 bod['x'] = float(x)
#
#                 body[cb] = bod
#
#     return body
#
# def nactiMereni(soubor: str) -> list:
#
#     mereni = []
#
#     with open(soubor, 'r') as f:
#         for line in f.read().splitlines():
#             if line[0] != 's':
#                 stanovisko, orientace, bod, delka, uhel = line.split(';')
#
#                 zamera = {}
#
#                 zamera['stanovisko'] = stanovisko
#                 zamera['orientace'] = orientace
#                 zamera['bod'] = bod
#                 zamera['delka'] = float(delka)
#                 zamera['uhel'] = float(uhel)
#
#                 mereni.append(zamera)
#
#     return mereni
#
# def grady2rad(uhel: float) -> float:
#     return uhel*np.pi/200
#
# def rad2grady(uhel: float) -> float:
#     return uhel*200/np.pi
#
# def smernik(stanovisko: dict, cil: dict) -> float:
#
#     dy = cil['y'] - stanovisko['y']
#     dx = cil['x'] - stanovisko['x']
#
#     w = np.arctan2(dy, dx)
#
#     if w < 0:
#         w += 2*np.pi
#
#     return w
#
# def rajon(stanovisko: dict, orientace: dict, delka: float, uhel: float) -> dict:
#
#     w = smernik(stanovisko, orientace)
#
#     y = stanovisko['y'] + delka*np.sin(uhel+w)
#     x = stanovisko['x'] + delka*np.cos(uhel+w)
#
#     bod = {}
#     bod['y'] = y
#     bod['x'] = x
#
#     return bod
#
#
# body = nactiBody('souradnice.csv')
#
# for zamera in nactiMereni('mereni.csv'):
#
#     stanovisko = body[zamera['stanovisko']]
#
#     orientace = body[zamera['orientace']]
#
#     bod = rajon(stanovisko, orientace, zamera['delka'], zamera['uhel'])
#
#     body[zamera['bod']] = bod
