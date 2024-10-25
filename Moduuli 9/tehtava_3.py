class Auto:
    def __init__(self,  rek, yli, nyk = 0, mat = 2000):
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
        self.mat += float(self.nyk * aika)




auto = Auto('ABC-123', 142)

kiihdytys = [60]

for kiihy in kiihdytys:
    auto.kiihdy(kiihy)
auto.kulje(1.5)
print(f'Rekisteri: {auto.rek}\n')
print(f'Maksiminopeus: {auto.yli}\n')
print(f'Kuljettu matka: {auto.mat}\n')

print(f'Nykynopeus: {auto.nyk}\n')
