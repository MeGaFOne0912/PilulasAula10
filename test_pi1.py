from pi1 import cor

def test_cor_amarelo():
    assert cor('amarelo') == 'Atenção'
def test_cor_vermelho():
    assert cor('vermelho') == 'Pare'
def test_cor_verde():
    assert cor('verde') == 'Siga'
def test_cor_invalida():
    assert cor('azul') == 'Cor inválida'