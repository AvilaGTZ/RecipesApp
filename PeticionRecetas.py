import requests
import json

def Obtener_recetas(Numero_de_recetas):
    Lista_de_recetas = []
    APIKey = "b0bbda75fd6c415982ca2cd885d0deb8"
    Params = {'apiKey':APIKey, 'number':Numero_de_recetas}
    RecipesURL = "https://api.spoonacular.com/recipes/random"
    
    Receta_aleatoria    = requests.get(RecipesURL, params=Params)
    if Receta_aleatoria.status_code == 200:
        Informacion_receta_sin_formato = Receta_aleatoria.content
        Informacion_receta_con_formato  = json.loads(Informacion_receta_sin_formato)
        Informacion_relevante_recetas   = Informacion_receta_con_formato['recipes']
        for Receta in Informacion_relevante_recetas:
            Lista_de_recetas.append(Receta)
        return Lista_de_recetas
    
    