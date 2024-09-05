def muunna(galloonat):
    return galloonat * 3.785

def main():
    while True:
        try:
            galloonat = float(input("Anna galloonat: "))
            if galloonat < 0:
                break
            litra = muunna(galloonat)
            print("Tämä on", litra, "litraa")
        except ValueError:
            print("Naa bro")

if __name__ == '__main__':
    main()