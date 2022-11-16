def conversaoFarenheit(celsius:float):
    F = celsius*(9/5) + 32
    return f'A temperatura de {celsius} celsius é de {F} farenheit'

print(conversaoFarenheit(32))