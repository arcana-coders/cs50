import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from plates import is_valid

def main ():
    test_6long()
    test_2long()
    test_1long()
    test_7long()
    test_2letters()
    test_firstnumber()
    test_firstnumber_not0()
    test_numbers_not_togueter()
    test_number_end()
    test_character()


def test_6long():
    assert is_valid("CS1250") == True
def test_2long():
    assert is_valid("CS") == True
def test_1long():
    assert is_valid("C") == False
def test_7long():
    assert is_valid("CS12345") == False
def test_2letters():
    assert is_valid("CS") == True
    assert is_valid("C5") == False
def test_firstnumber():
    assert is_valid("50CS") == False
    assert is_valid("50") == False
def test_firstnumber_not0():
    assert is_valid("CS01234") == False
    assert is_valid("CS1000") == True
    assert is_valid("CS0") == False
    assert is_valid("01NUM") == False
def test_numbers_not_togueter():
    assert is_valid("CS50A1") == False
    assert is_valid("CS501") == True
def test_number_end():
    assert is_valid("NUM1") == True
    assert is_valid("NUM1A") == False
def test_character():
    assert is_valid("CS50!") == False

    