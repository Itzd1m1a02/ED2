
def insertionSort (vetor, opcao):
    if opcao == 1:
        for i in range(1,len(vetor)):
            auxiliar = vetor[i]
            j = i - 1
            while (j >= 0) and (auxiliar < vetor[j]):
                vetor[j+1] = vetor[j]
                j = j - 1
            vetor[j+1] = auxiliar
    elif opcao == -1:
        for i in range(1,len(vetor)):
            auxiliar = vetor[i]
            j = i - 1
            while (j >= 0) and (auxiliar > vetor[j]):
                vetor[j+1] = vetor[j]
                j = j - 1
            vetor[j+1] = auxiliar
vetor = [-3, -16, 18, 36, -12, -25, -31, -15, 13, 16,  0, -45, -41, -22, 12]
opcao = int(input('Digite a opcao: '))
while opcao < -1 or opcao > 1 or opcao == 0:
    opcao = int(input('Digite a opcao: '))
insertionSort(vetor, opcao)
print(vetor)

