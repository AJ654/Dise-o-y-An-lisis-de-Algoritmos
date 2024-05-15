#MAYORQUIN GALLEGOS ANGEL DE JESUS

import random

# Algoritmo de selección para ordenar la lista
def seleccion(arr):
    n = len(arr)
    # Iteramos a través de cada elemento del array
    for i in range(n):
        # Suponemos que el primer elemento no ordenado es el menor
        min_idx = i
        # Recorremos el resto de elementos para encontrar el menor
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambiar el elemento más pequeño con el primer elemento no ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

cantidad = int(input("Ingresa la cantidad de elementos aleatorios para ordenar: "))

# Generar una lista de valores aleatorios entre 1 y 100
valores = [random.randint(0, cantidad) for _ in range(cantidad)]

print("Lista sin ordenar:", valores)

# Ordenar la lista usando Selection Sort
seleccion(valores)

print("Lista ordenada:", valores)
