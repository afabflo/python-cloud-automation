import requests

def obtener_cordenadas(ciudad:str):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={ciudad}"
    response = requests.get(url)
    data = response.json()

    if "results" not in data or len(data["results"]) == 0:
        return None

    info = data["results"][0]
    return info["latitude"],info["longitude"]

def obtener_clima(ciudad:str):
    coords = obtener_cordenadas(ciudad)
    if coords is None:
        return None

    lat = coords[0]
    lon = coords[1]

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&current_weather=true"
    )

    response = requests.get(url)
    data = response.json()

    if "current_weather" not in data:
        return None

    return data["current_weather"]