usuario = input('Informe o nome de usuario:')
senha = input('Informe a senha:')

while usuario == senha:
    print('\nO usuário e senhas iguais')
    usuario = input('Informe o nome de usuario:')
    senha = input('Informe a senha:')
else:
    print('\nUsuário aceito')