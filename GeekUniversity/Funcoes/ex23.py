def triangulo_lateral(altura):
    linha = 0
    largura = 2*altura - 1
    for i in range(1+largura):
        if i >= altura:
            linha -=1
            print('*'*linha)
        else:
            linha +=1
            print("*"*linha)

print(triangulo_lateral(4))



