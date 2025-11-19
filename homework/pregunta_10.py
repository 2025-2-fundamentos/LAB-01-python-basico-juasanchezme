"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    with open("files/input/data.csv", "r") as file:      #?Abrir el archivo en lectura (r)
            lineas = file.readlines()                    #? Leer las líneas y guardarlas en la lista 'lineas'

    Rta = []                                             #?Crear una lista vacía llamada 'Rta' para almacenar las tuplas

    for linea in lineas:                                 #? Iterar sobre cada línea del archivo
        partes = linea.strip().split("\t")               #?Eliminar saltos de línea y dividir por tabulaciones
        letra = partes[0]                                #? Obtener la letra de la columna 1 (parte[0])
        columna_4 = partes[3].split(",")                 #? Obtener los elementos de la columna 4 (separados por coma) y convertirlos en una lista
        columna_5 = partes[4].split(",")                 #?Obtener los elementos de la columna 5 (separados por coma) y convertirlos en una lista
        Rta.append((letra, len(columna_4), len(columna_5)))  #? Añadir una tupla con la letra y las longitudes de las listas de columna 4 y columna 5 a 'Rta'

    return Rta
print(pregunta_10())
