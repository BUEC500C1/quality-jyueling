from arabic_to_roman import arabicTOroman
import pytest

def test():
    assert arabicTOroman(1) == "I"
    assert arabicTOroman(6) == "VI"
    assert arabicTOroman(11) == "XI"
    assert arabicTOroman(23) == "XXIII"
    assert arabicTOroman(178) == "CLXXVIII"
    assert arabicTOroman(297) == "CCXCVII"
    assert arabicTOroman(369) == "CCCLXIX"
    assert arabicTOroman(732) == "DCCXXXII"
    assert arabicTOroman(848) == "DCCCXLVIII"
    assert arabicTOroman(1000) == "M"
    assert arabicTOroman(1232) == "MCCXXXII"
    assert arabicTOroman(1478) == "MCDLXXVIII"
    assert arabicTOroman(2796) == "MMDCCXCVI"
    assert arabicTOroman(3515) == "MMMDXV"
    
def test_error():
    assert arabicTOroman("a") == "Wrong Input"
    assert arabicTOroman("1.1") == "Wrong Input"
    
if __name__ == '__main__':
    test()
    test_error()