#MAYORQUIN GALLEGOS ANGEL DE JESUS

import random

# Función para fusionar dos mitades ordenadas
def merge(left, right):
    result = []
    i = 0
    j = 0
    # Comparamos y fusionamos las listas
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Añadimos los elementos restantes
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Función recursiva para Mergesort
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    # Dividimos la lista en dos mitades
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    # Fusionamos las dos mitades ordenadas
    return merge(left, right)

cantidad = int(input("Ingresa la cantidad de elementos aleatorios para ordenar: "))

# Generar una lista de valores aleatorios entre 1 y 100
valores = [random.randint(0, cantidad) for _ in range(cantidad)]

print("Lista sin ordenar:", valores)

# Ordenar la lista usando Mergesort
valores_ordenados = mergesort(valores)

print("Lista ordenada:", valores_ordenados)
