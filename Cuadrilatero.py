#MAYORQUIN GALLEGOS ANGEL DE JESUS

def identificar_cuadrilatero(lados):
    lados.sort()  # Ordenar los lados de menor a mayor para facilitar la identificación

    if len(set(lados)) == 1:
        return "Cuadrado"
    elif len(set(lados)) == 2:
        if lados[0] == lados[1] and lados[2] == lados[3]:
            return "Rectángulo"
        else:
            return "Paralelogramo"
    else:
        return "Otro cuadrilátero"

lados = []
for i in range(4):
    lado = float(input(f"Ingrese la medida del lado {i+1}: "))
    lados.append(lado)

tipo = identificar_cuadrilatero(lados)
print(f"El cuadrilátero es: {tipo}")