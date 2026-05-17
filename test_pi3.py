from pi3 import converter_nota_para_conceito

def test0():
    assert converter_nota_para_conceito(0.0) == 'F'
def test2_9():
    assert converter_nota_para_conceito(2.9) == 'F'
def test3():
    assert converter_nota_para_conceito(3.0) == 'D'
def test4_9():
    assert converter_nota_para_conceito(4.9) == 'D'
def test5():
    assert converter_nota_para_conceito(5.0) == 'C'
def test6_9():
    assert converter_nota_para_conceito(6.9) == 'C'
def test7():
    assert converter_nota_para_conceito(7.0) == 'B'
def test8_9():
    assert converter_nota_para_conceito(8.9) == 'B'
def test9_9():
    assert converter_nota_para_conceito(9.9) == 'A'
def test9():
    assert converter_nota_para_conceito(9.0) == 'A'
def test11():
    assert converter_nota_para_conceito(11.0) == 'Nota Inválida'
def testnegativo():
    assert converter_nota_para_conceito(-1.0) == 'Nota Inválida'