soma = 0
somaAcidentes2mil = 0
contador = 0

for i in range(5):
    codigo = int(input('Informe o código da cidade: '))
    veiculos = int(input('Informe o número de veículos de passeio:'))
    numero_acidentes = int(input('Informe o número de acidentes:'))
    soma += numero_acidentes
    print('')

    if 'maiorIndicedeAcidentes' not in vars() or numero_acidentes > maiorIndicedeAcidentes:
        maiorIndicedeAcidentes = numero_acidentes
        codigoMaior = codigo

    if 'menorIndicedeAcidentes' not in vars() or numero_acidentes < menorIndicedeAcidentes:
        menorIndicedeAcidentes = numero_acidentes
        codigoMenor = codigo

    if veiculos < 2000:
        somaAcidentes2mil += numero_acidentes
        contador += 1


print(f'd)codigo do maior numero {codigo} e {menorIndicedeAcidentes}\n  codigo do maior numero {codigo} e {maiorIndicedeAcidentes}\n\n'
      f'e){soma/5}\nf)Média de acidentes {somaAcidentes2mil/contador}')