import lesson27


def test_addition():
    assert lesson27.addition(5, 2) == 7
    assert lesson27.addition(90, 3) == 93
    assert lesson27.addition(30, 3) != 3

def test_subtraction():
    assert lesson27.subtraction(42, 8) == 34
    assert lesson27.subtraction(2, 8) == -6
    assert lesson27.subtraction(4, 8) != 4
