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
h = Hissi(1, 6)

h.siirry_kerrokseen(6)
h.siirry_kerrokseen(1)
