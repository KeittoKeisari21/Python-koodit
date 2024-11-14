class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, ka, svm):
        super().__init__(nimi)
        self.ka = ka
        self.svm = svm

    def tiedot(self):
        print(f'Kirja {self.nimi}')
        print(f'Tekijä {self.ka}')
        print(f'Sivuja {self.svm}')


class Lehti(Julkaisu):
    def __init__(self, nimi, toimittaja):
        super().__init__(nimi)
        self.toimittaja = toimittaja


    def info(self):
        print(f'Lehti {self.nimi}')
        print(f'Toimittaja {self.toimittaja}')


aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

print('Julkaisujen tiedot:')
aku_ankka.info()
print("")
hytti.tiedot()