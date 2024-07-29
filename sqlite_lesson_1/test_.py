from unittest import mock


def func(s):
    print(s)


def test():
    s = "c"
    with mock.patch("builtins.print", autospec=True) as print_result:
        func(s)
        print_result.assert_called_with(s)
