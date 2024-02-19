#MAYORQUIN GALLEGOS ANGEL DE JESUS

UNIDADES = ['', 'UNO', 'DOS', 'TRES', 'CUATRO', 'CINCO', 'SEIS', 'SIETE', 'OCHO', 'NUEVE']
DECENAS = ['', 'DIEZ', 'VEINTE', 'TREINTA', 'CUARENTA', 'CINCUENTA', 'SESENTA', 'SETENTA', 'OCHENTA', 'NOVENTA']
CENTENAS = ['', 'CIENTO', 'DOSCIENTOS', 'TRESCIENTOS', 'CUATROCIENTOS', 'QUINIENTOS', 'SEISCIENTOS', 'SETECIENTOS', 'OCHOCIENTOS', 'NOVECIENTOS']

def convertidorNumLetra(numero):
    unidades = numero % 10
    decenas = (numero % 100) // 10
    centenas = (numero % 1000) // 100

    if numero == 0:
        return 'CERO'
    elif numero < 10:
        return UNIDADES[numero]
    elif numero == 10:
        return 'DIEZ'
    elif numero == 11:
        return 'ONCE'
    elif numero == 12:
        return 'DOCE'
    elif numero == 13:
        return 'TRECE'
    elif numero == 14:
        return 'CATORCE'
    elif numero == 15:
        return 'QUINCE'
    elif numero > 15 and numero < 20:
        return 'DIECI' + UNIDADES[numero-10]
    elif numero == 20:
        return 'VEINTE'
    elif numero > 20 and numero < 30:
        return 'VEINTI' + UNIDADES[numero-20]
    elif numero > 30 and numero < 100:
        if unidades == 0:
            return DECENAS[decenas]
        else:
            return DECENAS[decenas] + ' Y ' + UNIDADES[unidades]
    elif numero >= 100 and numero < 1000:
        if numero == 100:
            return 'CIEN'
        else:
            return CENTENAS[centenas] + ' ' + convertidorNumLetra(numero % 100)
    elif numero >= 1000 and numero < 1000000:
        miles = numero // 1000
        resto = numero % 1000
        if miles == 1:
            return 'MIL ' + convertidorNumLetra(resto)
        else:
            return convertidorNumLetra(miles) + ' MIL ' + convertidorNumLetra(resto)
    elif numero >= 1000000 and numero < 1000000000:
        millones = numero // 1000000
        resto = numero % 1000000
        if millones == 1:
            return 'UN MILLON ' + convertidorNumLetra(resto)
        else:
            return convertidorNumLetra(millones) + ' MILLONES ' + convertidorNumLetra(resto)
    elif numero >= 1000000000 and numero < 1000000000000:
        billones = numero // 1000000000
        resto = numero % 1000000000
        if billones == 1:
            return 'UN BILLON ' + convertidorNumLetra(resto)
        else:
            return convertidorNumLetra(billones) + ' BILLONES ' + convertidorNumLetra(resto)
    elif numero >= 1000000000000 and numero < 1000000000000000:
        trillones = numero // 1000000000000
        resto = numero % 1000000000000
        if trillones == 1:
            return 'UN TRILLON ' + convertidorNumLetra(resto)
        else:
            return convertidorNumLetra(trillones) + ' TRILLONES ' + convertidorNumLetra(resto)

numero = int(input('Ingrese un número: '))
print(convertidorNumLetra(numero))