import calc

def test_add():
    assert calc.add(1, 6) == 7
    assert calc.add(5, 32) == 37

def test_sub():
    assert calc.sub(6, 2) == 4
    assert calc.sub(3, 10) == -7

def test_div():
    assert calc.div(6, 2) == 6 / 2
    assert calc.div(10, 4) == 10 / 4

def test_mul():
    assert calc.mul(1, 0) == 0
    assert calc.mul(21, 3) == 63
