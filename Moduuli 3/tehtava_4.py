y = input("Anna vuosiluku: ")

x = int(y)

if x % 4 == 0:
    print("vuosi on karkausvuosi")
elif x % 100 == 0 and x % 400 == 0:
    print("vuosi on karkausvuosi")
else:
    print("vuosi ei ole karkausvuosi")