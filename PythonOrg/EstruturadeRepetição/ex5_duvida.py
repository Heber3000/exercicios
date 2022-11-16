populacaoA = float(input('Informe a População do País A:'))
taxa_crescimentoA = 1.03
populacaoB = float(input('Informe a População do País B:'))
taxa_crescimentoB = 1.015
contador_anos = 1

while populacaoA >= populacaoB:

     populacaoA *= taxa_crescimentoA
     populacaoB *= taxa_crescimentoB
     contador_anos += 1

print(f'\nA para que a população alcance A alcance a população B levara {contador_anos} anos')