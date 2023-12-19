from seasons import convert
import pytest

def test_date_from_today():
    assert convert("2022-12-19") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert("2021-12-19") == "One million, fifty-one thousand, two hundred minutes"

def test_invalid_format():
    with pytest.raises(SystemExit):
        convert("January 1, 1999")
