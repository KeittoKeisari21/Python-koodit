class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nyky = alin


    def kerros_ylos(self, kohde):
        if self.nyky < kohde :
            self.nyky += 1


    def kerros_alas(self, kohde):
        if self.nyky > kohde:
            self.nyky -= 1



    def siirry_kerrokseen(self, kohde):
        print(f'Hissi on kerroksessa {self.nyky}')
        while self.nyky != kohde:
            if self.nyky > kohde:
                self.kerros_alas(kohde)
            elif self.nyky < kohde:
                self.kerros_ylos(kohde)
            print(f'Hissi on kerroksessa {self.nyky}')


class Talo:
    def __init__(self, alin, ylin, his):
        self.hissit = []
        self.alin = alin
        for i in range(his):
            self.hissit.append(Hissi(alin, ylin))


    def aja_hissia(self, his, kohkrs):
        if 0 <= his <= len(self.hissit):
            print(f'Hissi {his}')
            self.hissit[his].siirry_kerrokseen(kohkrs)

t = Talo(1, 5, 3)
t.aja_hissia(2, 3)
t.aja_hissia(0, 4)
t.aja_hissia(1, 5)