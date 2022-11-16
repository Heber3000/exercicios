frase = str(input('Escreva uma frase:')).upper()
vogais = 0
espacos = 0
for letras in frase:
    if 'AEIOU'.find(letras) >= 0:
        vogais +=1
    if letras == ' ':
        espacos += 1


print(f'Número de espacos e vogais é {espacos} e {vogais}')

