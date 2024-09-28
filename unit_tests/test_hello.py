from hello import hello

def test_hello():
    assert hello("David") == "hello, David"

def test_argument():
    assert hello() == "hello, world"
