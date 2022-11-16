vetor_1 = []
vetor_2= []
vetor_3 = []

for i in range(10):
    vetor_1.append(float(input('Informe os valores para o primeiro vetor:')))



for i in range(10):
    vetor_2.append(float(input('Informe os valores para o segundo vetor:')))


for i in range(10):
    vetor_3.append(float(input('Informe os valores para o terceiro vetor:')))


vetor_4 = []
for j in range(10):
    vetor_4.append(vetor_1[j])
    vetor_4.append(vetor_2[j])
    vetor_4.append(vetor_3[j])
print(vetor_1)
print(vetor_2)
print(vetor_3)
print(f'________________________\n{vetor_4}')