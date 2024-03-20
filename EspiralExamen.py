#MAYORQUIN GALLEGOS ANGEL DE JESUS

def printEspiral(n):
    matrix = [[0] * n for _ in range(n)]

    # Define los límites de la matriz
    tope, fondo, izquierda, derecha = 0, n - 1, 0, n - 1

    num = 1

    while num <= n * n:
        # Llenar la fila superior
        for i in range(izquierda, derecha + 1):
            matrix[tope][i] = num
            num += 1
        tope += 1

        # Llenar la columna derecha
        for i in range(tope, fondo + 1):
            matrix[i][derecha] = num
            num += 1
        derecha -= 1

        # Llenar la fila inferior de adelante para atras
        for i in range(derecha, izquierda - 1, -1):
            matrix[fondo][i] = num
            num += 1
        fondo -= 1

        # Llenar la columna izquierda de abajo para arriba
        for i in range(fondo, tope - 1, -1):
            matrix[i][izquierda] = num
            num += 1
        izquierda += 1

    for row in matrix:
        for num in row:
            print(num, end='\t')
        print()

x = int(input("Ingrese un número: "))
square = x ** 2

# Llamar a la función para imprimir la matriz en espiral
printEspiral(x)