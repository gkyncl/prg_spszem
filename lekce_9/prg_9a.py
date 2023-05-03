# nova datova struktura - slovniky (dictionary - dict)

# datova struktura pro uchovavani dat ve forme klic - hodnota

# tvorba slovniku

# 1)
OsobaVyska = {
    'Zacharias': 179,
    'Cestmir': 183,
    'Klotylda': 211}

# 2)
osoba = ['Zacharias', 'Cestmir', 'Klotylda']
vyska = [179, 183, 211]

OsobaVyska = dict(zip(osoba, vyska))

# 3)
OsobaVyska = {}
OsobaVyska['Zacharias'] = 179
OsobaVyska['Cestmir'] = 183
OsobaVyska['Klotylda'] = 211

# iterace pres slovnik
for osoba in OsobaVyska:
    print('Vyska cloveka {} je {} cm'.format(osoba, OsobaVyska[osoba]))


# do slovniku je mozno pridat slovnik!!!
slovnikSlovniku = {'slovnik1': OsobaVyska,
                   'slovnik2': OsobaVyska}

