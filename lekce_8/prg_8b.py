# prg_8_a - tvorba programu pro spravu uzivatelu

# vytvorte program, ktery bude simulovat system pro spravu uzivatelu
# pri spusteni se program zepta jestli chceme registrovat noveho uzivatele nebo se prihlasit
# pri volbe registrace zada uzivatel uzivatelske jmeno a heslo, ktere musi splnovat vybrana kriteria
# metody nad instanci string: (https://www.w3schools.com/python/python_ref_string.asp)
# uzivatele se ukladaji do seznamu uzivatelu - zapisuji se do souboru - 1 uzivatel na 1 radek: username, password

# pri volbe prihlaseni je uzivatel tazan na uz. jmeno
# pokud dane uziv. jmeno existuje v seznamu, je uzivatel pozadan o heslo na jehoz zadani ma 3 pokusy
# pokud zada spravne, vypise se hlaska, ze registrace probehla uspesne
# pokud zada 3x spatne, program skonci a da o tom info

def password_check(password):
    if len(password) < 6:
        print("heslo ma mene nez 6 znaku")
    if password.islower():
        print("heslo obsahuje pouze mala pismena")
    if password.isalpha():
        print("heslo obsahuje pouze pismena")
    if password.isalnum():
        print("heslo neobsahuje specialni znak/y")
    if password.isnumeric():
        print("heslo neobsahuje zadna pismena")
    if not len(password) < 6 and not password.islower() and not password.isalpha() and not password.isalnum() and not password.isnumeric():
        print("heslo je OK")
        return password
    else:
        return False



while True:
    print("Pro registraci zadejte R, pro prihlaseni zadejte P, pro ukonceni programu zadejte Q")
    ukon = input("co chcete udelat: ")

    # registrace
    if ukon == "R":
        username = input("zadejte uživatelské jméno: ")

        while True:
            password = input("zadejte heslo: ")
            a = password_check(password)
            if a != False:
                break

        # zapis uz jmena a hesla do souboru
        with open("uzivatele.txt", "a") as soubor:
            soubor.write("{} {}".format(username, password))
            soubor.write("\n")

    elif ukon == "P":
        print("udela se pozdeji ...")
    elif ukon == "Q":
        quit()
    else:
        print("takovy prikaz neznam")










