from typing import TYPE_CHECKING

import requests

from openweather_types import OpenWeatherData

if TYPE_CHECKING:
    pass


def get_data_from_open_weather_map(city, api_key):
    url_pattern = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    URL = url_pattern.format(city=city, api_key=api_key)
    response = requests.get(URL)
    data = response.json()
    return OpenWeatherData.create(data)
