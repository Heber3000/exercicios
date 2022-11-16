
vogais = []
consoantes = []

for i in range(1,11):
    letras = input('Informe umas letras: ').upper()
    if letras == 'A' or letras == 'E' or letras == 'I' or letras == 'U' or letras == 'U':
        vogais.append(letras)
    else:
        consoantes.append(letras)

print(f'\nA quantidade de consoantes {len(consoantes)}\n{consoantes}')





