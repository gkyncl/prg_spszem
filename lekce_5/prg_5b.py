# prg_5b - seznamy pokracovani

# procviceni prace s metodami listu

# dostupne metody:
# remove(), len(), append(), insert(), extend(), index()

# zadani: - v listech "potraviny_gulas", "mnozstvi_gulas", "potraviny_knedlik" a "mnozstvi_knedlik"
#         mame zadano, jake potraviny a jake mnozstvi potrebujeme na vareni gulas
#         - dale mame pridat ke knedlikum 1 kilo mouky
#         - ukolem je vypsat seznam potravin ve formatu:
#         potravina - mnozstvi
#         .
#         .
#         .

#         postup:
#         1) odstranime z potravin pro gulas potravinu, ktera tam nepatri vcetne jejiho mnozstvi
#         2) pridame 1 kilo mouky na predposledni pozici
#         3) spojime listy potravin a jejich mnozstvi
#         4) projdeme cyklem listem a vypiseme vysledek

#gulas
potraviny_gulas = ['cibule', 'sul', 'cesnek', 'hladka mouka', 'haribo medvidek', 'olej', 'majoranka', 'pepr', 'kmin', 'veprova plec', 'mleta paprika']
mnozstvi_gulas = ['2 kusy', '1 lzicka', '2 struzky', '1 lzice', '1 baleni', '3 lzice', '1 lzicka', '1 lzicka', '1 spetka', '600 gramu', '1 lzicka']

#knedlik
pridat = 'polohruba mouka'
kolik = '1 kilo'
potraviny_knedlik = ['cukr', 'sul', 'vejce', 'drozdi', 'rohlik']
mnozstvi_knedlik = ['1 lzicka', '20 gramu', '2 kusy', '20 gramu', '2 kusy']