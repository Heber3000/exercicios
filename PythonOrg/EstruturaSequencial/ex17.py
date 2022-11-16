nome_atleta = input('Informe o nome do Atleta:')
lista_de_Saltos = []
lista_atleta = []

while nome_atleta != 'FIM':
    nome_atleta = input('Informe o nome do Atleta:')
    lista_atleta.append(nome_atleta)
    for i in range(1,6):
        lista_de_Saltos.append(float(input('Informe o %s:' % i)))
        lista_atleta.append(lista_de_Saltos)

