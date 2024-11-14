import pytest
from working import convert

def test_valid_inputs():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:00 PM to 8 AM") == "22:00 to 08:00"
    assert convert("12 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("1:30 PM to 2:45 PM") == "13:30 to 14:45"
    assert convert("1 AM to 1 PM") == "01:00 to 13:00" 

def test_invalid_inputs():
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM") 
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")  
    with pytest.raises(ValueError):
        convert("9:00 to 5:00 PM")     
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")      
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM") 
    with pytest.raises(ValueError):
        convert("random text")       
