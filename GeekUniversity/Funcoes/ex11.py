def medias(nota1:float,nota2:float,nota3:float,opcao:str):
    if opcao == 'A':
        mediaAritmetica = (nota1+nota2+nota3)/3
        return f'{(mediaAritmetica)}'
    elif opcao == 'B':
        # pesos: 5,3,2
        mediaPonderada = (nota3*5 +nota2*3 +nota1*2)/(5+3+2)
        return f'{mediaPonderada}'
    else:
        return f'Opcao Inválida'


opcao = str(input('Informe opção (A) ou (B):')).upper()

print(medias(3,4,5,opcao))



