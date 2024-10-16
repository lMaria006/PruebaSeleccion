def generar_combinaciones(monedas):
 
    monedas.sort()  # Ordenar para manejar duplicados fácilmente
    combinaciones = []
    combinacion_actual = []
    
    def backtrack(start):
        combinaciones.append(combinacion_actual.copy())
        
        for i in range(start, len(monedas)):
            if i > start and monedas[i] == monedas[i - 1]:
                continue
            combinacion_actual.append(monedas[i])
            backtrack(i + 1)
            combinacion_actual.pop()
    
    backtrack(0)
    return combinaciones

def calcular_sumas(combinaciones):
    sumas = set()
    for combinacion in combinaciones:
        sumas.add(sum(combinacion))
    return sumas

def main():
    monedas = [5, 7, 1, 1, 2, 3, 22]
    
    combinaciones = generar_combinaciones(monedas)
    
    print(f"Total de combinaciones posibles: {len(combinaciones)}\n")
    print("Listado de todas las combinaciones:")
    for idx, combinacion in enumerate(combinaciones, 1):
        print(f"{idx}: {combinacion}")
    
    sumas_unicas = calcular_sumas(combinaciones)
    
    print(f"\nTotal de sumas únicas posibles: {len(sumas_unicas)}")
    print("Listado de todas las sumas únicas:")
    print(sorted(sumas_unicas))
    
if __name__ == "__main__":
    main()

