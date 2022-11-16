def fatorial(n):
    contador = 1
    for i in range(1,n+1):
        contador *= i
        print(i,end='*')

    print(f'{n}!={contador}')


print(fatorial(5))