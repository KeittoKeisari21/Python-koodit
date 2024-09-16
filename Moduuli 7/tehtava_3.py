la = {}

while True:
    print("1 Lisää lentoasema")
    print("2 Etsi olemassa oleva asema")
    print("3 Lopeta")

    x = input("Valitse toiminto: ")

    if x == "1":
        icao = input("Syötä lentoaseman ICAO-koodi: ")
        nimi = input("Syötä lentoaseman nimi: ")
        la[icao] = nimi
        print(f"Lentoasema {nimi} (ICAO: {icao}) lisätty.")

    elif x == "2":
        icao = input("Syötä Lentoaseman ICAO-koodi: ")
        if icao in la:
            print(f"Lentoasema: {la[icao]}")
        else:
            print("Lentoasemaa ei löydy")
    if x == "3":
        print("Sessio lopetettu valintasi poistetaan")
        break