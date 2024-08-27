x = input("Mikä hyttiluokka: LUX, A, B, C?: ")

if x =="LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif x == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif x == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif x == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")