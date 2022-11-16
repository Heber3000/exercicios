def positivoNegativo(num):
    if num  <= 0:
        return f'{-num}'
    elif num == 0:
        return f'{0}'
    else:
        return f'{num}'


print(positivoNegativo(4))

