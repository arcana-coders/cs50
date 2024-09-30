import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from twttr import shorten

def main ():
    test_low()
    test_upper()
    test_mix()
    test_number()
    test_punctuation()

def test_low ():
    assert shorten("learning python") == "lrnng pythn"
def test_upper():
    assert shorten("CS50 THE BEST COURSE") == "CS50 TH BST CRS" 
def test_mix ():
    assert shorten("David Malan Is My Teacher") == "Dvd Mln s My Tchr"
def test_number ():
    assert shorten("12345") == "12345"
def test_punctuation ():
    assert shorten("!#$%&/") == "!#$%&/"

