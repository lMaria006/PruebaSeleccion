S = 6 
limite = S * S

def cuadrados_ordenados(matriz):
    salida = []
    i = 0
    j = 0 
    
    for num in matriz:
        cuadrado = num * num
        if 0 <= cuadrado <= limite:
            salida.append(cuadrado)
    for i in range(len(salida)):
       for j in range(i+1, len(salida)):
           if salida [i] > salida [j]:
               salida[i], salida[j] = salida[j], salida[i] 
               
    return salida


matriz = [2,3,4,5]
print(cuadrados_ordenados(matriz))