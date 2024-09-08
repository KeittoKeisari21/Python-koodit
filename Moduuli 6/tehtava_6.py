import math
ha1 = float(input("Anna Pizzan halkaisija (cm): "))
hi1 = float(input("Anna Pizzan hinta (€): "))
ha2 = float(input("Anna Pizzan halkaisija (cm): "))
hi2 = float(input("Anna Pizzan hinta (€): "))

pin1 = math.pi * (ha1/2)**2
pin2 = math.pi * (ha2/2)**2

def lyks(hi, pin):
    return hi / pin

yhi1 = lyks(hi1, pin1)
yhi2 = lyks(hi2, pin2)

print("Pizza nro 1 yksikköhinta:", yhi1,"€/cm^2")
print("Pizza nro 2 yksikköhinta:", yhi2,"€/cm^2")

if yhi1 > yhi2:
    print("Pizza nro 2 on halvempi")
elif yhi1 < yhi2:
    print("Pizza nro 1 on halvempi")