import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from fuel import convert, gauge
import pytest


def main():
    test_convert()
    test_gauge()


def test_convert():
    assert convert("4/5") == 80
    assert convert("1/4") == 25
    assert convert("2/4") == 50
    assert convert("3/4") == 75
    assert convert("99/100") == 99
    with pytest.raises(ValueError):
        convert("X/Y")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")



def test_gauge():
    assert gauge(99) == "F"
    assert gauge(75) == "75%"
    assert gauge(50) == "50%"
    assert gauge(20) == "20%"
    assert gauge(1) == "E"
