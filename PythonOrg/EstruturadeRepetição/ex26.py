# Candidato A

numero_candidatosA = int(input('Informe a quantidade de candidatos A:'))
contador_A = 0 
for i in range(1,1 + numero_candidatosA):
    votacao_A = input('Confirma o voto no candidato A (S:Sim/N:Não):').upper()
    if votacao_A == 'S':
        contador_A += 1
        
# Candidato B
print('')
numero_candidatosB = int(input('Informe a quantidade de candidatos B:'))
contador_B = 0 
for i in range(1,1 + numero_candidatosB):
    votacao_B = input('Confirma o voto no candidato B (S:Sim/N:Não):').upper()
    if votacao_B == 'S':
        contador_B += 1
print('')
# Candidato C
numero_candidatosC = int(input('Informe a quantidade de candidatos C:'))
contador_C = 0
for i in range(1,1 + numero_candidatosC):
    votacao_C = input('Confirma o voto no candidato c (S:Sim/N:Não):').upper()
    if votacao_C == 'S':
        contador_C += 1
print('')

print(f'O número de Votos Para o candidato A:{contador_A}\nO número de Votos Para o candidato A:{contador_B}\nO número de Votos Para o candidato A:{contador_C}')
