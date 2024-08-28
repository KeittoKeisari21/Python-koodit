k1 = "python"
s1 = "rules"
x = 5
while x > 0:
    k = str(input("Käyttäjätunnus: "))
    s = str(input("Salasana: "))
    if k == k1 and s == s1:
        print("Tervetuloa")
        break
    else:
        x -= 1
if x == 0:
    print("Bro älä ees yritä enää mee nukkuu")
