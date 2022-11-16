def exponenciacao(x,z):
    exponenciacao =1
    for i in range(1,z+1):
        exponenciacao *= x
    return f'Exponenciação {exponenciacao}'

print(exponenciacao(4,2))