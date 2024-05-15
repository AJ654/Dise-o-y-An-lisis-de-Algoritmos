#MAYORQUIN GALLEGOS ANGEL DE JESUS

import random

# Función para reorganizar un heap
def heapify(arr, n, i):
    largest = i  # Suponemos que el elemento actual es el mayor
    left = 2 * i + 1  # Hijo izquierdo
    right = 2 * i + 2  # Hijo derecho

    # Si el hijo izquierdo es mayor que el elemento actual
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Si el hijo derecho es mayor que el mayor actual
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Si el mayor no es el elemento actual, intercambiamos y ajustamos el heap
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursivamente reorganizamos el subárbol
        heapify(arr, n, largest)

# Función para aplicar Heapsort
def heapsort(arr):
    n = len(arr)
    # Construimos el heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraemos elementos del heap y reorganizamos
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

cantidad = int(input("Ingresa la cantidad de elementos aleatorios para ordenar: "))

# Generar una lista de valores aleatorios entre 1 y 100
valores = [random.randint(0, cantidad) for _ in range(cantidad)]

print("Lista sin ordenar:", valores)

# Ordenar la lista usando Heapsort
heapsort(valores)

print("Lista ordenada:", valores)
