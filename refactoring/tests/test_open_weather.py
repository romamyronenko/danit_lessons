import pytest

from open_weather import dispatcher, default
from openweather_types import OpenWeatherData
from tests.mocks import get_mock_input, get_mock_print, mock_request, mock_response

menu = [
    (),
    ("Current city: Kyiv",),
    ("[1] Show Temperature",),
    ("[2] Show Weather",),
    ("[3] Show Wind",),
    ("[4] Show few parameters",),
    ("[5] Show all",),
    ("[8] Change city",),
    ("[9] TASK 1",),
    ("[0] Exit",),
]


class Base:
    inputs: list[str]
    expected_prints: list[tuple[str]]

    def test_main(self):
        prints = []
        expected_result = ("Temperature now in Kyiv: 22.59",)
        with get_mock_input(self.inputs), get_mock_print(prints), mock_request:
            dispatcher.set_default_handler(default)
            dispatcher.run()

        assert prints == self.expected_prints


class TestShowTemperature(Base):
    inputs = ["Kyiv", "1", "0"]
    expected_prints = [
        ("Kyiv",),
        ("Now it's Rainny now in Kyiv,  22.59℃ now and wind 9.07 m/s.",),
        *menu,
        ("Temperature now in Kyiv: 22.59",),
        *menu,
    ]


class TestShowWeather(Base):
    inputs = ["Kyiv", "2", "0"]
    expected_prints = [
        ("Kyiv",),
        ("Now it's Rainny now in Kyiv,  22.59℃ now and wind 9.07 m/s.",),
        *menu,
        ("Weather now in Kyiv: moderate rain",),
        *menu,
    ]


class TestShowWind(Base):
    inputs = ["Kyiv", "3", "0"]
    expected_prints = [
        ("Kyiv",),
        ("Now it's Rainny now in Kyiv,  22.59℃ now and wind 9.07 m/s.",),
        *menu,
        ("Wind now in Kyiv: 9.07",),
        *menu,
    ]


class TestShowFewParams(Base):
    inputs = ["Kyiv", "4", "wind temp", "0"]
    expected_prints = [
        ("Kyiv",),
        ("Now it's Rainny now in Kyiv,  22.59℃ now and wind 9.07 m/s.",),
        *menu,
        ("    wind: 9.07\n    temp: 22.59\n",),
        *menu,
    ]


class TestShowAll(Base):
    inputs = ["Kyiv", "5", "0"]
    expected_prints = [
        ("Kyiv",),
        ("Now it's Rainny now in Kyiv,  22.59℃ now and wind 9.07 m/s.",),
        *menu,
        ("Now in Kyiv: ",),
        (
            "    weather: moderate rain\n"
            "    temp: 22.59\n"
            "    hum: 66\n"
            "    wind: 9.07\n"
            "    main: Rain\n",
        ),
        *menu,
    ]


@pytest.mark.skip()
class TestShowChangeCity(Base):
    inputs = ["Kyiv", "8", "0"]
    expected_prints = [
        ("Kyiv",),
        ("Now it's Rainny now in Kyiv,  22.59℃ now and wind 9.07 m/s.",),
        *menu,
        ("Wind now in Kyiv: 9.07",),
        *menu,
    ]


class TestTask1(Base):
    inputs = ["Kyiv", "9", "0"]
    expected_prints = [
        ("Kyiv",),
        ("Now it's Rainny now in Kyiv,  22.59℃ now and wind 9.07 m/s.",),
        *menu,
        (
            0,
            ": ",
            [
                "Bulgarian Yogurt",
                "Organic 4% Milk Fat Whole Milk Cottage Cheese",
                "Organic Celery Hearts",
                "Cucumber Kirby",
                "Lightly Smoked Sardines in Olive Oil",
                "Bag of Organic Bananas",
                "Organic Hass Avocado",
                "Organic Whole String Cheese \\n\n",
            ],
        ),
        *menu,
    ]


class TestWrong(Base):
    inputs = ["Kyiv", "asd", "0"]
    expected_prints = [
        ("Kyiv",),
        ("Now it's Rainny now in Kyiv,  22.59℃ now and wind 9.07 m/s.",),
        *menu,
        ("Something went wrong! Try again please.",),
        *menu,
    ]


def test_types():
    result = OpenWeatherData.create(mock_response.json())
    assert result
