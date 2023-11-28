from bank import value

def main():
    test_return_0()
    test_return_20()
    test_return_100()

def test_return_0():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("Hello, Marta") == 0

def test_return_20():
    assert value("hi") == 20
    assert value("How you doing?") == 20

def test_return_100():
    assert value("good morning") == 100
    assert value("What's happening?") == 100

if __name__ == "__main__":
    main()