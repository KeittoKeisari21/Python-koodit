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

auto = Auto('ABC-123', 142)
print(f'Rekisteri: {auto.rek}\n')
print(f'Maksiminopeus: {auto.yli}\n')
print(f'Kuljettu matka: {auto.mat}\n')


kiihdytys = [30, 70, 50, -200]

for kiihy in kiihdytys:
    auto.kiihdy(kiihy)




print(f'Nykynopeus: {auto.nyk}\n')