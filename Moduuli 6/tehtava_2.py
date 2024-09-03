tahko = int(input("Anna nopan maksimiluku: "))
def noppa(tahko):
    import random

    while True:
        noppa = random.randint(1,tahko)
        print("Heitto: ",noppa)
        if (noppa == tahko):
            print(noppa, "Peli päättyi")
            break

noppa(tahko)