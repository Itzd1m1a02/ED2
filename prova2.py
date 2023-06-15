class Game:
    def __init__(self):
        self.nome = ""
        self.produtora = ""
        self.genero = ""
        self.plataforma = ""
        self.ano = ""
        self.classificacao = ""
        self.preco = ""
        self.midia = ""
        self.tamanho = ""

    def setNome(self, nome):
        self.nome = nome
    def getNome(self):
        return (self.nome)
    
    def setGenero(self, genero):
        self.genero = genero
    def getGenero(self):
        return (self.genero)
    
    def setPlataforma(self, plataforma):
        self.plataforma = plataforma
    def getPlataforma(self):
        return (self.plataforma)
    
    def setAno(self, ano):
        self.ano = ano
    def getAno(self):
        return (self.ano)
    
    def setClassificacao(self, classificacao):
        self.classificacao = classificacao
    def getClassificacao(self):
        return (self.classificacao)
    
    def setPreco(self, preco):
        self.preco = preco
    def getPreco(self):
        return (self.preco)
    
    def setMidia(self, midia):
        self.midia = midia
    def getMidia(self):
        return (self.midia)
    
    def setTamanho(self, tamanho):
        self.tamanho = tamanho
    def getTamanho(self):
        return (self.tamanho)
    
    def setProdutora(self, produtora):
        self.produtora = produtora
    def getProdutora(self):
        return (self.produtora)

def KeyPrimary(arq):
    TabelaDeIndices1 = []
    ChavesCanonicasPrimarias = []
    RRNs = []
    RRN = 0
    for line in arq.readlines()[4:19]:
        RRN += 1
        registro = line.split('|')
        chaveprimaria = registro[0] + registro[4]
        chaveprimaria = chaveprimaria.upper().replace(' ', '')
        ChavesCanonicasPrimarias.append(chaveprimaria)
        RRNs.append(RRN)

    for i in range(len(RRNs)):
        TabelaDeIndices1.append((RRNs[i], ChavesCanonicasPrimarias[i]))

    return TabelaDeIndices1, ChavesCanonicasPrimarias, RRNs

def KeySecundary(chavesPrimarias, arq):
    arq.seek(0)
    TabelaDeIndices2 = []
    ChavesCanonicasSecundarias = []
    for line in arq.readlines()[4:19]:
        registro = line.split('|')
        chavesecundaria = registro[1]
        chavesecundaria = chavesecundaria.upper().replace(' ', '')
        ChavesCanonicasSecundarias.append(chavesecundaria)

    for i in range(len(ChavesCanonicasSecundarias)):
        TabelaDeIndices2.append((ChavesCanonicasSecundarias[i], chavesPrimarias[i]))

    return TabelaDeIndices2, ChavesCanonicasSecundarias

def WriteArq(arq, primaria, secundaria, UltRemove):
    # Escreve os dados do arquivo com um cabeçalho
    arq.seek(0)
    Dados = open('Dados.txt', 'w')
    Dados.write(f'QTDE={16} TOP={UltRemove}\n')
    for line in arq.readlines()[4:19]:
        Dados.write(line)
    Dados.close()

    # Escreve os dados da tabela primária no arquivo
    primario = open('TabelaPrimaria.txt', 'w')
    primario.write('Tabela Primaria:\n')
    for i in range(len(primaria)):
        primario.write(str(primaria[i]) + '\n')
    primario.close()

    # Escreve os dados da tabela secundária no arquivo
    secundario = open('TabelaSecundaria.txt', 'w')
    secundario.write('Tabela Secundaria:\n')
    for i in range(len(secundaria)):
        secundario.write(str(secundaria[i]) + '\n')
    secundario.close()

def AddRegistro(arq, ChavesCanonicas1, ChavesCanocicas2, primaria, secundaria, RRNs):
    arq.seek(0)
    RRN = len(RRNs)
    addList = []

    for line in arq.readlines()[22:29]:        
        registro = line.split('|')
        chaveprimaria = registro[0] + registro[4]
        chaveprimaria = chaveprimaria.upper().replace(' ', '')

        if chaveprimaria not in set(ChavesCanonicas1):
            RRN += 1
            ChavesCanonicas1.append(chaveprimaria)
            RRNs.append(RRN)
            primaria.append((RRN, chaveprimaria))
            chavesecundaria = registro[1]
            chavesecundaria = chavesecundaria.upper().replace(' ', '')
            ChavesCanocicas2.append(chavesecundaria)
            secundaria.append((chavesecundaria, chaveprimaria))   
            
            # Cria uma nova instância de Game para cada registro
            game = Game()
            game.setNome(registro[0])
            game.setProdutora(registro[1])
            game.setGenero(registro[2])
            game.setPlataforma(registro[3])
            game.setAno(registro[4])
            game.setClassificacao(registro[5])
            game.setPreco(registro[6])
            game.setMidia(registro[7])
            game.setTamanho(registro[8])
            
            addList.append(game)

    #criação de tabela aux1 para não alterar a estrutura primaria principal
    tabelaaux1 = []
    tabelaaux1[:] = primaria
    tabelaaux1.sort(key=lambda a: a[1])
    
    print('\nDados Após Adicição na Tabela Primaria:\n')
    for j in range(len(tabelaaux1)):
        print(tabelaaux1[j])
    
    #criação de tabela aux2 para não alterar a estrutura secundaria principal
    tabelaaux2 = []
    tabelaaux2[:] = secundaria
    tabelaaux2.sort(key=lambda a: a[0])
    
    print('\nDados Após Adicição na Tabela secundaria:\n')
    for j in range(len(tabelaaux2)):
        print(tabelaaux2[j])

    return addList

