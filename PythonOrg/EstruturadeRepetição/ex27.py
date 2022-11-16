turma = int(input('Informe o número de turmas:'))
print("")
while turma <= 0:
    print('O número de turmas tem que ser maior que 0.')
    turma = int(input('Informe o número de turmas:'))
else:
    print("Número válido")

soma = 0
contador = 0

for i in range(1,1+turma):
    numero_alunos = int(input('Informe o número de aluno %s º:' % i))
    while numero_alunos > 40:
        print('O número tem que ser menor 40')
        numero_alunos = int(input('Informe o número de aluno %s º:' % i))

    soma += numero_alunos
    contador +=1

print(f'\nA média de alunos por turma {soma/contador}')