#biblioteca:
def formaHeap(array, i, size, modo):
    maior = i
    esquerda = 2*i+1
    direita = 2*i+2
    if modo == 1:
        if(esquerda <= (size-1)) and (array[esquerda] < array[i]):
            maior = esquerda
        if (direita <= (size-1)) and (array[direita] < array[maior]):
            maior = direita
        if i != maior:
            array[i], array[maior] = array[maior], array[i]
            formaHeap(array, maior, size - 1)
    if modo == -1:
        if(esquerda <= (size-1)) and (array[esquerda] > array[i]):
            maior = esquerda
        if (direita <= (size-1)) and (array[direita] > array[maior]):
            maior = direita
        if i != maior:
            array[i], array[maior] = array[maior], array[i]
            formaHeap(array, maior, size - 1)
def heap_max(array, size, modo):
    aux = range(size // 2, -1, -1)
    for i in aux:
        formaHeap(array, i, size, modo)

def Heapsort(array, modo):
    size = len(array)
    heap_max(array, size)
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i]  = array[i], array[0]
        size = size - 1
        formaHeap(array, 0, size, modo)