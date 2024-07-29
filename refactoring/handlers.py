from typing import TYPE_CHECKING

from city import City

if TYPE_CHECKING:
    from dispatcher import Dispatcher
    from openweather_types import OpenWeatherData


def show_temperature(data: "OpenWeatherData", current_city: "City"):
    print(f"Temperature now in {current_city.value}: {data.main.temp}")


def show_weather(data: "OpenWeatherData", current_city: "City"):
    print(
        f"Weather now in {current_city.value}: {data.weather[0].get('description')}"
    )  # TODO: need to update dataclass


def show_wind(data: "OpenWeatherData", current_city: "City"):
    print(f"Wind now in {current_city.value}: {data.wind.speed}")


def show_few_params(data: "OpenWeatherData", current_city: "City"):
    keys = input(
        "Enter keys (should be one word as key, separated by spaces): "
    ).split()

    result = {}

    data_ = {
        "weather": data.weather[0].get("description"),
        "temp": data.main.temp,
        "hum": data.main.humidity,
        "wind": data.wind.speed,
        "main": data.weather[0].get("main"),
    }

    if len(keys) == 1 and isinstance(keys[0], list):
        keys = keys[0]

    for key in keys:
        result[key] = data_[key] if key in data_ else None
    print("".join([f"    {key}: {value}\n" for key, value in result.items()]))


def show_all(data: "OpenWeatherData", current_city: "City"):
    """
      ('    weather: moderate rain\n'
    '    temp: 22.59\n'
    '    hum: 66\n'
    '    wind: 9.07\n'
    '    main: Rain\n',),
    """

    result = (
        f"    weather: {data.weather[0].get('description')}\n"
        f"    temp: {data.main.temp}\n"
        f"    hum: {data.main.humidity}\n"
        f"    wind: {data.wind.speed}\n"
        f"    main: {data.weather[0].get('main')}\n"
    )
    print(f"Now in {current_city.value}: ")
    print(result)


def change_city(data: "OpenWeatherData", current_city: "City"):
    while True:
        city = input("Enter city: ")
        print(city)
        try:
            current_city.set_city(city)
            break
        except (ValueError, AttributeError):
            print(f'"{city}" wasn\'t found. Please, try another one: ')

    # show_info(controller)


def task1(data: "OpenWeatherData", current_city: "City"):
    with open("orders.txt", "r") as f:
        tmp = f.read().split("\n\n")
        data = {i: tmp[i].split("@@@") for i in range(len(tmp))}
        for key, value in data.items():
            print(key, ": ", value)


def add_handlers(dispatcher: "Dispatcher"):
    dispatcher.add_handler("1", "Show Temperature")(show_temperature)
    dispatcher.add_handler("2", "Show Weather")(show_weather)
    dispatcher.add_handler("3", "Show Wind")(show_wind)
    dispatcher.add_handler("4", "Show few parameters")(show_few_params)
    dispatcher.add_handler("5", "Show all")(show_all)
    dispatcher.add_handler("8", "Change city")(change_city)
    dispatcher.add_handler("9", "TASK 1")(task1)
