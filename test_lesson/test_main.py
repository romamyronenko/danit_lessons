import pytest

from main import div


@pytest.mark.parametrize(
    "test_a, test_b, expected_result",
    [
        (4, 2, 2),
        (4, 1, 4),
        (4, 8, 0.5),
    ],
)
def test_div(test_a, test_b, expected_result):
    result = div(test_a, test_b)

    assert result == expected_result


@pytest.mark.skip()
def test_div_exception():
    with pytest.raises(ZeroDivisionError):
        div(4, 1)


def test():
    # given
    a = 10
    b = 5
    expected_result = 2

    # when
    result = div(a, b)

    # then
    assert result == expected_result
