#MAYORQUIN GALLEGOS ANGEL DE JESUS

import random

def burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Intercambio de elementos si están en el orden incorrecto
                arr[j], arr[j+1] = arr[j+1], arr[j]


cantidad = int(input("Ingresa la cantidad de elementos para ordenar: "))

# Generar una lista de valores aleatorios entre 1 y 100
valores = [random.randint(0, cantidad) for _ in range(cantidad)]

print("Lista sin ordenar:", valores)

burbuja(valores)

print("Lista ordenada:", valores)
