from pi5 import aplicarCupom
def testCupom10():
    assert aplicarCupom("CUPOM10", 50.0) == 0.10
def testCupom25():
    assert aplicarCupom("CUPOM25", 150.0) == 0.25   
def testCupomDescontoVIP():
    assert aplicarCupom("DESCONTOVIP", 600.0) == 0.35
def test10minusculo():
    assert aplicarCupom("cupom10", 50.0) == 0.10
def testCupom25Invalido():
    assert aplicarCupom("CUPOM25", 50.0) == 0.0
def testDescontoVIPInvalido():
    assert aplicarCupom("DESCONTOVIP", 300.0) == 0.0
def testCupomInvalido():
    assert aplicarCupom("CUPOM99", 500.0) == 0.0