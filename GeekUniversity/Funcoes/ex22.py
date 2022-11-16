def exercicio22(n):
    contador = 0
    for i in range(1,n+1):
        contador += 1
        print(f'{str("!")*contador}')
    return ''

print(exercicio22(5))