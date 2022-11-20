num = int(input('Informe um valor inteiro'))
soma = 0

for i in range(1,num+1):
    soma += 1/(1+i)
    print(f'H({i})=1/1+{i}={soma}')

