idades = []
alturas = []
contador = 0

for i in range(30):
    idades.append(int(input('Informe a idade do aluno de número %s:' % i)))
    alturas.append(int(input('Informe a altura do aluno de numero %s:' % i)))

    media = sum(alturas)/len(alturas)

    if idades[i] > 13 and alturas[i]:

        contador += 1

print(f'A Quantidade de alunos {contador}')



