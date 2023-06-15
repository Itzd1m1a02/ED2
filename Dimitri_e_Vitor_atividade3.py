#atividade 3 de ED2
#Dupla: Dimitri e vitor

import sys

class Heroi:
    #[NOME | SOBRENOME| NOME HEROI | PODER | FRAQUEZA | LOCAL | PROFISSAO]
    def __init__(self):
        self.nome = ""
        self.sobrenome = ""
        self.nome_heroi = ""
        self.poder = ""
        self.fraqueza = ""
        self.local = ""
        self.profissao = ""
        
    def setnome(self, nome):
        self.nome = nome
    def getnome(self):
        return (self.nome)
    
    def setsobrenome(self, sobrenome):
        self.sobrenome = sobrenome
    def getsobrenome(self):
        return (self.sobrenome)
    
    def setnome_heroi(self, nome_heroi):
        self.nome_heroi = nome_heroi
    def getnome_heroi(self):
        return (self.nome_heroi)
    
    def setpoder(self, poder):
        self.poder = poder
    def getpoder(self):
        return (self.poder)
    
    def setfraqueza(self, fraqueza):
        self.fraqueza = fraqueza
    def getfraqueza(self):
        return (self.fraqueza)
    
    def setlocal(self, local):
        self.local = local
    def getlocal(self):
        return (self.local)
    
    def setprofissao(self, profissao):
        self.profissao = profissao
    def getprofissao(self):
        return (self.profissao)

def RRNSdoArquivo(arq):
    arq.seek(0)
    arq.readline()
    RRNs = []
    for line in arq:
        item = line.strip().split('|')
        RRN = int(item[0])
        RRNs.append(RRN)

    return RRNs

def criaID(line):
    registro = line.split('|')
    id = registro[0]
    return int(id)

def quickSort(array, inicio, fim, ordem):
    if inicio < fim:
       pivo = particiona(array, inicio, fim, ordem)
       quickSort(array,inicio,pivo-1, ordem)
       quickSort(array,pivo+1,fim, ordem)
def particiona(array, inicio, fim, ordem):
    pivo = array[inicio][1]#como e' um array de tuplas, inicio[1] e' o segundo elemento (RRN)
    esquerda = inicio
    direita = fim
    if ordem == 'C' or ordem == 'c':
        while esquerda < direita:
            while array[esquerda][1] <= pivo and esquerda < fim:
                esquerda += 1
            while array[direita][1] > pivo and direita >= inicio:
                direita -= 1
            if esquerda < direita:
                array[esquerda], array[direita] = array[direita], array[esquerda]

    elif ordem == 'd' or ordem == 'D':
        while esquerda < direita:
            while array[esquerda][1] >= pivo and esquerda < fim:
                esquerda += 1
            while array[direita][1] < pivo and direita >= inicio:
                direita -= 1
            if esquerda < direita:
                array[esquerda], array[direita] = array[direita], array[esquerda]

    else:
        print("Erro. ordem de ordenacao nao encontrado. Use C para crescente e D para decrescente.")#controle de erros
        quit()

    array[inicio], array[direita] = array[direita], array[inicio]

    return direita

def insertionSort (array, ordem):
    if ordem == 'C' or ordem == 'c':
        for i in range(1,len(array)):
            auxiliar = array[i]
            j = i - 1
            while (j >= 0) and (auxiliar[1] < array[j][1]):
                array[j+1] = array[j]
                j -= 1
            array[j+1] = auxiliar

    if ordem == 'D' or ordem == 'd':
        for i in range(1,len(array)):
            auxiliar = array[i]
            j = i - 1
            while (j >= 0) and (auxiliar[1] > array[j][1]):
                array[j+1] = array[j]
                j -= 1
            array[j+1] = auxiliar

    else:
        print("Erro. ordem de ordenacao nao encontrado. Use C para crescente e D para decrescente.")#controle de erros
        print('Encerrando...')
        quit()

    return array

def Max_Heap(array, i, size, ordem):
    maior = i
    esquerda = 2*i+1
    direita = 2*i+2
    if ordem == 'C' or ordem == 'c':
        if(esquerda <= (size-1)) and (array[esquerda][1] > array[i][1]):
            maior = esquerda
        if (direita <= (size-1)) and (array[direita][1] > array[maior][1]):
            maior = direita
    if ordem == 'D' or ordem == 'd':
        if(esquerda <= (size-1)) and (array[esquerda][1] < array[i][1]):
            maior = esquerda
        if (direita <= (size-1)) and (array[direita][1] < array[maior][1]):
            maior = direita
    else:
        print("Erro. ordem de ordenacao nao encontrado. Use C para crescente e D para decrescente.")#controle de erros
        print('Encerrando...')
        quit()
    if i != maior:
        array[i], array[maior] = array[maior], array[i]
        Max_Heap(array, maior, size - 1, ordem)    
def descobreFilhos(array, size, ordem):
    for i in range(size // 2, -1, -1):
        Max_Heap(array, i, size, ordem)
def heapSort(array, ordem):
    size = len(array)
    descobreFilhos(array, size, ordem)
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i]  = array[i], array[0]
        size -= 1
        Max_Heap(array, 0, size, ordem)

