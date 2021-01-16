import requests
from PIL import Image

#'title'                                  Titulo de la receta
#'servings'                               Numero de porciones
#'readyInMinutes'                         Tiempo de preparacion
#'healthScore'                            Que tan saludable es
#'image'                                  Imagen de la receta
#'extendedIngredients'[x]'originalString' Ingredientes de la receta
#'analyzedInstructions'[x]step            Pasos de preparacion

class Receta_modelo():
    def __init__(self):
        self.Titulo            = ""
        self.Porciones         = ""
        self.TiempoPreparacion = ""
        self.NivelSludable     = ""
        self.Imagen            = ""
        self.NombreImagen      = ""
        self.Ingredientes      = []
        self.Instrucciones     = []
        self.OriginalUrl       = ""
        
def Obtener_Imagen_Receta(URL):
    Nombre_imagen = URL.split("/")[-1]
    img_data = requests.get(URL).content
    with open(Nombre_imagen, 'wb') as handler:
        handler.write(img_data)
    
    image = Image.open(Nombre_imagen)
    image_mod = image.resize((150,150))
    image.close()
    image_mod.save(Nombre_imagen)
    return Nombre_imagen
    
        
        
def Genera_Modelo_Recetas(Lista_Recetas):
    
    Lista_recetas_modelada = []
    
    Receta_para_modelar  = Receta_modelo()
    Mensaje_Status = "OK"
    
    
    for Receta in Lista_Recetas:
        try:
            Receta_para_modelar.Titulo            = Receta['title']
            Receta_para_modelar.Porciones         = Receta['servings']
            Receta_para_modelar.NivelSludable     = Receta['healthScore']
            Receta_para_modelar.TiempoPreparacion = Receta['readyInMinutes']
            
            Receta_para_modelar.Imagen            = Receta['image']
            Nombre_imagen = Obtener_Imagen_Receta(Receta_para_modelar.Imagen)
            Receta_para_modelar.NombreImagen = Nombre_imagen
            
            Receta_para_modelar.Ingredientes      = Receta['extendedIngredients']
            Receta_para_modelar.Instrucciones     = Receta['analyzedInstructions'][0]['steps']
            Receta_para_modelar.OriginalUrl       = Receta['sourceUrl']
            
            Lista_recetas_modelada.append(Receta_para_modelar)
            Receta_para_modelar = Receta_modelo()
        except:
            pass
        
    return Mensaje_Status, Lista_recetas_modelada
    
        
        
        
        
        
        
