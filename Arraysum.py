#MAYORQUIN GALLEGOS ANGEL DE JESUS

def simpleArraySum(ar):
    sum = 0
    for i in range(len(ar)):
        sum += ar[i]
    return sum

ar_count_temp = input("Ingrese el tamaño del arreglo: ")
ar_count = int(ar_count_temp)

ar_temp_temp = input("Ingrese los elementos del arreglo separados por espacios: ")
ar_temp = ar_temp_temp.split()

ar = list(map(int, ar_temp))

result = simpleArraySum(ar)

print(result)