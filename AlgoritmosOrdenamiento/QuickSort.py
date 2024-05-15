#MAYORQUIN GALLEGOS ANGEL DE JESUS

import random

# Función para dividir el array y posicionar el pivote
def particion(arr, low, high):
    pivot = arr[high]  # Elegimos el último elemento como pivote
    i = low - 1  # Índice para el elemento más pequeño
    # Recorremos el array y colocamos los elementos menores al pivote a la izquierda
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Intercambiamos
    # Colocamos el pivote en su posición correcta
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Función recursiva de Quicksort
def quicksort(arr, low, high):
    if low < high:
        # Obtenemos el índice del pivote después de la partición
        pi = particion(arr, low, high)
        # Ordenamos recursivamente las dos mitades
        quicksort(arr, low, pi - 1)  # Parte izquierda del pivote
        quicksort(arr, pi + 1, high)  # Parte derecha del pivote

cantidad = int(input("Ingresa la cantidad de elementos aleatorios para ordenar: "))

# Generar una lista de valores aleatorios entre 1 y 100
valores = [random.randint(0, cantidad) for _ in range(cantidad)]

print("Lista sin ordenar:", valores)

# Ordenar la lista usando Quicksort
quicksort(valores, 0, len(valores) - 1)

print("Lista ordenada:", valores)
