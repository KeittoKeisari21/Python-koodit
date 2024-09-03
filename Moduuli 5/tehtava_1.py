import random
noppa = int(input("Montako noppaa: "))
x = 0

for i in range(noppa):
    heitto = random.randint(1, 6)
    x += heitto
print("Heittojen summa: ", x)
