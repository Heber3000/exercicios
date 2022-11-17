def contar_caracter(palavras:str):
    resultado = {}

    for caracter in palavras:
        resultado[caracter] = resultado.get(caracter,0) + 1

    return resultado

if __name__ == '__main__':
    print(contar_caracter('heber'))
    print(contar_caracter('banana'))




