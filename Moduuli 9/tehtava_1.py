class Auto:
    def __init__(self,  rek, yli, nyk = 0, mat = 0):
        self.mat = mat
        self.rek = rek
        self.yli = yli
        self.nyk = nyk

auto = Auto('ABC-123', 142)
print(f'Rekisteri: {auto.rek}\n')
print(f'Maksiminopeus: {auto.yli}\n')
print(f'Kuljettu matka: {auto.mat}\n')
print(f'Nykynopeus: {auto.nyk}\n')