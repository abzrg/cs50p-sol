"""\
Test working.py
"""

import pytest

from working import convert


def test_without_colon() -> None:
    """\
    Test working hours that does not contain : in them
    """
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 6 AM") == "00:00 to 06:00"
    assert convert("12 PM to 6 PM") == "12:00 to 18:00"


def test_with_colon() -> None:
    """\
    Test working hours that contain : in them
    """
    assert convert("9:24 AM to 5:42 PM") == "09:24 to 17:42"
    assert convert("12:01 AM to 6:59 AM") == "00:01 to 06:59"
    assert convert("12:30 PM to 6:03 PM") == "12:30 to 18:03"


def test_input_format() -> None:
    """\
    Test invalid input working hours
    """
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")
