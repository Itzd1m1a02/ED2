#biblioteca:
from numpy import random
from datetime import datetime, timedelta

#funções:
def BubbleSort (x, cont):
    trocou = True
    while trocou == True:
        trocou = False
        for i in range(0, len(x)-1):
            if x[i] > x[i+1]:
                x[i], x [i+1] = x[i+1], x[i]
                cont[0] += 3
                trocou = True
    return x

def selectsort(x, y, cont):
    for i in range(0, y-1):#vai de 0 ao tamanho -1 para não estrapolar no tamanho do vetor
        menor = i #recebe o indicador da possição do vetor
        for j in range(i, y):
            if x[j] < x[menor]:#caso na posição j(coluna) senha menor que o valor que esta no aux   então o 
                menor = j #aux recebe a posição do vetor em que o numero e o menor de todos e menor
                cont[0] += 3
        if i != menor:#caso o valor que o indicador i(linha) aponta, então e trocado  a possição 
            x[i], x[menor] = x[menor], x[i]
            cont[0] += 3
    return x

def insertionSort (vetor, cont):
    for i in range(1,len(vetor)):
        auxiliar = vetor[i]
        j = i - 1
        while (j >= 0) and (auxiliar < vetor[j]):
            vetor[j+1] = vetor[j]
            j -= 1
            cont[0] += 3
        vetor[j+1] = auxiliar
        cont[0] += 3
    return vetor

def MergeSort(V, inicio, fim, cont):
    if fim <= inicio:
        return V
    else:
        meio = (inicio + fim) // 2
        MergeSort(V, inicio, meio, cont)#caminha pela parte esquerda do vetor
        MergeSort(V, meio+1, fim, cont)#caminha pela parte direita do vetor
        Merge(V, inicio, meio, fim, cont)#função que verifica se o vetor unitario formado e mior ou menor e junta dois vetores
def Merge(V, inicio, meio, fim, cont):
    vaux = V[:] #copia o vetor principal para um auxiliar
    p1 = inicio #função que anda o vetor esquerdo(inicial) sem alterar o vetor original
    p2 = meio + 1#função que recebe o meior do vetor V para fraguimentação ate ter um ou mais vetores unitarios
    for k in range(inicio, fim + 1): #for que vai ate o fim do vetor
        if p1 > meio: # se o ponto 1 da posição do inicio e maior que o numero no meio do vetor
            V[k] = vaux[p2] #então o valor salvo naquela posição do vetor aux e colocado no veor original
            p2 += 1 #posição + 1
            cont[0] += 2
        elif p2 > fim: #se o ponto 2 da posição do inicio e maior que o fim
            V[k] = vaux[p1]#então o valor salvo naquela posição do vetor aux e colocado no veor original
            p1 += 1
            cont[0] += 2
        elif vaux[p2] < vaux[p1]:#se o valor salvo no ponto p2 e menor que o valor salvo no p1
            V[k] = vaux[p2] 
            p2 += 1
            cont[0] += 2
        else:
            V[k] = vaux[p1]#se o valor salvo no ponto p1 e menor que o valor salvo no p2
            p1 += 1
            cont[0] += 1

def Quicksort(array, inicio, fim, cont):
    if inicio < fim:
       pivo = particiona(array, inicio, fim, cont)
       Quicksort(array,inicio,pivo-1, cont)
       Quicksort(array,pivo+1,fim, cont)
def particiona(array, inicio, fim, cont):
    pivo = array[inicio]
    esquerda = inicio+1
    direita = fim
    aux = False
    while not aux:
        while esquerda <= direita and array[esquerda] <= pivo:
            esquerda += 1
        while array[direita] >= pivo and direita >= esquerda:
            direita -= 1
        if direita < esquerda:
            aux = True
        else:
            array[esquerda], array[direita] = array[direita], array[esquerda]
            cont[0] += 3
    array[inicio], array[direita] = array[direita], array[inicio]
    cont[0] += 3
    return direita

