def contar_caracter(palavra:str):
    caracter_ordenados = sorted(palavra)
    contador = 1

    caracter_anterior = caracter_ordenados[0]

    for caracter in caracter_ordenados[1:]:
        if caracter == caracter_anterior:
            contador += 1
        else:
            print(f'{caracter_anterior}:{contador}')
            caracter_anterior = caracter
            contador = 1
    print(f'{caracter_anterior}:{contador}')








if __name__ == '__main__':

    print(contar_caracter('heber'))
    print(contar_caracter('banana'))
