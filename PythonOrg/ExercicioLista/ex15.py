lista = []
contador_acimade7 = 0
contador_acimaMedia = 0

valor = int(input('Informe os valores'))
while valor != -1:
    valor = int(input('Informe os valores'))
    lista.append(valor)


lista.remove(-1)

for i in lista:
    if i <= 7:
        contador_acimade7 += 1
    if i >= int(sum(lista)/len(lista)):
        contador_acimaMedia +=1



print(f'a){len(lista)}\nb){lista}\nc){lista[:-1]}\nd){sum(lista)}\ne){sum(lista)/len(lista)}\nf){contador_acimaMedia}\ng){contador_acimade7}'
      f'\nh)Encerrou ')