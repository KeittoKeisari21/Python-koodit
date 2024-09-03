ll = []
while True:
    luku = input("Syötä luku: ")
    if luku == "":
        break
    ll.append(luku)
    ll.sort(reverse = True)
print("Viisi suurinta: ")

for i in range(min(5,len(ll))):
    print(ll[i])
