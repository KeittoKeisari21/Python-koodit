x = set()

while True:
    y = input("Syötä nimi: ")
    if y == "":
        break

    if y in x:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        x.add(y)

for y in x:
    print(y)