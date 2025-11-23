import json

import requests
ciudad = input("Ciudad: ")
url_geo = f"https://geocoding-api.open-meteo.com/v1/search?name={ciudad}"
response = requests.get(url_geo)
data = response.json()
print(json.dumps(data,indent=4))
ciudad_info = data["results"][0]
lat = ciudad_info["latitude"]
long = ciudad_info["longitude"]
print(f"Latitud: {lat} Longitud:{long} ")
url_clima = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={lat}&longitude={long}"
    f"&current_weather=true&hourly=temperature_2m"
)

response_clima = requests.get(url_clima)
data_clima = response_clima.json()

if "current_weather" not in data_clima:
    print("No hay datos meteorológicos para esta ubicación.")
    exit()

current = data_clima["current_weather"]



