def DesenhaLinha(n):
    contador = 0
    for i in range(1,n+1):
        contador += 1
        print(str("=")*contador,end="")
    return ''


print(DesenhaLinha(10))
