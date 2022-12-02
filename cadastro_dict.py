perguntas = ('Nome','telefone','email')

dict ={}


for i in range(2):
    print(f'Cadastro: {1+i}')
    for resposta in perguntas:
        dict[resposta] = input(f'{resposta}:')

print(dict)