def getRRNs(chave, TabelaPrimaria):
    rrns = []
    for i, item in enumerate(TabelaPrimaria):
        if item[1] == chave:
            rrns.append(i)
    return rrns
def RemoveCanonica2(chave, TabelaSecundaria):
    TabelaSecundaria[:] = [item for item in TabelaSecundaria if item[1] != chave]
def RemoveRegistro(arq, ChaveCanonica1, TabelaPrimaria, TabelaSecundaria, RRNs):
    removelist = []
    arq.seek(0)
    for line in arq.readlines()[32:39]:
        registro = line.split('|')
        ChaveDeRemocao = registro[0] + registro[4]
        ChaveDeRemocao = ChaveDeRemocao.upper().replace(' ', '')
        if ChaveDeRemocao in set(ChaveCanonica1):  # se achou o item para remover 
            rrns = getRRNs(ChaveDeRemocao, TabelaPrimaria)
            rrns.sort(reverse=True)  # Ordenar em ordem decrescente para remover corretamente
            for index in rrns:
                TabelaPrimaria.pop(index)
                RemoveCanonica2(ChaveDeRemocao, TabelaSecundaria)
            # Atualizar os RRNs
            for i in range(len(TabelaPrimaria)):
                TabelaPrimaria[i] = (i + 1, TabelaPrimaria[i][1])
                
        game = Game()
        game.setNome(registro[0])
        game.setProdutora(registro[1])
        game.setGenero(registro[2])
        game.setPlataforma(registro[3])
        game.setAno(registro[4])
        game.setClassificacao(registro[5])
        game.setPreco(registro[6])
        game.setMidia(registro[7])
        game.setTamanho(registro[8])
        
        removelist.append(game)

    print('\nDados Após Remoção na Tabela Primária:\n')
    TabelaPrimaria.sort(key=lambda a: a[1])
    for j in range(len(TabelaPrimaria)):
        print(TabelaPrimaria[j])
    
    print('\nDados Após Remoção na Tabela Secundária:\n')
    TabelaSecundaria.sort(key=lambda a: a[0])
    for j in range(len(TabelaSecundaria)):
        print(TabelaSecundaria[j])
    
    return removelist

def main():
    inputFile = open('DimitriPereiraMaia.txt', 'r+')
    TabelaPrimaria, chavescanonicas1, RRNs = KeyPrimary(inputFile)
    TabelaSecundaria, chavecanonicas2 = KeySecundary(chavescanonicas1, inputFile)
    UltRemove = -1
    
    #criação de tabela aux1 para não alterar a estrutura primaria principal
    tabelaaux1 = []
    tabelaaux1[:] = TabelaPrimaria
    #ordenada em ordem alfabética com base na chave canônica 1
    tabelaaux1.sort(key=lambda a: a[1])
    
    print('\nTabela de Índices Primários Base:\n')
    for i in range(len(tabelaaux1)):
        print(tabelaaux1[i])

    #criação de tabela aux2 para não alterar a estrutura secundaria principal
    tabelaaux2 = []
    tabelaaux2[:] = TabelaSecundaria
    #ordenada em ordem alfabética com base na chave canônica 2
    tabelaaux2.sort(key=lambda a: a[0])
    
    print('\nTabela de Índices Secundários Base:\n')
    for i in range(len(tabelaaux2)):
        print(tabelaaux2[i])

    #chamada das funções
    addlista = AddRegistro(inputFile, chavescanonicas1, chavecanonicas2, TabelaPrimaria, TabelaSecundaria, RRNs)
    removelist = RemoveRegistro(inputFile, chavescanonicas1, TabelaPrimaria, TabelaSecundaria, RRNs)
    WriteArq(inputFile, TabelaPrimaria, TabelaSecundaria, UltRemove)
    
    

main()