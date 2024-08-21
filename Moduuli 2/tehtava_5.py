le = input("Anna leviskät: ")
na = input("Anna naulat: ")
lu = input("Anna luodit: ")


f1 = float(le)
f2 = float(na)
f3 = float(lu)

g1 = 13.3
g2 = 32 * g1
g3 = 20 * g2

i1 = f3 * g1
i2 = f2 * g2
i3 = f1 * g3
i4 = i1 + i2 + i3
i5 = int(i4/1000)

print("Massa nykymittojen mukaan:")
print (i5, "Kilogrammaa", str(round(i4%1000,2)), "Grammaa")


