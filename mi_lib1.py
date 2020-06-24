import numpy as np



n = int(input("Ingrese el numero de fila: \n"))
m = int(input("Ingrese el numero de columna: \n"))
s = int(input("Columna que desea mover al final: \n"))


matriz = np.random.randint(0, 100, size=(n, m))

print(matriz)

print(matriz[1:])