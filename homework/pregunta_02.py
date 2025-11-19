"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    traductor = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E':4}
    with open('files/input/data.csv', 'r') as file:
        repeticiones = [0,0,0,0,0]
        for linea in file:
            datos = linea.split()
            letra = datos[0].strip()
            repeticiones[traductor[letra]] += 1

    res = [(letra, repeticiones[i]) for i , letra in enumerate(traductor.keys())]

    return res
