"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open("files/input/data.csv", "r") as file:      #?Abrir el archivo en lectura (r)
            lineas = file.readlines()                    #? Leer las líneas y guardarlas en la lista 'lineas'

    suma_por_letra = {}                                  #? Crear un diccionario vacío para almacenar la suma por letra

    for linea in lineas:                                #? Iterar sobre cada línea del archivo
        partes = linea.strip().split("\t")               #? Eliminar saltos de línea y dividir la línea por tabulaciones  
        letra = partes [0]                                 #? Obtener la letra de la columna 1 (columna 0)
        columna_5 = partes [4].split(",")                #? Obtener los valores de la columna 5 y separarlos por coma

        suma_columna_5 = sum(int(valor.split(":") [1] ) for valor in columna_5) #? Sumar los valores en la columna 5 (después de dividir por ':', se toma la parte numérica)

        if letra not in suma_por_letra:
            suma_por_letra[letra] = 0
        suma_por_letra[letra] += suma_columna_5         #? Añadir la suma de la columna 5 al valor correspondiente de la letra

    return suma_por_letra
print(pregunta_12())
