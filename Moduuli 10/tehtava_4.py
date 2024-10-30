import random
class Auto:
    def __init__(self,  rek, yli, nyk = 0, mat = 0):
        self.mat = mat
        self.rek = rek
        self.yli = yli
        self.nyk = nyk

    def kiihdy(self, muutos):
        if self.nyk + muutos > self.yli:
            self.nyk = self.yli
        elif self.nyk + muutos < 0:
            self.nyk = 0
        else:
            self.nyk += muutos

    def kulje(self, aika):
        self.mat += self.nyk * aika

class Kilpailu:
    def __init__(self, nimi, matka, autot):
        self.nimi = nimi
        self.matka = matka
        self.autot = autot
        self.aika = 0

    def tunti(self):
        self.aika += 1
        for auto in self.autot:
            auto.kiihdy(auto.yli * random.uniform(-10, 15))
            auto.kulje(1)


    def tk(self):
        print(f'\nKilpailun {self.nimi} tilanne {self.aika} tunnin jälkeen')
        print(f"{'Auto':<8} {'Matka':>9} {'Nopeus':>12} {'Max':>12}")
        print("-" * 40)

        sa = sorted(self.autot, key=lambda auto: auto.mat, reverse=True)

        for auto in sa:
            print(f"{auto.rek:<8} {auto.mat:>9.1f} {auto.nyk:>12.1f} {auto.yli:>12.1f}")


    def ko(self):
        return any(auto.mat >= self.matka for auto in self.autot)

autot = []
for i in range(10):
    autot.append(Auto('ABC-' + str(i+1), random.randint(100, 200), 0))

kp = Kilpailu("Suuri romuralli", 8000, autot)

while not kp.ko():
    kp.tunti()
    if kp.aika % 10 == 0:
        kp.tk()

print('\nKisa ohi')
kp.tk()