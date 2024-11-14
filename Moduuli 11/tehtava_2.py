class Auto:
    def __init__(self, rek , yli, nyk = 0, mat = 0):
        self.rek = rek
        self.yli = yli
        self.nyk = nyk
        self.mat = mat

    def kulje(self, tunnit):
        self.mat += self.nyk * tunnit


class Tehosekotin(Auto):
    def __init__(self, rek , yli, akku):
        super().__init__(rek, yli)
        self.akku = akku

class Oikeeauto(Auto):
    def __init__(self, rek, yli, tankki):
        super().__init__(rek, yli)
        self.tankki = tankki


tesla = Tehosekotin('ABC-15', 180, 52.5)
toyota = Oikeeauto('ACD-123', 165, 32.3)


tesla.nyk = 100
toyota.nyk = 90

tesla.kulje(3)
toyota.kulje(3)

print(f'Sähkövatkaimen mittar: {tesla.mat} km')
print(f'Oikean auton mittari {toyota.mat} km')
