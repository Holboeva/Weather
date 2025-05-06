import requests

API_KEY = "de7cbe734e7e1b3827bdde85fc351fb2"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "icon": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}.png"
        }
    return None
