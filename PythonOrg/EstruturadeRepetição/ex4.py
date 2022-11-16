populacaoA = 80000
taxa_crescimentoA = 1.03
populacaoB= 200000
taxa_crescimentoB = 1.015
contador_anos = 0


while populacaoA <= populacaoB:
    populacaoA *= taxa_crescimentoA
    populacaoB *= taxa_crescimentoB
    contador_anos += 1

print(f'\nA para que a população alcance A alcance a população B levara {contador_anos} anos')