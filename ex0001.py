#-3 -16 18 36 -12 -25 -31 -15 13 16 0 -45 -41 -22 12
def  BubbleSort (x,y):
    trocou = True
    if  y == 1:
        while trocou == True:
            trocou = False
            for i in range(0, len(x)-1):
                print(x)
                if x[i] > x[i+1]:
                    x[i], x [i+1] = x[i+1], x[i]
                    trocou = True
    if  y == -1:
        while trocou == True :
            trocou = False
            for i in range(0, len(x)-1):
                print(x)
                if x[i] < x[i+1]:
                    x[i], x [i+1] = x[i+1], x[i]
                    trocou = True
def info ():
    print('Digite 1 para ordem crecente\nDigite -1 para decrecente\n')

x  = [-3,-16,18,36,-12,-25,-31,-15,13,16,0,-45,-41,-22,12]
info()
y = int (input('Digite uma opção para ordenação: '))
while y < -1 or y > 1 or y == 0:
    info()
    y = int (input('Digite uma opção para ordenação: '))
BubbleSort (x,y)
