import pytest

from factorial import factorial


@pytest.mark.parametrize(
    "n, expected_result",
    [
        (1, 1),
        (0, 1),
        (2, 2),
        (3, 6),
        (5, 120),
    ],
)
def test_factorial(n, expected_result):
    assert factorial(n) == expected_result


@pytest.mark.smoke
def test_negative():
    with pytest.raises(ValueError):
        factorial(-2)


class Base:
    n: int
    expected_result: int

    def test(self):
        assert factorial(self.n) == self.expected_result


class TestZero(Base):
    n = 0
    expected_result = 1


class TestOne(Base):
    n = 1
    expected_result = 1
