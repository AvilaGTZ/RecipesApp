import openpyxl
from openpyxl import *
import os

def Lista_a_Texto(Lista_con_textos, Tipo):
    
    Texto_formado = ""
    
    for Texto in Lista_con_textos:
        
        if Tipo == "Instrucciones":
            Texto_formado = Texto_formado + Texto['step'] + "\n"
        
        elif Tipo == "Ingredientes":
            Texto_formado = Texto_formado + Texto['originalString'] + "\n"
    
    return Texto_formado

    
def Generar_recetario_excel(Recetas_modeladas, Nombre_recetario):
    print("Generando el recetario: " + Nombre_recetario)
    
    Estilo_titulo       = 'B3'
    Estilo_Porciones    = 'C3'
    Estilo_saludable    = 'D3'
    Estilo_tiempo       = 'E3'
    Estilo_imagen       = 'F3'
    Estilo_ingredientes = 'G3'
    Estilo_preparacion  = 'H3'
    Estilo_url          = 'I3'
    
    Columna_titulo       = 'B'
    Columna_Porciones    = 'C'
    Columna_saludable    = 'D'
    Columna_tiempo       = 'E'
    Columna_imagen       = 'F'
    Columna_ingredientes = 'G'
    Columna_preparacion  = 'H'
    Columna_url          = 'I'
    
    Renglon_escritura      = 3
    
    try:
        #Abrimos la plantilla de excel
        Libro_Excel = openpyxl.load_workbook("PlantillaRecetario.xlsx")
        
        #Seleccionamos la hoja de calculo con la que deseamos trabajar
        Hoja_recetario = Libro_Excel["Recetario"]
        
        Mensaje_Status = "OK"
        
        for Receta in Recetas_modeladas:
            
            #Obtenemos las celdas de donde sacaremos los estilos
            Celda_titulo_estilo        = Hoja_recetario[Estilo_titulo]
            Celda_Porciones_estilo     = Hoja_recetario[Estilo_Porciones]
            Celda_saludable_estilo     = Hoja_recetario[Estilo_saludable]
            Celda_tiempo_estilo        = Hoja_recetario[Estilo_tiempo]
            Celda_imagen_estilo        = Hoja_recetario[Estilo_imagen]
            Celda_ingredientes_estilo  = Hoja_recetario[Estilo_ingredientes]
            Celda_preparacion_estilo   = Hoja_recetario[Estilo_preparacion]
            Celda_url_estilo           = Hoja_recetario[Estilo_url]
            
            #Generamos las coordenadas de las celdas que nos interesa modificar
            Celda_titulo       = Columna_titulo       + str(Renglon_escritura)
            Celda_Porciones    = Columna_Porciones    + str(Renglon_escritura)
            Celda_saludable    = Columna_saludable    + str(Renglon_escritura)
            Celda_tiempo       = Columna_tiempo       + str(Renglon_escritura)
            Celda_imagen       = Columna_imagen       + str(Renglon_escritura)
            Celda_ingredientes = Columna_ingredientes + str(Renglon_escritura)
            Celda_preparacion  = Columna_preparacion  + str(Renglon_escritura)
            Celda_url          = Columna_url          + str(Renglon_escritura)
            
            #Obtenemos las celdas que queremos modificar en base a las coordenadas
            #calculadas previamente
            Celda_titulo_modificable       = Hoja_recetario[Celda_titulo]
            Celda_Porciones_modificable    = Hoja_recetario[Celda_Porciones]
            Celda_saludable_modificable    = Hoja_recetario[Celda_saludable]
            Celda_tiempo_modificable       = Hoja_recetario[Celda_tiempo]
            Celda_imagen_modificable       = Hoja_recetario[Celda_imagen]
            Celda_ingredientes_modificable = Hoja_recetario[Celda_ingredientes]
            Celda_preparacion_modificable  = Hoja_recetario[Celda_preparacion]
            Celda_url_modificable          = Hoja_recetario[Celda_url]
            
            #Agregamos los estilos copiandolos de las celdas originales a 
            #las celdas que modificaremos.
            Celda_titulo_modificable._style       = Celda_titulo_estilo._style
            Celda_Porciones_modificable._style    = Celda_Porciones_estilo._style
            Celda_saludable_modificable._style    = Celda_saludable_estilo._style
            Celda_tiempo_modificable._style       = Celda_tiempo_estilo._style
            Celda_imagen_modificable._style       = Celda_imagen_estilo._style
            Celda_ingredientes_modificable._style = Celda_ingredientes_estilo._style
            Celda_preparacion_modificable._style  = Celda_preparacion_estilo._style
            Celda_url_modificable._style          = Celda_url_estilo._style
            
            #Agregamos la informacion de la receta hacia las celdas en excel
            Celda_titulo_modificable.value       = Receta.Titulo
            Celda_Porciones_modificable.value    = Receta.Porciones
            Celda_saludable_modificable.value    = str(Receta.NivelSludable)     + " /100"
            Celda_tiempo_modificable.value       = str(Receta.TiempoPreparacion) + " mins"
            
            img = openpyxl.drawing.image.Image(Receta.NombreImagen)
            img.anchor = Celda_imagen # Or whatever cell location you want to use.
            Hoja_recetario.add_image(img)
            Celda_url_modificable.value = Receta.Imagen
                 
            #Ya que los ingredientes y las instrucciones son listas,
            #Se necesitan convertir a una sola cadena de texto para 
            #Poder vaciarla a la celda de excel.
            
            Ingredientes_texto  = Lista_a_Texto(Receta.Ingredientes, "Ingredientes")
            Instrucciones_texto = Lista_a_Texto(Receta.Instrucciones, "Instrucciones")
            
            Celda_ingredientes_modificable.value = Ingredientes_texto
            Celda_preparacion_modificable.value  = Instrucciones_texto
            
            Renglon_escritura = Renglon_escritura + 1
            
        
        Libro_Excel.save(Nombre_recetario + ".xlsx")
        for Receta in Recetas_modeladas:
            os.remove(Receta.NombreImagen)
        return Mensaje_Status
    
    except Exception as e:
        Mensaje_Status = "ERR: Error al generar el recetario en excel"
        print(str(e))
        return Mensaje_Status
        
        
        
    

