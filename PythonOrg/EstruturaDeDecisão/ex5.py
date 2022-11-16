nota1 = float(input('Informe a primeira nota:'))
nota2 = float(input('Informe a segunda nota:'))
media = (nota1+nota2)/2

if media >= 7:
    print(f'Aprovado')
elif media == 10:
    print(f'Aprovada com Louvor')
elif media <= 10:
    print(f'Reprovado')
else:
    print(f'Média inválida')