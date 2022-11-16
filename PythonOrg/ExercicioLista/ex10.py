vetor_1 = []
vetor_2= []

for i in range(10):
    vetor_1.append(float(input('Informe os valores para o primeiro vetor:')))



for i in range(10):
    vetor_2.append(float(input('Informe os valores para o segundo vetor:')))



vetor_3 = []
for j in range(10):
    vetor_3.append(vetor_1[j])
    vetor_3.append(vetor_2[j])
print(vetor_1)
print(vetor_2)
print(vetor_3)

