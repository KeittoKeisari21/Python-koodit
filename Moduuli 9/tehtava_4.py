import random
import math
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
        self.mat += float(self.nyk * aika)




autot = []

for i in range(10):
    autot.append(Auto('ABC-' + str(i+1), random.randint(100, 200), 0))

break_cycle = False
while True:
    if break_cycle:
        break
    for a in autot:
        a.kulje(0.5)
        a.kiihdy(a.yli * random.uniform(-10, 15))
        if a.mat >= 10_000:
            break_cycle = True




for auto in autot:
    print(f'{auto.rek},Maksiminopeus {math.trunc(auto.yli)}km/h, Nykykinen nopeus {math.trunc(auto.nyk)}kmh/h, Kuljettu matka {math.trunc(auto.mat)} km\n')

