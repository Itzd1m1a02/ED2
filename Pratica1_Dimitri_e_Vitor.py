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
                    trocou = True
                    cont[0] += 1
        cont[0] += 1
    if y == 'd':
        while trocou == True :
            trocou = False
            for i in range(0, len(x)-1):
                if x[i] < x[i+1]:
                    x[i], x [i+1] = x[i+1], x[i]
                    trocou = True
                    cont[0] += 1
        cont[0] += 1
    return x

def selectsort(x, y, op, cont):
    if op == 'c':
        for i in range(0, y-1):#vai de 0 ao tamanho -1 para não estrapolar no tamanho do vetor
            menor = i #recebe o indicador da possição do vetor
            for j in range(i, y):
                if x[j] < x[menor]:#caso na posição j(coluna) senha menor que o valor que esta no aux   então o 
                    menor = j #aux recebe  apossição do vetor em que o numero e o menor de todos e menor
                    cont[0] += 1
            if i != menor:#caso o valor que o indicador i(linha) aponta, então e trocado  a possição 
                x[i], x[menor] = x[menor], x[i]
                cont[0] += 1
        cont[0] += 1
    if op == 'd':
        for i in range(0, y-1):#vai de 0 ao tamanho -1 para não estrapolar no tamanho do vetor
            menor = i #recebe o indicador da possição do vetor
            for j in range(i, y):
                if x[j] > x[menor]:#caso na posição j(coluna) senha menor que o valor que esta no aux então o 
                    menor = j #aux recebe  apossição do vetor em que o numero e o menor de todos e menor
                    cont[0] += 1
            if i != menor:#caso o valor que o indicador i(linha) aponta, então e trocado  a possição 
                x[i], x[menor] = x[menor], x[i]
                cont[0] += 1
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
            vetor[j+1] = auxiliar
        cont[0] += 1
    elif opcao == 'd':
        for i in range(1,len(vetor)):
            auxiliar = vetor[i]
            j = i - 1
            while (j >= 0) and (auxiliar > vetor[j]):
                vetor[j+1] = vetor[j]
                j = j - 1
            vetor[j+1] = auxiliar
        cont[0] += 1
    return vetor

def MergeSort(op, V, inicio, fim, cont):
    if fim <= inicio:
        cont[0] += 1
        return V
    else:
        meio = (inicio + fim) // 2
        MergeSort(op, V, inicio, meio, cont)#caminha pela parte esquerda do vetor
        MergeSort(op, V, meio+1, fim, cont)#caminha pela parte direita do vetor
        Merge(op, V, inicio, meio, fim, cont)#função que verifica se o vetor unitario formado e mior ou menor e junta dois vetores  
def Merge(op, V, inicio, meio, fim, cont):
    vaux = V[:] #copia o vetor principal para um auxiliar
    p1 = inicio #função que anda o vetor esquerdo(inicial) sem alterar o vetor original
    p2 = meio + 1#função que recebe o meior do vetor V para fraguimentação ate ter um ou mais vetores unitarios
    if (op == 'c'): # ordem crecente
        cont[0] += 1
        for k in range(inicio, fim + 1): #for que vai ate o fim do vetor
            if p1 > meio: # se o ponto 1 da posição do inicio e maior que o numero no meio do vetor
                V[k] = vaux[p2] #então o valor salvo naquela posição do vetor aux e colocado no veor original
                p2 += 1 #posição + 1
                cont[0] += 1
            elif p2 > fim: #se o ponto 2 da posição do inicio e maior que o fim
                V[k] = vaux[p1]#então o valor salvo naquela posição do vetor aux e colocado no veor original
                p1 += 1
                cont[0] += 1
            elif vaux[p2] < vaux[p1]:#se o valor salvo no ponto p2 e menor que o valor salvo no p1
                V[k] = vaux[p2] 
                p2 += 1
                cont[0] += 1
            else:
                V[k] = vaux[p1]#se o valor salvo no ponto p1 e menor que o valor salvo no p2
                p1 += 1
                cont[0] += 1
    if (op == 'd'):#ordem decrecente
        cont[0] += 1
        for k in range(inicio, fim + 1):
            if p1 > meio:
                V[k] = vaux[p2]
                p2 += 1
                cont[0] += 1
            elif p2 > fim:
                V[k] = vaux[p1]
                p1 += 1
                cont[0] += 1
            elif vaux[p2] > vaux[p1]:
                V[k] = vaux[p2]
                p2 += 1
                cont[0] += 1
            else:
                V[k] = vaux[p1]
                p1 += 1
                cont[0] += 1
 
def Quicksort(V, inicio, fim, op):
    if inicio < fim:
        pivo = particionar(V, inicio, fim, op)
        Quicksort(V, inicio, pivo-1, op)
        Quicksort(V, pivo+1, fim, op)
def particionar(V, inicio, fim, op):
    esq = inicio
    dir = fim
    pivo = V[inicio]
    if op == 'c':
        while (esq < dir):
            while (V[esq] <= pivo and esq <= fim):
                esq += 1
            while (V[dir] > pivo and dir >= inicio):
                dir -= 1
            if (esq < dir):
                V[esq], V[dir] = V[dir], V[esq]
        V[dir], V[inicio] = V[inicio], V[dir]
        return dir
    if op == 'd':
        while (esq < dir):
            while (V[esq] >= pivo and esq <= fim):
                esq += 1
            while (V[dir] < pivo and dir >= inicio):
                dir -= 1
            if (esq < dir):
                V[esq], V[dir] = V[dir], V[esq]
        V[dir], V[inicio] = V[inicio], V[dir]
        return dir
           
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
array = random.randint(0,aux,size) #gera numeros aleatorios de acordo com o tamanho
fim = len(array) - 1
inicio = 0
j = [0]

#chamada de estruturas de ordenação
print('==================================================================')
BubbleSort(array, modo, j)
print(f'\n\nVetor ordenado com Bubblesort:{array}, comp:{j}')
selectsort(array, size, modo, j)
print(f'\n\nVetor ordenado com Selectsort:{array}, comp:{j}')
insertionSort(array, modo, j)
print(f'\n\nVetor ordenado com Insertionsort:{array}, comp:{j}')
MergeSort(modo, array, inicio, fim, j)
print(f'\n\nVetor ordenado com Mergesort:{array}, comp:{j}')

Quicksort(array, inicio, fim, modo)
print(f'\n\nVetor ordenado com Quicksort:{array}')
print('\n\n==================================================================\n')
#finaliza o arq
fp.close()