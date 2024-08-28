import random

x = random.randint(1, 10)
while True:
    y = int(input("Arvaa luku 1 - 10 väliltä: "))
    if y > x:
        print("Liian iso")
    elif y < x:
        print("Liian pieni")
    else:
        print("Arvasit oikein")
        break