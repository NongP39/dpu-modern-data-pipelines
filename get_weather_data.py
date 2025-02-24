import requests

API_KEY = "cf58fa7d8db08fed7620093cb114766d"  # แทนที่ YOUR_API_KEY ด้วย API Key ของคุณ
payload = {
    "q": "bangkok",
    "appid": API_KEY,
    "units": "metric"
}

url = "https://api.openweathermap.org/data/2.5/weather"
response = requests.get(url, params=payload)

print(response.url)
data = response.json()
print(data)