from dispatcher import Dispatcher
from handlers import add_handlers

API_KEY = "bb162c28be60f5bf4afb31a045255ad2"
dispatcher = Dispatcher(API_KEY)

add_handlers(dispatcher)


def default(data: "OpenWeatherData", current_city: "City"):
    print("Something went wrong! Try again please.")


if __name__ == "__main__":
    # data = get_data_from_open_weather_map("Kyiv", API_KEY)
    # ...
    print("-----------T-A-S-K-2----------")
    dispatcher.set_default_handler(default)
    dispatcher.run()
