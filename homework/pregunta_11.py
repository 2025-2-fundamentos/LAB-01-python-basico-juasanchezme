"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    with open("files/input/data.csv", "r") as file:      #?Abrir el archivo en lectura (r)
            lineas = file.readlines()                    #? Leer las líneas y guardarlas en la lista 'lineas'

    suma_por_letra = {}                                  #? Crear un diccionario vacío para almacenar la suma por letra

    for linea in lineas:                                #? Iterar sobre cada línea del archivo
        partes = linea.strip().split("\t")               #? Eliminar saltos de línea y dividir la línea por tabulaciones   
        columna_2 = int(partes[1])                      #?#? Obtener el valor de la columna 2 (convertir a entero)           
        columna_4 = partes[3].split(",")                #? Obtener los elementos de la columna 4 y dividirlos por comas

        for letra in columna_4:                         #? Iterar sobre cada letra en la columna 4
            if letra not in suma_por_letra:             #? Si la letra no está en el diccionario
                suma_por_letra[letra] = 0               #? Inicializar el contador de esa letra en 0
            suma_por_letra[letra] += columna_2          #? Sumar el valor de la columna 2 a la letra correspondiente

    return dict(sorted(suma_por_letra.items()))
print(pregunta_11())

