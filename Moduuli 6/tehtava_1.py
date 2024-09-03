def noppa():
    import random

    while True:
        noppa = random.randint(1,6)
        print("Heitto: ",noppa)
        if (noppa == 6):
            print(noppa, "Peli päättyi")
            break

noppa()