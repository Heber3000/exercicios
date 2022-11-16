primeiro = 0
segundo = 1
for n in range(1,500):
    terceiro = primeiro+segundo
    primeiro=segundo
    segundo=terceiro
    print(segundo)
