

for i in range(10):
    aluno_num = int(input('Informe o número:'))
    altura = float(input('Informe a altura:'))

    if "maisAlto" not in vars() or altura > maisAlto:
        maisAlto = altura
        codigoMaisAlto = aluno_num
    if "maisBaixo" not in vars() or altura > maisBaixo:
        maisBaixo = altura
        codigoMaisBaixo = aluno_num

print(f'O mais alto tem código {codigoMaisAlto} e sua altura é de {maisAlto}\nO mais baixo tem código {codigoMaisBaixo} e sua altura é de {maisBaixo}')


