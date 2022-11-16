frase = input('Infor uma frase:')

frase_reversa =frase[::-1]


if frase == frase_reversa:
    print('Palindromo')
else:
    print('Não palindromo')