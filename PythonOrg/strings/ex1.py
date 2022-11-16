str_1 = input('Informe uma frase:')
str_2 = input('Informe a segunda fase:')



if len(str_1) == len(str_2):
    mensagem = 'As strings tem o mesmo tamanho'
else:
    mensagem = 'As strings tem tamanho diferentes'

print(f'string 1: {str_1}\nstring 2: {str_2}\nA "{str_1}":{len(str_1)}\nA "{str_2}":{len(str_2)}\n{mensagem}')