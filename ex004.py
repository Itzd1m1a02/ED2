def MergeSort(V, inicio, fim):
    if inicio < fim:
        Meio = int(((inicio + fim) / 2))
        MergeSort(V, inicio, Meio)
        MergeSort(V, meio+1, fim)
        Merge(V, inicio, meio, fim)

def Merge(V, inicio, meio, fim):
    Vaux = V
    p1 = inicio
    p2 = meio+1
    cont = 0
    while p1 <= meio and p2 <= fim:
        if V[p1] < V[p2]: 
            aux[cont] = V[p1]
            p1 = p1 + 1
        else: 
            aux[contador] = V[p2]
            p2 = p2 + 1
        cont = cont + 1 

array = [-3, -16, 18, 36, -12, -25, -31, -15, 13, 16,  0, -45, -41, -22, 12]
inicio = 0
fim = len(array) - 1
MergeSort(array, inicio, fim)