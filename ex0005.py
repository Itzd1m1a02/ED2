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
            while esquerda < direita and array[esquerda] <= pivo:
                esquerda += 1
            while array[direita] >= pivo and direita > esquerda:
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
            while esquerda < direita and array[esquerda] >= pivo:
                esquerda += 1
            while array[direita] <= pivo and direita > esquerda:
                direita -= 1
            if direita < esquerda:
                aux = True
            else:
                array[esquerda], array[direita] = array[direita], array[esquerda]
                cont[0] += 1
        array[inicio], array[direita] = array[direita], array[inicio]
        cont[0] += 1
        return direita
