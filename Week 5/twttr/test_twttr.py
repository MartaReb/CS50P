from twttr import shorten

def main():
    test_vowels()
    test_numbers()
    test_punctuation()

def test_vowels():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"

def test_numbers():
    assert shorten("1234") == "1234"

def test_punctuation():
    assert shorten("!,.?") == "!,.?"

if __name__ == "__main__":
    main()