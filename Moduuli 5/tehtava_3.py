luku = int(input("Anna luku: "))
al = True
for i in range(2, luku):
    if luku % i == 0:
        al = False
        break
if al:
    print(f"{luku} on alkuluku")
else:
    print(f"{luku} ei ole alkuluku")