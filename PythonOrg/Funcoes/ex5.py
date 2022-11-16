def somaImposto(custo,taxaImposto):
    custo = custo*(custo*taxaImposto/100)
    return f'R${custo}'
print(somaImposto(500,1.5))