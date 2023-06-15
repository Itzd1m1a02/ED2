class NoBTreeNode:
    def __init__(self, folha=False):
        self.chaves = []
        self.filho = []
        self.folha = folha

class ArvoreB:
    def __init__(self, t):
        self.raiz = NoBTreeNode(True)
        self.tamanho_minimo = t

    def inserir(self, k):
        raiz = self.raiz
        if len(raiz.chaves) == (2 * self.tamanho_minimo) - 1:
            temp = NoBTreeNode()
            self.raiz = temp
            temp.filho.insert(0, raiz)
            self.dividir_filho(temp, 0)
            self.inserir_nao_cheio(temp, k)
        else:
            self.inserir_nao_cheio(raiz, k)

    def inserir_nao_cheio(self, x, k):
        i = len(x.chaves) - 1
        if x.folha:
            x.chaves.append(k)
            while i >= 0 and k < x.chaves[i]:
                x.chaves[i + 1] = x.chaves[i]
                i -= 1
            x.chaves[i + 1] = k
        else:
            while i >= 0 and k < x.chaves[i]:
                i -= 1
            i += 1
            if len(x.filho[i].chaves) == (2 * self.tamanho_minimo) - 1:
                self.dividir_filho(x, i)
                if k > x.chaves[i]:
                    i += 1
            self.inserir_nao_cheio(x.filho[i], k)

    def dividir_filho(self, x, i):
        t = self.tamanho_minimo
        y = x.filho[i]
        z = NoBTreeNode(y.folha)
        x.filho.insert(i + 1, z)
        x.chaves.insert(i, y.chaves[t - 1])
        z.chaves = y.chaves[t: (2 * t) - 1]
        y.chaves = y.chaves[0: t - 1]
        if not y.folha:
            z.filho = y.filho[t: 2 * t]
            y.filho = y.filho[0: t - 1]

    def exibir(self, x, l=0):
        print("Nível da arvore: ", l, " quant => ", len(x.chaves), end=": ")
        for i in x.chaves:
            print(f'{i} ', end=" ")
        print()
        l += 1
        if len(x.filho) > 0:
            for i in x.filho:
                self.exibir(i, l)

# Exemplo de uso
tamanho_arvore = int(input("Digite o tamanho desejado da arvore:"))
arvore_b = ArvoreB(tamanho_arvore)  # Define o valor de t para a árvore B (3 neste caso)

# Insere os números na árvore B
while(True):
    print("Digite S para sair\n")
    item = input("Digite um numero para adiciona lo na arvore:")
    if(item == 'S' or item == 's'):
        break
    else:
        item = int(item)
        arvore_b.inserir(item)
        
# Exibe a árvore B
arvore_b.exibir(arvore_b.raiz)
