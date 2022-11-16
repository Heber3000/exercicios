produto1 = float(input('Informe o preço dos produtos:'))
produto2= float(input('Informe o preço dos produtos:'))
produto3 = float(input('Informe o preço dos produtos:'))
print('')

if produto1 == produto2 and produto1==produto3:
    print('Todos produtos tem o mesmo preço')
else:
    if produto1 < produto2 and produto1 < produto2:
        print(f'Leve o produto {produto1}')
    elif produto2 < produto1 and produto2 < produto3:
        print(f'Leve o produto {produto2}')
    else:
        print(f'Leve o produto {produto3}')