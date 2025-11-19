"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    with open("files/input/data.csv", "r") as file:                 #? abrir el archivo en lectura (r)
        lineas = file.readlines()                                   #?leer las lineas y guardarlas en la lista lineas
    valores = {}                                                    #?diccionario 
    for linea in lineas:
        partes = linea.strip().split("\t")                          #?elimina saltos de linea y divide las tabulaciones  
        columna5 = partes[4].split(",")                             #?accede a la columna 5 que contiene pares clave:valor y separa con coma cada pareja clave-valor

        for item in columna5:                                       
            clave, valor = item.split(":")                          #?se separa cada item por :
            valor = int(valor)

            if clave in valores:
                valores[clave].append(valor)                        #?verificar si esta en el diccionario, si esta se agrega el nuevo valor, sino se crea una lista con ese valor
            else:
                valores[clave] = [valor]
        
    resultado = []                                                  #?se crea la lista vacia para el calculo de los mminimos y maximos     
    for clave in sorted(valores.keys()):                            #?claves ordenadas alfabeticcamente con sorted()
        valor_maximo = max(valores[clave])
        valor_minimo = min(valores[clave])
        resultado.append((clave, valor_minimo, valor_maximo))       #?Se agrega la tupla (clave, valor_mínimo, valor_máximo) a la lista resultado.
    return resultado

print(pregunta_06())
