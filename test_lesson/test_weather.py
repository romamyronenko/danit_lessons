from openweather_types import SimpleNamespace
from unittest import mock
from unittest.mock import MagicMock

from weather import get_temp

"""144 ms"""
expected_result = 292.75
#
#
# def mock_get(url, params):
#     mock_response = SimpleNamespace()
#     mock_response.json = lambda: {'main': {'temp': expected_result}}
#     return mock_response


def test_get_temp():
    city = "Dnipro"
    with mock.patch(
        "requests.get",
        return_value=MagicMock(json=lambda: {"main": {"temp": expected_result}}),
    ):
        response = get_temp(city=city)

    assert response == expected_result
