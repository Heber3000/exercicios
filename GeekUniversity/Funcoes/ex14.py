def consumo(km,litros):
    consumo = km/litros
    print(f'\nConsumo:{"%.2f" % consumo} km/l')
    if consumo < 8:
        return f'\nVenda o Carro!'
    elif consumo <= 14:
        return f'\nEconômico'
    else:
        return f'\nSuper Econômico'

print(consumo(300,2))


