def frete(peso:float):
    if peso <= 0:
        return 0
    elif peso <= 1:
        return 5.0
    elif peso <= 5:
        return 10.0
    else:
        return 18.0