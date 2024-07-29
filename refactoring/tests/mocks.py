from types import SimpleNamespace
from unittest import mock

mock_response = SimpleNamespace()
mock_response.status_code = 200
mock_response.json = lambda: {
    "coord": {"lon": 30.5167, "lat": 50.4333},
    "weather": [
        {"id": 501, "main": "Rain", "description": "moderate rain", "icon": "10d"}
    ],
    "base": "stations",
    "main": {
        "temp": 22.59,
        "feels_like": 22.63,
        "temp_min": 22.59,
        "temp_max": 22.59,
        "pressure": 1011,
        "humidity": 66,
        "sea_level": 1011,
        "grnd_level": 995,
    },
    "visibility": 7024,
    "wind": {"speed": 9.07, "deg": 191, "gust": 15.29},
    "rain": {"1h": 3.47},
    "clouds": {"all": 83},
    "dt": 1717522122,
    "sys": {
        "type": 2,
        "id": 2089522,
        "country": "UA",
        "sunrise": 1717465783,
        "sunset": 1717524192,
    },
    "timezone": 10800,
    "id": 703448,
    "name": "Kyiv",
    "cod": 200,
}
mock_request = mock.patch("requests.get", return_value=mock_response)


def create_input_mock(values: list[str]):
    values = iter(values)

    def mock_input(*_, **__):
        return next(values)

    return mock_input


def create_print_mock(prints_list):
    def mock_print(*args, **kwargs):
        prints_list.append(args)

    return mock_print


def get_mock_input(values: list[str]):
    return mock.patch("builtins.input", new=create_input_mock(values))


def get_mock_print(prints_list: list):
    return mock.patch("builtins.print", new=create_print_mock(prints_list))
