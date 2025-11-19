"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    with open("files/input/data.csv", "r") as file:      #? Abrir el archivo en lectura (r)
            lineas = file.readlines()                    #? Leer las líneas y guardarlas en la lista 'lineas'

    counter = {}                                     #?#? Crear un diccionario vacío para contar las ocurrencias de cada clave

    for linea in lineas:
        partes = linea.strip().split("\t")           #? Eliminar saltos de línea y dividir por tabulaciones
        columna_5 = partes[4]                        #? Obtener la columna 5 (que contiene las claves y valores)
        pares = columna_5.split(",")                 #? Separar las parejas clave:valor por coma

        for par in pares:                            #? Iterar sobre cada pareja clave:valor
            clave, _ = par.split(":")                #! Separar la clave del valor (no necesitamos el valor, así que lo ignoramos con '_')
            if clave not in counter:                 #? Si la clave no está en el diccionario
                counter[clave] = 0                   #? Inicializar su contador en 0
            counter[clave] += 1                      #? Incrementar el contador de la clave

    return dict(sorted(counter.items()))
print(pregunta_09())

