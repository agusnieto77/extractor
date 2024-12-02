from config import FIELD_DEFINITIONS, MESSAGES_CONFIG, JSON_TEMPLATE, EXAMPLES

def create_messages(texto_entrada):
    """
    Crea la lista de mensajes para la API de OpenAI
    """
    # Formateamos las definiciones de campos como texto
    field_definitions_text = '. '.join([
        f"'{key}': '{value}'" 
        for key, value in FIELD_DEFINITIONS.items()
    ])

    # Creamos el mensaje del usuario con el template
    user_message = MESSAGES_CONFIG["template"]["content"].format(
        json_template=JSON_TEMPLATE,
        field_definitions=field_definitions_text,
        input_example=EXAMPLES,
        input_text=texto_entrada
    )

    # Retornamos la lista completa de mensajes
    return [
        MESSAGES_CONFIG["system"],
        {"role": "user", "content": user_message}
    ]

def leer_archivo(nombre_archivo):
    """
    Lee el contenido de un archivo de texto
    Args:
        nombre_archivo (str): Ruta al archivo a leer
    Returns:
        str: Contenido del archivo o None si hay error
    """
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except Exception as e:
        print(f"Error al leer el archivo {nombre_archivo}: {str(e)}")
        return None
