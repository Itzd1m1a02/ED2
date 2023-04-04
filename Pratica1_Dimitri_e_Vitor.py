#biblioteca:
from numpy import random

#funções:
def  BubbleSort (x, y, cont):
    trocou = True
    if y == 'c':
        while trocou == True:
            trocou = False
            for i in range(0, len(x)-1):
                if x[i] > x[i+1]:
                    x[i], x [i+1] = x[i+1], x[i]
                    cont[0] += 1
                    trocou = True
    if y == 'd':
        while trocou == True :
            trocou = False
            for i in range(0, len(x)-1):
                if x[i] < x[i+1]:
                    x[i], x [i+1] = x[i+1], x[i]
                    cont[0] += 1
                    trocou = True
                    
    return x

def selectsort(x, y, op, cont):
    if op == 'c':
        for i in range(0, y-1):#vai de 0 ao tamanho -1 para não estrapolar no tamanho do vetor
            menor = i #recebe o indicador da possição do vetor
            for j in range(i, y):
                if x[j] < x[menor]:#caso na posição j(coluna) senha menor que o valor que esta no aux   então o 
                    menor = j #aux recebe  apossição do vetor em que o numero e o menor de todos e menor
            if i != menor:#caso o valor que o indicador i(linha) aponta, então e trocado  a possição 
                x[i], x[menor] = x[menor], x[i]
                cont[0] += 1
    if op == 'd':
        for i in range(0, y-1):#vai de 0 ao tamanho -1 para não estrapolar no tamanho do vetor
            cont[0] += 1
            menor = i #recebe o indicador da possição do vetor
            for j in range(i, y):
                if x[j] > x[menor]:#caso na posição j(coluna) senha menor que o valor que esta no aux então o 
                    menor = j #aux recebe  apossição do vetor em que o numero e o menor de todos e menor
            if i != menor:#caso o valor que o indicador i(linha) aponta, então e trocado  a possição 
                x[i], x[menor] = x[menor], x[i]
                cont[0] += 1
    return x

def insertionSort (vetor, opcao, cont):
    if opcao == 'c':
        for i in range(1,len(vetor)):
            auxiliar = vetor[i]
            j = i - 1
            while (j >= 0) and (auxiliar < vetor[j]):
                vetor[j+1] = vetor[j]
                j = j - 1
                cont[0] += 1
            vetor[j+1] = auxiliar
    elif opcao == 'd':
        for i in range(1,len(vetor)):
            auxiliar = vetor[i]
            j = i - 1
            while (j >= 0) and (auxiliar > vetor[j]):
                vetor[j+1] = vetor[j]
                j = j - 1
                cont[0] += 1
            vetor[j+1] = auxiliar
    return vetor

def MergeSort(V, inicio, fim, op, cont):
    if fim <= inicio:
        return V
    else:
        meio = (inicio + fim) // 2
        MergeSort(V, inicio, meio, op, cont)#caminha pela parte esquerda do vetor
        MergeSort(V, meio+1, fim, op, cont)#caminha pela parte direita do vetor
        Merge(V, inicio, meio, fim, op, cont)#função que verifica se o vetor unitario formado e mior ou menor e junta dois vetores
def Merge(V, inicio, meio, fim, op, cont):
    vaux = V[:] #copia o vetor principal para um auxiliar
    p1 = inicio #função que anda o vetor esquerdo(inicial) sem alterar o vetor original
    p2 = meio + 1#função que recebe o meior do vetor V para fraguimentação ate ter um ou mais vetores unitarios
    if (op == 'c'): # ordem crecente
        for k in range(inicio, fim + 1): #for que vai ate o fim do vetor
            if p1 > meio: # se o ponto 1 da posição do inicio e maior que o numero no meio do vetor
                V[k] = vaux[p2] #então o valor salvo naquela posição do vetor aux e colocado no veor original
                p2 += 1 #posição + 1
            elif p2 > fim: #se o ponto 2 da posição do inicio e maior que o fim
                V[k] = vaux[p1]#então o valor salvo naquela posição do vetor aux e colocado no veor original
                p1 += 1
            elif vaux[p2] < vaux[p1]:#se o valor salvo no ponto p2 e menor que o valor salvo no p1
                V[k] = vaux[p2] 
                p2 += 1
            else:
                V[k] = vaux[p1]#se o valor salvo no ponto p1 e menor que o valor salvo no p2
                p1 += 1
                cont[0] += 1
    if (op == 'd'):#ordem decrecente
        for k in range(inicio, fim + 1):
            if p1 > meio:
                V[k] = vaux[p2]
                p2 += 1
            elif p2 > fim:
                V[k] = vaux[p1]
                p1 += 1
            elif vaux[p2] > vaux[p1]:
                V[k] = vaux[p2]
                p2 += 1
            else:
                V[k] = vaux[p1]
                p1 += 1
                cont[0] += 1

