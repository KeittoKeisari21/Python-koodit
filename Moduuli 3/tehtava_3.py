x = input("Anna biologinen sukupuoli: ")
h = input("Anna hemoglobiiniarvosi(g/l): ")
y = int(h)


if x == "mies" and y <= 136:
    print("liian alhainen")
elif x == "mies" and y >= 195:
    print("liian korkea")
elif x == "nainen" and y <= 117:
    print("liian alhainen")
elif x == "nainen" and y >= 175:
    print("liian korkea")
else:
    print("normaali")
