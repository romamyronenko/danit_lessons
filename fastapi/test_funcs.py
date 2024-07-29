import pytest

from funcs import cows_and_bulls_, check_brackets


@pytest.mark.parametrize(
    "input_secret, input_guess, expected_result",
    [
        ("", "", {"cows": 0, "bulls": 0}),
        ("3333", "3131", {"cows": 0, "bulls": 2}),
        ("1234", "1888", {"cows": 0, "bulls": 1}),
        ("1234", "4321", {"cows": 4, "bulls": 0}),
        ("2111", "2244", {"cows": 0, "bulls": 1}),
        ("2211", "1212", {"cows": 2, "bulls": 2}),
    ],
)
def test_cows_and_bulls(input_secret, input_guess, expected_result):
    result = cows_and_bulls_(input_secret, input_guess)
    assert result == expected_result


@pytest.mark.parametrize(
    "test_s, expected_result",
    [
        ("", True),
        ("(", False),
        ("()", True),
        ("(()", False),
        ("())", False),
        ("(sd[sd]sdsd)", True),
        ("(sd[sdsdsd)]", False),
        ("(sd[sdsdsd)]", False),
    ],
)
def test_check_brackets(test_s, expected_result):
    assert check_brackets(test_s) == expected_result
