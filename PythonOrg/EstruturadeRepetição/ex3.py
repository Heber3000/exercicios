nome = input('Informe o seu nome:')
#a
while len(nome) < 3:
    nome = input('Informe o seu nome:')
else:
    print('Nome aceito\n')

#b
idade = int(input('Informe a idade:'))
while idade < 0 or idade >150:
    idade = int(input('Informe a idade:'))
else:
    print('Idade aceito\n')
#b
salario = float(input("Informe o salário: "))
while salario < 0:
    salario = float(input("Informe o salário: "))
else:
    print('Salário aceito\n')
#c
sexo = input('Informe o sexo M-Masculino ou F-Feminino').upper()
while sexo != 'M' and sexo != 'F':
    sexo = input('Informe o sexo M-Masculino ou F-Feminino').upper()
else:
    print("Sexo Válido\n")
#d
estado_civil = input("Informe o estado Civil: S-Solteiro,C-Casado,V-Viuvo,D-Divorciado").upper()
while estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
    estado_civil = input("Informe o estado Civil: S-Solteiro,C-Casado,V-Viuvo,D-Divorciado").upper()
else:
    print('Estado civil válido')



