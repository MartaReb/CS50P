from plates import is_valid

def test_first_two_letters():
    assert is_valid("CS50") == True
    assert is_valid("C5CS") == False
    assert is_valid("5CSS") == False
    assert is_valid("50CS") == False

def test_min_and_max_characters():
    assert is_valid("AA") == True
    assert is_valid("WARSAW") == True
    assert is_valid("A") == False
    assert is_valid("GOODBYE") == False

def test_numbers_at_the_end():
    assert is_valid("CS50P") == False
    assert is_valid("0CS50") == False

def test_spaces_and_punctuations():
    assert is_valid("HELLO,") == False
    assert is_valid("HELL?O") == False
    assert is_valid("HE LLO") == False