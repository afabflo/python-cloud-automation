import json

import requests
url = "https://api.open-meteo.com/v1/forecast?latitude=40.4168&longitude=-3.7038&current_weather=true"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(json.dumps(data,indent=4))
else:
    print(response.status_code)

current = data["current_weather"]
temperature = current["temperature"]
viento = current["windspeed"]
direccion = current["winddirection"]
latitude = data["latitude"]
print(f"Latitudine: {latitude}")
print(f"Temperatura actual : {temperature}ºC")
print(f"Viento : {viento}km/h")
print(f"Direccion del viento : {direccion}º")