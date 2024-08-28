x = []
while True:
    y = input("Anna numero: ")
    if y == "":
        break
    x.append(int(y))
print("Isoin numero on", str(max(x)))
print("Pienin numero on", str(min(x)))