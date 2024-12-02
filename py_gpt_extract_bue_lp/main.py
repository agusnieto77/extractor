from extractor import ShipInfoExtractor
from utils import leer_archivo
import json
import os

def main():
    # Verificar que existe la API key
    if not os.environ.get("OPENAI_API_KEY"):
        print("Error: No se encontró la API key de OpenAI en las variables de entorno")
        return
    
    # Crear instancia del extractor
    extractor = ShipInfoExtractor()
    
    # Leer el archivo de texto
    texto = leer_archivo(nombre_archivo)
    
    if texto is None:
        return
    
    # Extraer información
    resultado = extractor.extraer_informacion(texto)
    
    # Imprimir resultado
    if resultado:
        print(json.dumps(resultado, indent=2, ensure_ascii=False))
    else:
        print("No se pudo procesar la nota")

if __name__ == "__main__":
    nombre_archivo = '../txts/bue_lp_01.txt'
    main()
