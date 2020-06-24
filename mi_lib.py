import random

def crea_arreglo(n,m):
    
    matriz = []
    
    for i in range(n):
        matriz.append([])
        for j in range(m):
            matriz[i].append(random.randint(0, 100))
            
    return matriz

n = int(input("Ingrese el número de filas: \n"))
m = int(input("Ingrese el número de columnas: \n"))
print("")
print("Matriz: ")
print("")
print(crea_arreglo(n,m))