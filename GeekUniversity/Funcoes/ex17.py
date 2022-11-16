def somaInteiros(num1:int,num2:int):
    soma = 0
    for i in range(num1,num2+1):
        soma +=i
        print(i)
    return f'===================\n+{soma}'

print(somaInteiros(1,1000))