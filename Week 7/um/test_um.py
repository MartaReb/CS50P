from um import count
import pytest

def main():
    test_upper_lower_case()
    test_words_with_um()
    test_um_with_spaces_and_punctuation_marks()

def test_upper_lower_case():
    assert count("um") == 1
    assert count("Um thanks for the album.") == 1
    assert count("UM thanks, um") == 2

def test_words_with_um():
    assert count("yum") == 0
    assert count("yummy") == 0
    assert count("Um Mum") == 1


def test_um_with_spaces_and_punctuation_marks():
    assert count("...um...") == 1
    assert count("  um  ") == 1
    assert count("hello, um, world") == 1
    assert count("Um! Hello, um, world, um") == 3
    assert count("Um. Is this that album where, um, umm, the clumsy alums play drums?") == 2