def Quicksort(V, inicio, fim):
    if inicio < fim:
        pivo = particionar(V, inicio, fim)
        Quicksort(V, inicio, pivo-1)
        Quicksort(V, pivo+1, fim)
def particionar(V, inicio, fim):
    esq = inicio
    dir = fim
    pivo = V[inicio]
    while (esq < dir):
        while (V[esq] <= pivo and esq <= fim):
            esq += 1
        while (V[dir] > pivo and dir >= inicio):
            dir -= 1
        if (esq < dir):
            V[esq], V[dir] = V[dir], V[esq]
    V[dir], V[inicio] = V[inicio], V[dir]
    return dir
   
V = [-3,-16,18,36,-12,-25,-31,-15,13,16,0,-45,-41,-22,12]
inicio = 0
fim = len(V) - 1
Quicksort(V, inicio, fim)
print('Vetor ordenado: ', V)
