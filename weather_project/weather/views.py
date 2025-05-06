











import requests
from django.core.cache import cache
from django.shortcuts import render

def get_countries_weather():
    cached_data = cache.get('countries_weather_data')
    if cached_data:
        return cached_data

    countries_url = "https://restcountries.com/v3.1/all"
    countries_data = requests.get(countries_url).json()

    all_countries = []
    weather_api_key = "de7cbe734e7e1b3827bdde85fc351fb2"

    for country in countries_data:
        name = country.get("name", {}).get("common", "Unknown")
        capital = country.get("capital", ["Unknown"])[0] if country.get("capital") else "Unknown"
        population = country.get("population", "N/A")
        flag_url = country.get("flags", {}).get("png", "")

        weather = {"temperature": "N/A", "description": "No data", "icon": ""}
        if capital != "Unknown":
            weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={capital}&appid={weather_api_key}&units=metric"
            weather_response = requests.get(weather_url).json()
            if weather_response.get("cod") == 200:
                weather = {
                    "temperature": weather_response["main"]["temp"],
                    "description": weather_response["weather"][0]["description"],
                    "icon": f"http://openweathermap.org/img/wn/{weather_response['weather'][0]['icon']}.png"
                }

        wikipedia_link = f"https://en.wikipedia.org/wiki/{name.replace(' ', '_')}"
        youtube_link = f"https://www.youtube.com/results?search_query={name}"

        all_countries.append({
            "name": name,
            "capital": capital,
            "population": f"{population:,}",
            "flag_url": flag_url,
            "weather": weather,
            "wikipedia_link": wikipedia_link,
            "youtube_link": youtube_link,
        })

    cache.set('countries_weather_data', all_countries, timeout=900)

    return all_countries

def country_list(request):
    countries = get_countries_weather()
    return render(request, 'weather/countries.html', {"countries": countries})
