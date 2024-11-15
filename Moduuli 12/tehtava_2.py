import requests

api = "Juuh"

while True:
    kpk = input("Kaupungin nimi?: ")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={kpk}&appid={api}"

    vastaus = requests.get(url)

    if vastaus.status_code == 200:
        data = vastaus.json()
        kelvin = data['main']['temp']
        celsius = kelvin -273.15
        saa = data['weather'][0]['description']


        print(f'Lämpötila {celsius:.1f} Celsiusta')
        print(f'Sään kuvaus {saa}')
        break