def Max_Heap(array, i, size, cont):
    maior = i
    esquerda = 2*i+1
    direita = 2*i+2
    if(esquerda <= (size-1)) and (array[esquerda] > array[i]):
        maior = esquerda
    if (direita <= (size-1)) and (array[direita] > array[maior]):
        maior = direita
    if i != maior:
        array[i], array[maior] = array[maior], array[i]
        cont[0] += 3
        Max_Heap(array, maior, size - 1, cont)    
def descobreFilhos(array, size, cont):
    aux = range(size // 2, -1, -1)
    for i in aux:
        Max_Heap(array, i, size, cont)
def Heapsort(array, cont):
    size = len(array)
    descobreFilhos(array, size, cont)
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i]  = array[i], array[0]
        cont[0] += 3
        size -= 1
        Max_Heap(array, 0, size, cont)
        
def arrayMaker(size, modo):
    array = []
    match modo:
        case 'c':
            for i in range (1,size+1):
                array.append(i)
        case 'd':
            for i in range (size,0,-1):
                array.append(i)
        case 'r':
            for i in range(size):
                array.append(random.randint(0, 32000))
        case _:
            print('Modo desconhecido. ERRO!')
            quit()
    return array

#entrada de nome e abertura do arq no modo de leitura
arq = input('\nDigite o nome do arquivo: ')
fp = open(arq+'.txt','r')

#leitura de cada linha do arq
size = int(fp.readline())
modo = fp.readline()
array = arrayMaker(size, modo)

print(f'\nTamanho do vetor: {size}\n')
match modo:
    case 'c':
        print(f'Vetor gerado em ordem crescente:{array}\n')
    case 'd':
        print(f'Vetor gerado em ordem decrescente:{array}\n')
    case 'r':
        print(f'Vetor gerado aleatoriamente:{array}\n')
    case _:
        quit()

fim = len(array) - 1
inicio = 0

#chamada de estruturas de ordenação
print('==================================================================')
bubble_comps = [0]
time_inicial = datetime.now()

BubbleSort(array, bubble_comps)

time_final = datetime.now()
bubble_time = time_final - time_inicial
print(f'\n\nVetor ordenado com Bubblesort:\n{array}')

#========================================================================

selection_comps = [0] #zera o contador
array = arrayMaker(size, modo)

time_inicial = datetime.now()

selectsort(array, size, selection_comps)

time_final = datetime.now()
selection_time = time_final - time_inicial
print(f'\n\nVetor ordenado com SelectSort:\n{array}')

#========================================================================

insertion_comps = [0]
array = arrayMaker(size, modo)

time_inicial = datetime.now()

insertionSort(array, insertion_comps)

time_final = datetime.now()
insertion_time = time_final - time_inicial
print(f'\n\nVetor ordenado com InsertionSort:\n{array}')

#========================================================================

merge_comps = [0]
array = arrayMaker(size, modo)

time_inicial = datetime.now()

MergeSort(array, inicio, fim, merge_comps)

time_final = datetime.now()
merge_time = time_final - time_inicial
print(f'\n\nVetor ordenado com Mergesort:\n{array}')

#========================================================================

quick_comps = [0]
array = arrayMaker(size, modo)

time_inicial = datetime.now()

Quicksort(array, inicio, fim, quick_comps)

time_final = datetime.now()
quick_time = time_final - time_inicial
print(f'\n\nVetor ordenado com Quicksort:\n{array}')

#========================================================================

heap_comps = [0]
array = arrayMaker(size, modo)

time_inicial = datetime.now()

Heapsort(array, heap_comps)

time_final = datetime.now()
heap_time = time_final - time_inicial
print(f'\n\nVetor ordenado com Heapsort:\n{array}')
print('\n\n==================================================================\n')

print("Numeros de comparações | Tempos decorridos [milissegundos]:")
print(f"BubbleSort:{bubble_comps} | {bubble_time.microseconds/1000}")
print(f"SelectionSort:{selection_comps} | {selection_time.microseconds/1000}")
print(f"InsertioSort:{insertion_comps} | {insertion_time.microseconds/1000}")
print(f"MergeSort:{merge_comps} | {merge_time.microseconds/1000}")
print(f"QuickSort:{quick_comps} | {quick_time.microseconds/1000}")
print(f"HeapSort:{heap_comps} | {heap_time.microseconds/1000}")


#finaliza o arq
fp.close()