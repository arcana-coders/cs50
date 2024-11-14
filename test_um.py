import pytest
from um import count 

def test_basic():
    
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM um Um") == 3

def test_punctuation():
    
    assert count("um?") == 1
    assert count("Um.") == 1
    assert count("um, um... um!") == 3
    assert count("um... um") == 2

def test_in_sentences():
    
    assert count("Um, I think this is right.") == 1
    assert count("Um, um... interesting!") == 2
    assert count("I was thinking, um, maybe later.") == 1
    assert count("Um? Well, that's unexpected.") == 1

def test_not_a_word():
    
    assert count("yummie") == 0
    assert count("alumni") == 0
    assert count("humano") == 0
    assert count("Yummy, umami, umbrella") == 0

def test_mixed_cases():
    
    assert count("Um, um... umami? Um.") == 3
    assert count("Some random text with UM, and um? Also humano.") == 2
    assert count("Um, are you sure about this yummie? Um!") == 2
