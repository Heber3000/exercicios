def media(n):
    vetor_real = []
    for i in range(1,n+1):
        vetor_real.append(float(input('Adicione os valores a lista %sº:' % i)))
    return f'\nA média valor é {sum(vetor_real)/len(vetor_real)}'


print(media(5))