def Quicksort(array, inicio, fim, op, cont):
   if inicio < fim:
       pivo = particiona(array, inicio, fim, op, cont)
       Quicksort(array,inicio,pivo-1, op, cont)
       Quicksort(array,pivo+1,fim, op, cont)
def particiona(array, inicio, fim, op, cont):
    pivo = array[inicio]
    esquerda = inicio+1
    direita = fim
    aux = False
    
    if op == 'c':
        while not aux:
            while esquerda <= direita and array[esquerda] <= pivo:
                esquerda += 1
            while array[direita] >= pivo and direita >= esquerda:
                direita -= 1
            if direita < esquerda:
                aux = True
            else:
                array[esquerda], array[direita] = array[direita], array[esquerda]
                cont[0] += 1
        array[inicio], array[direita] = array[direita], array[inicio]
        cont[0] += 1
        return direita
    
    if op == 'd':
        while not aux:
            while esquerda <= direita and array[esquerda] >= pivo:
                esquerda += 1
            while array[direita] <= pivo and direita >= esquerda:
                direita -= 1
            if direita < esquerda:
                aux = True
            else:
                array[esquerda], array[direita] = array[direita], array[esquerda]
                cont[0] += 1
        array[inicio], array[direita] = array[direita], array[inicio]
        cont[0] += 1
        return direita

def Max_Heap(array, i, size, modo, cont):
    maior = i
    esquerda = 2*i+1
    direita = 2*i+2
    if modo == 'c':
        if(esquerda <= (size-1)) and (array[esquerda] > array[i]):
            maior = esquerda
        if (direita <= (size-1)) and (array[direita] > array[maior]):
            maior = direita
        if i != maior:
            array[i], array[maior] = array[maior], array[i]
            cont[0] += 1
            Max_Heap(array, maior, size - 1, modo, cont) 
    if modo == 'd':
        if(esquerda <= (size-1)) and (array[esquerda] < array[i]):
            maior = esquerda
        if (direita <= (size-1)) and (array[direita] < array[maior]):
            maior = direita
        if i != maior:
            array[i], array[maior] = array[maior], array[i]
            cont[0] += 1
            Max_Heap(array, maior, size - 1, modo, cont)    
def descobreFilhos(array, size, modo, cont):
    aux = range(size // 2, -1, -1)
    for i in aux:
        Max_Heap(array, i, size, modo, cont)
def Heapsort(array, modo, cont):
    size = len(array)
    descobreFilhos(array, size, modo, cont)
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i]  = array[i], array[0]
        size -= 1
        Max_Heap(array, 0, size, modo, cont)

#entrada de nome e abertura do arq no modo de leitura
arq = input('\nDigite o nome do arquivo: ')
fp = open(arq+'.txt','r')

#leitura de cada linha do arq
size = int(fp.readline())
modo = fp.readline()

#um numero de 0 ate N
aux = int(input('\n\nDigite de 1 ate N: '))
while (aux < 0 or aux == 0):
    aux = int(input('\n\nDigite de 1 ate N: '))
print('\n')

#criação de um array como o tamanho lido do arquivo.
array = []
for i in range(size):
    array.append(random.randint(0, aux))
fim = len(array) - 1
inicio = 0
j = [0]

#chamada de estruturas de ordenação
print('==================================================================')
BubbleSort(array, modo, j)
print(f'\n\nVetor ordenado com Bubblesort:{array}, comp: {j}')
random.shuffle(array) #embaranah o vetor de novo
j = [0] #zera o contador

selectsort(array, size, modo, j)
print(f'\n\nVetor ordenado com Selectsort:{array}, comp: {j}')
random.shuffle(array)
j = [0]

insertionSort(array, modo, j)
print(f'\n\nVetor ordenado com Insertionsort:{array}, comp: {j}')
random.shuffle(array)
j = [0]

MergeSort(array, inicio, fim, modo, j)
print(f'\n\nVetor ordenado com Mergesort:{array}, comp: {j}')
random.shuffle(array)
j = [0]

Quicksort(array, inicio, fim, modo, j)
print(f'\n\nVetor ordenado com Quicksort:{array}, comp: {j}')
random.shuffle(array)
j = [0]

Heapsort(array, modo, j)
print(f'\n\nVetor ordenado com Heapsort:{array}, comp: {j}')
print('\n\n==================================================================\n')

#finaliza o arq
fp.close()