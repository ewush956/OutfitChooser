#from config import API_KEY
import os
import requests
from dotenv import load_dotenv

def get_weather_data(lat: float, lon: float,) -> dict:

    #url = "https://api.openweathermap.org/data/2.5/weather"
    url = "https://api.openweathermap.org/data/3.0/onecall"

    query_parameters = {
        "lat": lat,
        "lon": lon,
        "exclude": "minutely,hourly,alerts",
        "appid": os.getenv('API_KEY'),
        "units": "metric",
    }

    response = request.get(url, params=query_parameters)
    response.raise_for_status()

    weather_data = response.json()
    return weather_data