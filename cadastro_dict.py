def cadastrar():
    perguntas = {'nome','telefone','email'}

    dict = {}
    dados = []

    for i in range(2):
        print(f'Cadastro:{1+i}')
        for resposta in perguntas:
            dict[resposta] = input(f'{resposta}:')
        dados.append(dict)

    return dados

print(cadastrar())