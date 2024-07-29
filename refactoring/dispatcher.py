from city import City
from utils import get_data_from_open_weather_map


class Dispatcher:
    def __init__(self, api_key):
        self._handlers = {}
        self._default_handler = lambda *_, **__: (None, None)

        self._api_key = api_key

    def _get_choice(self, current_city):
        print()
        print(f"Current city: {current_city.value}")
        for cmd, (_, description) in self._handlers.items():
            print(f"[{cmd}] {description}")

        print("[0] Exit")
        return input("Enter number in brackets: ")

    def set_default_handler(self, handler):
        self._default_handler = handler

    def add_handler(self, cmd, description):
        def wrapper(func):
            self._handlers[cmd] = (func, description)
            return func

        return wrapper

    def run(self):
        city = input("Enter city: ")

        current_city = City(city)

        data = get_data_from_open_weather_map(current_city.value, self._api_key)
        print(current_city.value)
        print(
            f"Now it's {data.weather[0].get('main')}ny now in {city},  {data.main.temp}\u2103 now and wind {data.wind.speed} m/s."
        )

        while True:
            choice = self._get_choice(current_city)
            if choice == "0":
                break
            func, _ = self._handlers.get(choice, (self._default_handler, ""))

            # update data
            data = get_data_from_open_weather_map(current_city.value, self._api_key)

            func(data, current_city)
