"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open("files/input/data.csv", "r") as file:                 #? abrir el archivo en lectura (r)
        lineas = file.readlines()                                   #?leer las lineas y guardarlas en la lista lineas
    Valores = {}                                                    #?diccionario 
    for linea in lineas:
        partes = linea.strip().split("\t")                          #?elimina saltos de linea y divide las tabulaciones  
        letra = partes[0]                                           #?letra en la columnauno 
        valor = int(partes[1])                                      #?valor numerico en la columna 2 convertido a int

        if letra in Valores:                                        #?agrupacion de valores por letra
            Valores[letra].append(valor)
        else:
            Valores[letra] = [valor]
    
    resultado = []
    for letra in sorted(Valores.keys()):                            #?letras organizadas con sorted
        maximo_valor = max(Valores[letra])                          #?valor maximo en la lista de valores
        minimo_valor = min(Valores[letra])                          #?valor minimo
        resultado.append((letra, maximo_valor, minimo_valor))       #?se crea la tupla y se agregan en la lista resultado
    return resultado

print(pregunta_05())
