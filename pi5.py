def aplicarCupom(codigoCupom: str, valorCompra: float):
    codigoCupom = codigoCupom.upper()
    if codigoCupom == "CUPOM10":
        return 0.10
    if codigoCupom == "CUPOM25" and valorCompra > 100:
        return 0.25
    if codigoCupom == "DESCONTOVIP" and valorCompra > 500:
        return 0.35
    return 0.0