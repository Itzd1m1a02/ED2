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