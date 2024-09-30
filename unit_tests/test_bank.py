import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from bank import value

def main ():
    test_nothing ()
    test_something ()
    test_jackpot ()

def test_nothing ():
    assert value("Hello") == "$0"
    assert value("Hello to all the world!!") == "$0"
    assert value("Hello Hello!!") == "$0"

def test_something ():
    assert value("Hi!") == "$20"
    assert value("How are you?") == "$20"
    assert value("Hola hola!!") == "$20"

def test_jackpot ():
    assert value("alo alo") == "$100"
    assert value("Mucho gusto!!") == "$100"
    assert value("Que tal mis amigos!!") == "$100"