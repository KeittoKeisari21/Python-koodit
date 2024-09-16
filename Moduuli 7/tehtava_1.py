kuukaudet = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä",
                "kesä", "syksy", "syksy", "syksy", "talvi", "talvi")
järjestysnumero = int(input("Anna kuukauden järjestysnumero (1-12): "))
vuodenaika = kuukaudet[järjestysnumero-1]
print (f"{järjestysnumero}. vuodenaika on {vuodenaika}.")