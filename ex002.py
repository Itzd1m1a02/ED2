def selectsort(x, y):
    for i in range(0, y-1):
        menor = i
        for j in range(i, y):
            if x[j] < x[menor]:
                menor = j
        if i != menor:
            x[i], x[menor] = x[menor], x[i] 
    print(x)            

array = [-3, -16, 18, 36, -12, -25, -31, -15, 13, 16,  0, -45, -41, -22, 12]
tam_array = len(array)

selectsort(array, tam_array)
