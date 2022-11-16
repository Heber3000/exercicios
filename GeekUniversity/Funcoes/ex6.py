
def conversao_segundos(horas,minutos,segundos):
    return f'O total de segundos {horas*(60)*60+minutos*(60)+segundos}'

print(conversao_segundos(2,00,30))