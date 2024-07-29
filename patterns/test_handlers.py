from main import UpperCaseTextHandler, ReplaceTextHandler


def test_upper_case_text_handler():
    text = "aswefggf"
    expected_result = "ASWEFGGF"

    handler = UpperCaseTextHandler()

    assert handler.handle(text) == expected_result


def test_replcace_text_handler():
    text = "aswefggfvsdfghtrfhh"
    expected_result = "aswe gg vsd ghtr hh"

    handler = ReplaceTextHandler()

    assert handler.handle(text) == expected_result


def test_handlers_chain():
    text = "aswefggfvsdfghtrfhh"
    expected_result = "ASWE GG VSD GHTR HH"

    handler1 = ReplaceTextHandler()
    handler2 = UpperCaseTextHandler()

    handler1.set_next(handler2)

    assert handler1.handle(text) == expected_result
