import copy

from main import foo


def test_foo():
    test_b = 10
    test_a = [1, 2, 3]
    expected_a = copy.copy(test_a)

    foo(test_b, test_a)

    assert test_a == expected_a
