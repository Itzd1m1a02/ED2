import numpy as np
def somaFracao(x, y, quant): 
    # Inicializa o numerador e o denominador para a soma
    numerador_soma = 0
    denominador_soma = y[0]  # Inicializa com o denominador da primeira fração

    # Calcula o mínimo múltiplo comum (MMC) de todos os denominadores
    for i in range(quant):
        denominador_soma = np.lcm(denominador_soma, y[i])

    # Calcula a soma das frações
    for i in range(quant):
        numerador_soma += (x[i] * (denominador_soma // y[i]))
        
    print(f"A soma das frações é: {numerador_soma}/{denominador_soma}")
    
def subFracao(x, y, quant): 
    # Inicializa o numerador e o denominador para a sub
    numerador_sub = [0] * quant
    denominador_sub = y[0]  # Inicializa com o denominador da primeira fração

    # Calcula o mínimo múltiplo comum (MMC) de todos os denominadores
    for i in range(quant):
        denominador_sub = np.lcm(denominador_sub, y[i])

    # Calcula a sub das frações
    for i in range(quant):
        numerador_sub[i] = (x[i] * (denominador_sub // y[i]))
        
    sub = numerador_sub[0]
    for i in range(1, quant):
        sub = sub - numerador_sub[i]
        
    print(f"A soma das frações é: {sub}/{denominador_sub}")
    
def multiplicacao(x,y, quant):
    mulTotalNumerador = x[0]
    for i in range(1, quant):
        mulTotalNumerador = mulTotalNumerador * x[i]
        
    mulTotalDenominador = y[0]
    for i in range(1, quant):
        mulTotalDenominador = mulTotalDenominador * y[i]
        
    print(f"Multiplicacao das fracoes: {mulTotalNumerador}/{mulTotalDenominador}")
    
def divisao(x,y,quant):
    # Inicializa o numerador e o denominador para a divisão
    numerador_div = x[0]
    denominador_div = y[0]

    # Calcula a divisão das frações
    for i in range(1, quant):
        numerador_div *= y[i]
        denominador_div *= x[i]
    
    print(f"Resultado da divisão: {numerador_div}/{denominador_div}")       
        
if __name__ == "__main__":
    quant = int(input("Digite a quantidade de fracoes: "))
    while quant <= 1:
        quant = int(input("Digite a quantidade de fracoes: "))
    
    x = [0] * quant
    y = [0] * quant
    
    for i in range(quant):
        x[i] = int(input(f"{i+1} - numerador: "))
        y[i] = int(input(f"{i+1} - denominador: "))
    
    while True:
        print("-1-sair do programa\n1-soma\n2-subtracao\n3-multiplicao\n4-divisao")
        aux = int(input("opcao: "))    
        if aux == 1:
            print("\n")
            somaFracao(x,y,quant)    
        elif aux == 2:
            print("\n")
            subFracao(x,y,quant)
        elif aux == 3:
            print("\n")
            multiplicacao(x,y,quant)
        elif aux == 4:
            print("\n")
            divisao(x,y,quant)
        elif aux == -1:
            quit()
        else:
            print("valor invalido! Tente novamente.\n")