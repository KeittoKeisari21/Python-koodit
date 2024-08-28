import random

p1 = int(input("Kuinka monta pistettä arvotaan?: "))
p2 = 0

for i in range(p1):
    x = random.uniform(1, -1)
    y = random.uniform(1, -1)
    if x*x + y*y < 1:
        p2 = p2 +1

pl = 4 * p2 / p1
print("Piin likiarvo on: ",pl)