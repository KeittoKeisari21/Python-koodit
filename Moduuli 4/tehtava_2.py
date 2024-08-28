x = 2.54
while True:
    y = float(input("Anna tuumat: "))
    if y > 0:
        print(y * x,"cm")
    elif y < 0:
        print("Ei nyt neagatiivisia lukuja samperi")
        break