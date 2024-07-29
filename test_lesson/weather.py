import requests

"""
?lat={lat}&lon={lon}&exclude={part}&appid={API key}
"""
API_KEY = "4dea32be938b7cdc2f4e6d8b718fdcae"


def get_temp(city):
    city_list = ["Dnipro", "Paris", "tt"]
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={"appid": API_KEY, "q": city},
    )
    response = response.json()
    retval = response.get("main", {})
    retval = retval.get("temp", {})
    return retval


print(get_temp("Dnipro"))
