from numb3rs import validate
import pytest

def main():
    test_format_ip()
    test_range_of_numbers()

def test_format_ip():
    assert validate(r"1.2.3.4") == True
    assert validate(r"1.2.3") == False
    assert validate(r"1.2") == False
    assert validate(r"1") == False
    assert validate(r"1.2.3.4.5") == False
    assert validate(r"cat") == False

def test_range_of_numbers():
    assert validate(r"255.255.255.0") == True
    assert validate(r"-255.255.255.255") == False
    assert validate(r"256.255.255.255") == False
    assert validate(r"255.256.255.255") == False
    assert validate(r"255.256.255.255") == False
    assert validate(r"255.255.256.255") == False
    assert validate(r"255.255.256.1000") == False

if __name__ == "__main__":
    main()