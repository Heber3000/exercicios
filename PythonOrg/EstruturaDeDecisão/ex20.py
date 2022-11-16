nota_1 = float(input("Informe a primeira Nota:"))
nota_2 = float(input("Informe a segunda Nota:"))
nota_3 = float(input("Informe a terceira Nota:"))

media = (nota_1+nota_2+nota_3)/3

if media < 0 or media > 10:
    print('Média não pode ser menor que zero e maior que a 10')
else:
    if media == 10:
        print("aprovado com distinção")
    elif media < 7:
        print('Reprovado')
    else:
        print('Aprovado')
