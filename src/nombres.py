import csv
from collections import namedtuple
FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'año,nombre,frecuencia,genero')
def leer_frecuencias_nombres(ruta):
    listafrecuencia = []
    with open (ruta, encoding="utf-8")  as f:
        lector = csv.reader(f)
        next(lector)
        for año,nombre,frecuencia,genero in lector:
            año = int(año)
            frecuencia = int(frecuencia)
            listafrecuencia.append(FrecuenciaNombre(año,nombre,frecuencia,genero))
        return listafrecuencia
    
def filtrar_por_genero(lista, genero): 
    """
    Recibe una lista de tuplas de tipo FrecuenciaNombre y un género de tipo str, 
    y devuelve una lista de tuplas de tipo FrecuenciaNombre 
    con los registros del género recibido como parámetro.
    """
    lista_filtrada = []
    for nacimiento in lista:
        if nacimiento.genero == genero:
            lista_filtrada.append(nacimiento)
    return lista_filtrada


def calcular_nombres(lista,genero): 
    """
    Recibe una lista de tuplas de tipo FrecuenciaNombre y un género de tipo str, 
    y devuelve un conjunto {str} con los nombres del género recibido como parámetro. 
    El género puede ser 'Hombre', 'Mujer' o tener un valor None, 
    en cuyo caso se incluyen en el conjunto todos los nombres. 
    El valor por defecto del género es None.
    """
    conjunto_filtrado = set()
    for nacimiento in lista:
        if genero == None or nacimiento.genero == genero:
            conjunto_filtrado.add(nacimiento.nombre)
    return conjunto_filtrado

def calcular_nombres_ambos_generos(lista): 
    """
    Recibe una lista de tuplas de tipo FrecuenciaNombre, y devuelve un conjunto {str} 
    con los nombres que han sido utilizados en ambos géneros.
    """
    chicos = calcular_nombres(lista,"Hombre")
    chicas = calcular_nombres(lista,"Mujer")
    return chicos&chicas

def calcular_nombres_compuestos(lista,genero): 
    """
    recibe una lista de tuplas de tipo FrecuenciaNombre y un género de tipo str, 
    y devuelve un conjunto {str} con los nombres que contienen más de una palabra. 
    El género puede ser 'Hombre', 'Mujer' o tener un valor None, en cuyo caso 
    se incluyen en el conjunto todos los nombres. El valor por defecto del género es None.
    """
    conjunto_compuestos = set()
    for nacimiento in lista:
        if genero == None or nacimiento.genero == genero:
            if " " in nacimiento.nombre:
                conjunto_compuestos.add(nacimiento.nombre)
    return conjunto_compuestos

def calcular_frecuencia_media_nombre_años(lista,nombre,año_i,año_f): 
    """
    Recibe una lista de tuplas de tipo FrecuenciaNombre, un nombre, un año inicial 
    y un año final y calcula la frecuencia media del nombre dado como parámetro 
    en el rango de años [año_inicial, año_final) formado por el año inicial y el año final dados como parámetro. 
    Si no se puede calcular la media devuelve 0.
    """
    frecuencia_t = 0
    for nacimiento in lista:
        if nacimiento.nombre == nombre and nacimiento.año >= año_i and nacimiento.año < año_f:
            frecuencia_t += nacimiento.frecuencia
    if (año_f-año_i)<1:
        return 0
    else:
        return frecuencia_t/((año_f)-(año_i))

def calcular_nombre_mas_frecuente_año_genero(lista,año,genero): 
    """
    Recibe una lista de tuplas de tipo FrecuenciaNombre, un año y un género 
    y devuelve el nombre más frecuente en el año dado como parámetro del género dado como parámetro.
    """
    max = None
    for nacimiento in lista:
        if nacimiento.genero == genero and nacimiento.año == año and (max == None or max.frecuencia < nacimiento.frecuencia):
            max = nacimiento
    return max.nombre

def calcular_año_mas_frecuencia_nombre(lista,nombre): 
    """
    Recibe una lista de tuplas de tipo FrecuenciaNombre y un nombre 
    y devuelve el año con mayor frecuencia del nombre dado como parámetro.
    """
    max = None
    for nacimiento in lista:
        if nacimiento.nombre == nombre and (max == None or max.frecuencia < nacimiento.frecuencia):
                max = nacimiento
    return max.año

def calcular_nombres_mas_frecuentes(lista,genero,decada,n): 
    """
    Recibe una lsta de tuplas de tipo FrecuenciaNombre, un género, un entero que reresenta una década 
    y un número n y devuelve una lista con los n nombres más frecuentes, de mayor a menor frecuencia, 
    del un género dado en la década dada. Por defecto, debe devolver los 5 más frecuentes. 
    La década se da con cuatro dígitos: 1960, 1970..
    """
    nombres_frecuentes = []
    if n == None:
        n = 5
    while len(nombres_frecuentes) < n:
        max = None
        for nacimiento in lista:
            if nacimiento.genero == genero and nacimiento.año >= decada and nacimiento.año < decada+10 and nacimiento.nombre not in nombres_frecuentes and\
                (max == None or max.frecuencia < nacimiento.frecuencia):
                max = nacimiento
        nombres_frecuentes.append(max.nombre)
    return nombres_frecuentes

