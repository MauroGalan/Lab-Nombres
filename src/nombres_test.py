from nombres import leer_frecuencias_nombres,filtrar_por_genero,calcular_nombres,calcular_top_nombres_de_año,calcular_nombres_ambos_generos,\
    calcular_nombres_compuestos,calcular_frecuencia_media_nombre_años,calcular_nombre_mas_frecuente_año_genero,\
    calcular_año_mas_frecuencia_nombre,calcular_nombres_mas_frecuentes

if __name__ == "__main__":
    #print(f"Los nacimientos masculinos son: {filtrar_por_genero(leer_frecuencias_nombres("data/frecuencias_nombres.csv"),"Hombre")}")
    #print(f"Los nombre femeninos son: {calcular_nombres(leer_frecuencias_nombres("data/frecuencias_nombres.csv"),"Mujer")}")
    #print(f"Los nombre son: {calcular_nombres(leer_frecuencias_nombres("data/frecuencias_nombres.csv"),None)}")
    #print(f"Los nombres usados para ambos géneros son: {calcular_nombres_ambos_generos(leer_frecuencias_nombres("data/frecuencias_nombres.csv"))}")
    #print(f"Los nombres compuestos son: {calcular_nombres_compuestos(leer_frecuencias_nombres("data/frecuencias_nombres.csv"),None)}")
    #print(f"Los nombres compuestos de mujer son: {calcular_nombres_compuestos(leer_frecuencias_nombres("data/frecuencias_nombres.csv"),"Mujer")}")
    #print(f"La media de nacimientos llamados Nerea entre 2005 y 2010 es: {calcular_frecuencia_media_nombre_años(leer_frecuencias_nombres("data/frecuencias_nombres.csv"),"NEREA",2005,2010)}")
    #print(f"(ERROR INTENCIONADO) La media de nacimientos llamados Gonzalo entre 2000 y 2015 es: {calcular_frecuencia_media_nombre_años(leer_frecuencias_nombres("data/frecuencias_nombres.csv"),"GONZALO",2015,2000)}")
    #print(f"El nombre de mujer más frecuente de 2017 es {calcular_nombre_mas_frecuente_año_genero(leer_frecuencias_nombres("data/frecuencias_nombres.csv"),2017,"Mujer")}")
    #print(f"El nombre VERA es más frecuente en el año {calcular_año_mas_frecuencia_nombre(leer_frecuencias_nombres("data/frecuencias_nombres.csv"),"VERA")}")
    #print(f"Los nombres de hombre más frecuentes en la década del 2000 son {calcular_nombres_mas_frecuentes(leer_frecuencias_nombres("data/frecuencias_nombres.csv"),"Hombre",2000,3)}")
    #print(f"Los nombres de mujer más frecuentes en la década de 2010 son {calcular_nombres_mas_frecuentes(leer_frecuencias_nombres("data/frecuencias_nombres.csv"),"Mujer",2010,None)}")
    #print(f"Los 10 nombres más frecuntes en 2008 son: {calcular_top_nombres_de_año(leer_frecuencias_nombres("data/frecuencias_nombres.csv"), 2008, None, None)}")