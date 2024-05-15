#MAYORQUIN GALLEGOS ANGEL DE JESUS

import random

def insercion(arr):
    # Recorremos desde el segundo elemento hasta el final
    for i in range(1, len(arr)):
        clave = arr[i]  # Elemento a insertar
        j = i - 1
        # Desplazar los elementos que son mayores que 'clave' hacia la derecha
        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave  # Insertar el elemento en su posición correcta

cantidad = int(input("Ingresa la cantidad de elementos aleatorios para ordenar: "))

# Generar una lista de valores aleatorios entre 1 y 100
valores = [random.randint(0, cantidad) for _ in range(cantidad)]

print("Lista sin ordenar:", valores)

# Ordenar la lista usando Insertion Sort
insercion(valores)

print("Lista ordenada:", valores)
