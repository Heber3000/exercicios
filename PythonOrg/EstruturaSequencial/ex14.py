peso_do_peixe = float(input('Informe o peso do peixe: '))

if peso_do_peixe <= 50:
    print('\nSem Multa')
else:
    excesso = peso_do_peixe - 50
    print(f'\nDa quantida {peso_do_peixe}kg ouve um excesso de {excesso}\nO valor da multa é R${excesso*4}')