def mergeSort(array, inicio, fim, ordem):
    if fim <= inicio:
        return array
    else:
        meio = (inicio + fim) // 2
        mergeSort(array, inicio, meio, ordem)#caminha pela parte esquerda do vetor
        mergeSort(array, meio+1, fim, ordem)#caminha pela parte direita do vetor
        merge(array, inicio, meio, fim, ordem)#função que verifica se o vetor unitario formado e mior ou menor e junta dois vetores
def merge(array, inicio, meio, fim, ordem):
    vaux = array[:] #copia o vetor principal para um auxiliar
    p1 = inicio #função que anda o vetor esquerdo(inicial) sem alterar o vetor original
    p2 = meio + 1#função que recebe o meior do vetor array para fraguimentação ate ter um ou mais vetores unitarios
    if ordem == 'C' or ordem == 'c':
        for k in range(inicio, fim + 1): #for que vai ate o fim do vetor
            if p1 > meio: # se o ponto 1 da posição do inicio e maior que o numero no meio do vetor
                array[k] = vaux[p2] #então o valor salvo naquela posição do vetor aux e colocado no veor original
                p2 += 1 #posição + 1
            elif p2 > fim: #se o ponto 2 da posição do inicio e maior que o fim
                array[k] = vaux[p1]#então o valor salvo naquela posição do vetor aux e colocado no veor original
                p1 += 1
            elif vaux[p2][1] < vaux[p1][1]:#se o valor salvo no ponto p2 e menor que o valor salvo no p1
                array[k] = vaux[p2] 
                p2 += 1
            else:
                array[k] = vaux[p1]#se o valor salvo no ponto p1 e menor que o valor salvo no p2
                p1 += 1
    
    if ordem == 'D' or ordem == 'd':
        for k in range(inicio, fim + 1): #for que vai ate o fim do vetor
            if p1 > meio: # se o ponto 1 da posição do inicio e maior que o numero no meio do vetor
                array[k] = vaux[p2] #então o valor salvo naquela posição do vetor aux e colocado no veor original
                p2 += 1 #posição + 1
            elif p2 > fim: #se o ponto 2 da posição do inicio e maior que o fim
                array[k] = vaux[p1]#então o valor salvo naquela posição do vetor aux e colocado no veor original
                p1 += 1
            elif vaux[p2][1] > vaux[p1][1]:#se o valor salvo no ponto p2 e menor que o valor salvo no p1
                array[k] = vaux[p2] 
                p2 += 1
            else:
                array[k] = vaux[p1]#se o valor salvo no ponto p1 e menor que o valor salvo no p2
                p1 += 1

    else:
        print("Erro. ordem de ordenacao nao encontrado. Use C para crescente e D para decrescente.")#controle de erros
        print('Encerrando...')
        quit()

def writeOutputFile(inputfile, output, keysArray, size, top, qtde, sort, order):
    outputfile = open(output, 'w')

    outputfile.write(f'SIZE={size} TOP={top} QTDE={qtde} SORT={sort} ORDER={order}n')
    for item in keysArray:
        registro = buscaRegistro(inputfile, item[0])
        outputfile.write(registro + '\n')

    outputfile.close()

def buscaRegistro(file, rrn):
    file.seek(0)
    file.readline()
    for i in range(rrn):
        file.readline()
    registro = file.readline()
    return registro   

def main():
    inputfile = open('input.txt', 'r+')
    inputfile.seek(0,2)
    if inputfile.tell() == 0:
        print('Arquivo vazio. Encerrando...')
        quit()
    inputfile.seek(0)

    linha = inputfile.readline().strip()
    lista = linha.split(' ')
    #======================================================
    maiorRegistroDeBits = lista[0].replace('SIZE=', '')
    ultElemRemovido = lista[1].replace('TOP=', '')
    quantidade = lista[2].replace('QTDE=', '')
    metodoOrdenacao = lista[3].replace('SORT=', '')
    ordem = lista[4].replace('ORDER=', '')

    #controle de erro para os dados no cabecalho
    #os demais, aqui nao tratados, foram tratados nas funcoes que os manipulam
    #if maiorRegistroDeBits != 136 or ultElemRemovido != -1 or quantidade < 1:
    #    print('Erro. Dados do cabecalho improprios para uso. Encerrando...')
    #    quit()
    #======================================================

    #======================================================
    #RRNs = RRNSdoArquivo(inputfile)
    inputfile.seek(0)
    TabelaDeIndices = []#array de tuplas [(elemento 0, elemento 1)]
    RRN = 0
    for line in inputfile.readlines()[1:]:
        id = criaID(line)
        TabelaDeIndices.append((RRN, id))
        RRN += 1
    #======================================================

    if metodoOrdenacao == 'Q':#quick
        quickSort(TabelaDeIndices, 0, len(TabelaDeIndices)-1, ordem)

    elif metodoOrdenacao == 'H':#heap
        heapSort(TabelaDeIndices, ordem)

    elif metodoOrdenacao == 'M':#merge
        mergeSort(TabelaDeIndices, 0, len(TabelaDeIndices)-1, ordem)

    elif metodoOrdenacao == 'I':#insertion
        TabelaDeIndices = insertionSort(TabelaDeIndices,ordem)
        
    else:
        print("Erro. Metodo de ordenacao nao existente. Use, Q, H, M, ou I.")

    writeOutputFile(inputfile, 'output.txt', TabelaDeIndices, maiorRegistroDeBits, ultElemRemovido, quantidade, metodoOrdenacao, ordem)
    inputfile.close()

main()