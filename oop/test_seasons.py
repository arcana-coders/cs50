from seasons import calc_age

def test_calc_age():
    assert calc_age("2010-01-01") == "Seven million, eight hundred fifty-six thousand, six hundred forty minutes"
    assert calc_age("2024-01-01") == "Four hundred ninety-three thousand, nine hundred twenty minutes"
    assert calc_age("1978-02-01") == "Twenty-four million, six hundred forty-two thousand, seven hundred twenty minutes"
    try:
        calc_age("invalid-date")
    except ValueError as e:
        assert str(e) == "Algo está mal. Por favor use una fecha válida."
