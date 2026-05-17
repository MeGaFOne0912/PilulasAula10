from pi2 import frete

def test_frete1kg():
    assert frete(1.0) == 5.0
def test_freteAcima1kg():
    assert frete(1.01) == 10.0
def test_frete5kg():
    assert frete(5.0) == 10.0
def test_freteAcima5kg():
    assert frete(5.01) == 18.0
def test_frete0kg():
    assert frete(0.0) == 0.0
def test_freteNegativo():
    assert frete(-10.0) == 0.0
