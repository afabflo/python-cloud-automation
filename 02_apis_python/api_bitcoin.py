import requests
url = "https://api.open-meteo.com/v1/forecast?latitude=40.4168&longitude=-3.7038&current_weather=true"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(response.status_code)
