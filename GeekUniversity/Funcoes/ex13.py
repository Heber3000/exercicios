def operacoes(num1,num2,operacao:str):
    if operacao == '+':
        return f'adição.\n{num1} + {num2} = {num1+num2}'
    elif operacao == '-':
        return f'subtração.\n{num1} - {num2} = {num1 - num2}'
    elif operacao == '*':
        return f'multiplicação.\n{num1} X {num2} = {num1 * num2}'
    elif operacao == '/':
        return f'divisão.\n{num1} X {num2} = {num1 / num2}'
    else:
        return f'valor inválido'

print(operacoes(4,2,"/"))