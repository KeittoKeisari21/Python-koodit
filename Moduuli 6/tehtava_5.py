def karsi(kaikki):
    return kaikki % 2 == 0
kaikki = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p = list(filter(karsi, kaikki))
print(kaikki)
print(p)


