def vetor(n):
    vetor = []
    for i in range(n):
        vetor.append(int(input('Adicione valores inteiros em um vetor:')))
    print(vetor)
    return f'O valor máximo é de {max(vetor)}'

print(vetor(5))