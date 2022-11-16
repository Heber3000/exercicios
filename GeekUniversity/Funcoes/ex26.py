def soma_n(n):
    soma = 0
    for i in range(1,n+1):
        soma +=i
        print(i)
    return print(f'==============\n+{soma}')

print(soma_n(10))
