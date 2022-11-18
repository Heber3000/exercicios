num = int(input('Informe o número: '))

for i in range(num+1,0,-1):
    if i % 2 != 0:
        print(i)