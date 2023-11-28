from utils import calculate_bmi

def test_bmi():
    expected = 25
    actual = calculate_bmi(100, 2)
    assert actual == expected