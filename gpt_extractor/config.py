# Configuración del modelo y mensajes
MODELO = "gpt-4o-mini"

# Configuración de mensajes
MESSAGES_CONFIG = {
    "system": {
        "role": "system",
        "content": (
            "Eres un asistente experto en extraer información estructurada de notas sobre la entrada de barcos a puerto. "
            "Debes responder EXCLUSIVAMENTE con un objeto JSON válido que contenga los campos solicitados. "
            "Si no encuentras información para algún campo, debes responder con el valor null en ese campo."
        )
    },
    "template": {
        "role": "user",
        "content": (
            "Extrae la siguiente información del evento de entrada de barco descrito en la nota, "
            "utilizando el formato JSON exacto: {json_template}. "
            "Aquí está la definición de cada clave: {field_definitions} "
            "Texto de la nota: {input_text}"
        )
    }
}

# Template del JSON y definiciones de campos
JSON_TEMPLATE = {
    'Fecha de salida': None,
    'Duración del viaje': None,
    'Fecha de llegada': None,
    'Puerto de salida': None,
    'Escalas en los puertos de la ruta': None,
    'Puerto de destino': None,
    'Tipo de buque': None,
    'Nombre del buque': None,
    'Tonelaje del buque': None,
    'Pabellón del buque': None,
    'Cargo o función del responsable': None,
    'Nombre del responsable': None,
    'Mercancías transportadas': None
}

FIELD_DEFINITIONS = {
    'Fecha de salida': 'La fecha en que el barco salió del puerto de origen. Muchas veces figura el mes y el día sin el año, se debe estimar el año en función de la fecha de llegada, si el mes de llegadas (diciembre) es mayor al mes de partida (septiembre) es el mismo año de la fecha de llegada, si el mes de llegada (febrero) es menor al de partida (noviembre), el año de la fecha de partida es 1 año menos que el año de llegada.',
    'Duración del viaje': 'Duración estimada del viaje en días. Si está la fecha de salida y la fecha de llegada, calcular los días transcurridos.',
    'Fecha de llegada': 'La fecha en que el barco llegó al puerto de destino.',
    'Puerto de salida': 'El nombre del puerto desde el cual salió el barco.',
    'Escalas en los puertos de la ruta': 'Lista de los puertos donde hizo escala el barco antes de llegar a destino.',
    'Puerto de destino': 'El nombre del puerto donde arribó el barco.',
    'Tipo de buque': 'El tipo de embarcación, e.g., bergantín, fragata, vapor.',
    'Nombre del buque': 'El nombre propio del barco.',
    'Tonelaje del buque': 'El peso total o capacidad de carga del buque en toneladas.',
    'Pabellón del buque': 'El país bajo cuya bandera navega el barco.',
    'Cargo o función del responsable': 'El cargo de la persona responsable a bordo, e.g., capitán, patrón.',
    'Nombre del responsable': 'El nombre de la persona responsable a bordo.',
    'Mercancías transportadas': 'Descripción de las mercancías (y sus consignatarios, sus nombres) transportadas por el barco. En general las mercancías están consignadas a nombre de alguien. Ejemplo de inicio de la descripción de las mercancías: , á Lohmann Meyn y ca., á J. P. Villanueva 6 cajones cristales, á R. Hoppmann 11 idem ...'
}

# Configuración del schema JSON
JSON_SCHEMA = {
    "type": "json_schema",
    "json_schema": {
        "name": "ship_entry",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "Fecha de salida": {
                    "type": "string",
                    "description": "Fecha de salida del puerto en formato YYYY-MM-DD.",
                    "nullable": True
                },
                "Duración del viaje": {
                    "type": "string",
                    "description": "Duración estimada del viaje.",
                    "nullable": True
                },
                "Fecha de llegada": {
                    "type": "string",
                    "description": "Fecha de llegada al puerto en formato YYYY-MM-DD.",
                    "nullable": True
                },
                "Puerto de salida": {
                    "type": "string",
                    "description": "Puerto desde el cual salió el barco.",
                    "nullable": True
                },
                "Escalas en los puertos de la ruta": {
                    "type": "string",
                    "description": "Puertos donde el barco hizo escala.",
                    "nullable": True
                },
                "Puerto de destino": {
                    "type": "string",
                    "description": "Puerto donde arribó el barco.",
                    "nullable": True
                },
                "Tipo de buque": {
                    "type": "string",
                    "description": "Tipo de embarcación.",
                    "nullable": True
                },
                "Nombre del buque": {
                    "type": "string",
                    "description": "Nombre del barco.",
                    "nullable": True
                },
                "Tonelaje del buque": {
                    "type": "number",
                    "description": "Capacidad de carga del buque en toneladas.",
                    "nullable": True
                },
                "Pabellón del buque": {
                    "type": "string",
                    "description": "País bajo cuya bandera navega el barco.",
                    "nullable": True
                },
                "Cargo o función del responsable": {
                    "type": "string",
                    "description": "Cargo del responsable a bordo.",
                    "nullable": True
                },
                "Nombre del responsable": {
                    "type": "string",
                    "description": "Nombre del responsable a bordo.",
                    "nullable": True
                },
                "Mercancías transportadas": {
                    "type": "string",
                    "description": "Descripción de las mercancías transportadas.",
                    "nullable": True
                }
            },
            "required": ["Fecha de salida", "Duración del viaje", "Fecha de llegada", "Puerto de salida", 
                        "Escalas en los puertos de la ruta", "Puerto de destino", "Tipo de buque", 
                        "Nombre del buque", "Tonelaje del buque", "Pabellón del buque", 
                        "Cargo o función del responsable", "Nombre del responsable", "Mercancías transportadas"],
            "additionalProperties": False
        }
    }
}

# Configuración del modelo
MODEL_CONFIG = {
    "temperature": 0,
    "max_tokens": 4000,
    "top_p": 0,
    "frequency_penalty": 0,
    "presence_penalty": 0
}
