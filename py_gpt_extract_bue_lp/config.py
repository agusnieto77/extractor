# Configuración del modelo y mensajes
MODELO = "gpt-4o-mini"

# Configuración de mensajes
MESSAGES_CONFIG = {
    "system": {
        "role": "system",
        "content": (
            "Eres un asistente experto en extraer información estructurada de notas sobre entradas de barcos a puerto. "
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
            "Ejemplo de nota: {input_example}"
            "Texto de la nota: {input_text}"
        )
    }
}

EXAMPLES = """EJEMPLO 1: 
  input = 'Fecha de arribo: 4 de enero de 1880 | Pernambuco el 23 de Dbre berg gta portugues Gomez de Castro 147 tons cap Goncalvez à J Cibils con: 40 pip caña, 50 bcas azúcar moscavada 975 bcas 75 1[4 azúcar blanca.' 
  output = '{ "travel_departure_date": "1879-12-23", "travel_arrival_date": "1880-01-04", "travel_duration_value": null, "travel_duration_unit": null, "travel_arrival_moment": null, "travel_departure_port": "Pernambuco", "travel_port_of_call_list": [], "travel_arrival_port": "Buenos Aires", "ship_type": "berg gta", "ship_name": "Gomez de Castro", "ship_tons_capacity":  147, "ship_tons_units": " tons", "ship_flag": "portugues", "master_role": "cap", "master_name": "Goncalvez", "ship_agent_name": null, "crew_number": null, "cargo_list": [ { "cargo_merchant_name": "J Cibils", "cargo": [ { "cargo_quantity": 40, "cargo_unit": "pip", "cargo_commodity": "caña" }, { "cargo_quantity": 50, "cargo_unit": "bcas", "cargo_commodity": "azúcar moscavada" }, { "cargo_quantity": 975, "cargo_unit": "bcas", "cargo_commodity": "azúcar blanca" } ] } ], "passengers": null, "in_ballast": false, "quarantine": null, "forced_arrival": null, "obs": "75 1[4" }'
  EJEMPLO 2: 
  input = 'Fecha de arribo: 4 de enero de 1880 | Londres Amberes Rio Janeiro y Montevido vapor inglés Horrox 1101 tons cap Eddes á E, Norton con: á Bemberg C. 5 fds bsas 1 bto mtras; J Fulton 15 cj 5 casc provisiones; Parry 115 cj merc. J. Etchegaray 10 fds medias; Tramway Ciudad de Buenos Aires 25 casc herraduras; H. Peltzer 10 cj drogas; Puerto Ensenada 24 btos acero; Ferro C, del Sud 6 cj cristaleria; Moore C.12 cj perfumeria, Hape hnos 6 fds bolsas; Orden 230 cj hojalata 331 bto merc 51 cj id 9 id papel.' 
  output = '{ "travel_departure_date": null, "travel_arrival_date": "1880-01-05", "travel_duration_value": null, "travel_duration_unit": null, "travel_arrival_moment": null, "travel_departure_port": "Londres", "travel_port_of_call_list": [ { "port_of_call_place": "Amberes", "port_of_call_arrival_date": null, "port_of_call_departure_date": null }, { "port_of_call_place": " Rio Janeiro", "port_of_call_arrival_date": null, "port_of_call_departure_date": null }, { "port_of_call_place": " Montevideo", "port_of_call_arrival_date": null, "port_of_call_departure_date": null } ], "travel_arrival_port": "Buenos Aires", "ship_type": "vapor", "ship_name": "Horrox", "ship_tons_capacity": 1101, "ship_tons_units": "tons", "ship_flag": "inglés", "master_role": "cap", "master_name": "Eddes", "ship_agent_name": null, "crew_number": null, "cargo_list": [ { "cargo_merchant_name": "E. Norton", "cargo": [] }, { "cargo_merchant_name": "Bemberg C.", "cargo": [ { "cargo_quantity": 5, "cargo_unit": "fds", "cargo_commodity": "bsas" }, { "cargo_quantity": 1, "cargo_unit": "bto", "cargo_commodity": "mtras" } ] }, { "cargo_merchant_name": "J Fulton", "cargo": [ { "cargo_quantity": 15, "cargo_unit": "cj", "cargo_commodity": "provisiones" } ] }, { "cargo_merchant_name": "Parry", "cargo": [ { "cargo_quantity": 115, "cargo_unit": "cj", "cargo_commodity": "merc." } ] }, { "cargo_merchant_name": "J. Etchegaray", "cargo": [ { "cargo_quantity": 10, "cargo_unit": "fds", "cargo_commodity": "medias" } ] }, { "cargo_merchant_name": "Tramway Ciudad de Buenos Aires", "cargo": [ { "cargo_quantity": 25, "cargo_unit": "casc", "cargo_commodity": "herraduras" } ] }, { "cargo_merchant_name": "H. Peltzer", "cargo": [ { "cargo_quantity": 10, "cargo_unit": "cj", "cargo_commodity": "drogas" } ] }, { "cargo_merchant_name": "Puerto Ensenada", "cargo": [ { "cargo_quantity": 24, "cargo_unit": "btos", "cargo_commodity": "acero" } ] }, { "cargo_merchant_name": "Ferro C. del Sud", "cargo": [ { "cargo_quantity": 6, "cargo_unit": "cj", "cargo_commodity": "cristaleria" } ] }, { "cargo_merchant_name": "Moore C.", "cargo": [ { "cargo_quantity": 12, "cargo_unit": "cj", "cargo_commodity": "perfumeria" } ] }, { "cargo_merchant_name": "Hape hnos", "cargo": [ { "cargo_quantity": 6, "cargo_unit": "fds", "cargo_commodity": "bolsas" } ] }, { "cargo_merchant_name": "Orden", "cargo": [ { "cargo_quantity": 230, "cargo_unit": "cj", "cargo_commodity": "hojalata" }, { "cargo_quantity": 331, "cargo_unit": "bto", "cargo_commodity": "merc" }, { "cargo_quantity": 51, "cargo_unit": "cj", "cargo_commodity": "id" }, { "cargo_quantity": 9, "cargo_unit": "id", "cargo_commodity": "papel" } ] } ], "quarantine": null, "forced_arrival": null, "obs": "5 casc" }'"""

# Template del JSON actualizado
JSON_TEMPLATE = {
    'travel_departure_date': None,
    'travel_arrival_date': None,
    'travel_duration_value': None,
    'travel_duration_unit': None,
    'travel_arrival_moment': None,
    'travel_departure_port': None,
    'travel_port_of_call_list': [],
    'travel_arrival_port': None,
    'ship_type': None,
    'ship_name': None,
    'ship_tons_capacity': None,
    'ship_tons_units': None,
    'ship_flag': None,
    'master_role': None,
    'master_name': None,
    'ship_agent_name': None,
    'crew_number': None,
    'cargo_list': [],
    'passengers': None,
    'in_ballast': None,
    'quarantine': None,
    'forced_arrival': None,
    'obs': None
}

# Definiciones de campos actualizadas
FIELD_DEFINITIONS = {
    'travel_departure_date': 'La fecha en que el barco salió del puerto de origen. Siempre es la fecha más antigua. Muchas veces figura el mes y el día sin el año, se debe estimar el año en función de la fecha de llegada, si el mes de llegadas (diciembre) es mayor al mes de partida (septiembre) es el mismo año de la fecha de llegada, si el mes de llegada (febrero) es menor al de partida (noviembre), el año de la fecha de partida es 1 año menos que el año de llegada. Si dice "ayer" o "antes de ayer", calcular restando días a la fecha de llegada.',
    'travel_arrival_date': 'La fecha en que el barco llegó al puerto de destino [Buenos Aires].',
    'travel_duration_value': 'null',
    'travel_duration_unit': 'null',
    'travel_arrival_moment': 'null',
    'travel_departure_port': 'El nombre del puerto desde el cual salió el barco. Simpre es el primer puerto de salida, los siguientes puertos de salidas, si los hay, son puertos de escala.',
    'travel_port_of_call_list': 'Lista de objetos que describen los puertos (y opcionalmente más información como fechas de llegada o salida) en los que el barco hizo escala durante su trayecto al puerto de llegada.',
    'travel_arrival_port': 'Buenos Aires',
    'ship_type': 'El tipo de embarcación, e.g., bergantín, fragata, vapor.',
    'ship_name': 'El nombre propio del barco.',
    'ship_tons_capacity': 'El peso total o capacidad de carga del buque en toneladas.',
    'ship_tons_units': 'Especifica las unidades en las que está expresado las dimensiones del buque. Generalmente aparece en toneladas, pero puede aparecer también en quintales.',
    'ship_flag': 'El país o nacionalidad, puede ser un gentilicio, bajo cuya bandera navega el barco. Ejemplo: bergantín "francés", vapor "español", polacra "griega", bergantin goleta paquete "oriental"',
    'master_role': 'El cargo de la persona responsable a bordo, e.g., capitán, patrón.',
    'master_name': 'El nombre de la persona responsable a bordo.',
    'ship_agent_name': 'null',
    'crew_number': 'null',
    'cargo_list': 'Lista de objetos que describen las mercancías y sus dueños o destinatarios. Cada objeto en la lista debe seguir esta estructura (en este orden): {"cargo_merchant_name": "Nombre del consignatario", "cargo": [{"cargo_quantity": número, "cargo_unit": "unidad", "cargo_commodity": "tipo de mercancía"}]}. Es común que se utilice la palabra "idem" para referirse a la unidad o mercancía inmediatamente anterior, evitando la repetición. Puede ocurrir que tanto el valor de la clave "cargo_unit" como de la clave "cargo_commodity"sea idem. Ejemplo: "Coneh y Levy idem idem". Si el número de la carga (cargo_quantity) es ilegible o no está presente, debe asignarse un valor de 0 (ejemplo: "Coneh y Levy idem idem"). Ejemplo de texto aprocesar: "á Zimermmann y ca., 1 cajon mercancias, á Nicholson Green y ca., 29 cajones mercancias, 1 idem muestras, á Corach y Mora idem idem, 1 idem cristales". Ejemplo extracción de datos: [{"cargo_merchant_name": "Zimermmann y ca.", "cargo": [{"cargo_quantity": 1, "cargo_unit": "cajon", "cargo_commodity": "mercancias"}]}, {"cargo_merchant_name": "Nicholson Green y ca.", "cargo": [{"cargo_quantity": 29, "cargo_unit": "cajones", "cargo_commodity": "mercancias"}, {"cargo_quantity": 1, "cargo_unit": "idem", "cargo_commodity": "muestras"}]}, {"cargo_merchant_name": "Corach y Mora", "cargo": [{"cargo_quantity": 0, "cargo_unit": "idem", "cargo_commodity": "idem"}, {"cargo_quantity": 1, "cargo_unit": "idem", "cargo_commodity": "cristales"}]}]. Hay mercancías (cargo_commodity) que no explicitan unidades, por ejemplo "baldosas"; en estos caso en "cargo_unit" va null y en "cargo_commodity" va "baldosas".',
    'passengers': 'Representa la cantidad total de pasajeros.',
    'in_ballast': 'Define se se mencion que la embarcación está "en lastre" [True | False]',
    'quarantine': 'Información relativa a la existencia de condiciones especiales de la llegada motivadas por circunstancias sanitarias que imponen la cuarentena.',
    'forced_arrival': 'Información sobre la llegada al puerto debido a causas imprevistas, como un arribo forzoso por temporal, avería u otras emergencias.',
    'obs': 'Notas o comentarios adicionales que aborden aspectos no contemplados en las variables registradas, proporcionando información contextual o relevante sobre el evento.'
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
        "travel_departure_date": {
          "type": "string",
          "description": "Fecha de salida del puerto en formato YYYY-MM-DD.",
          "nullable": True
        },
        "travel_arrival_date": {
          "type": "string",
          "description": "Fecha de llegada al puerto en formato YYYY-MM-DD.",
          "nullable": True
        },
        "travel_duration_value": {
          "type": "string",
          "description": "null",
          "nullable": True
        },
        "travel_duration_unit": {
          "type": "string",
          "description": "null",
          "nullable": True
        },
        "travel_arrival_moment": {
          "type": "string",
          "description": "null",
          "nullable": True
        },
        "travel_departure_port": {
          "type": "string",
          "description": "Puerto desde el cual salió el barco.",
          "nullable": True
        },
        "travel_port_of_call_list": {
          "type": "array",
          "description": "Lista de puertos donde el barco hizo escala.",
          "nullable": True,
          "items": {
            "type": "object",
            "properties": {
              "port_of_call_place": {
                "type": "string",
                "description": "Puerto donde hizo la escala.",
                "nullable": True
              },
              "port_of_call_arrival_date": {
                "type": "string",
                "description": "Fecha de llegada al puerto de escala.",
                "nullable": True
              },
              "port_of_call_departure_date": {
                "type": "string",
                "description": "null",
                "nullable": True
              },
            },
            "required": ["port_of_call_place", "port_of_call_arrival_date", "port_of_call_departure_date"],
            "additionalProperties": False
          },
        },
        "travel_arrival_port": {
          "type": "string",
          "description": "Buenos Aires",
          "nullable": True
        },
        "ship_type": {
          "type": "string",
          "description": "Tipo de embarcación.",
          "nullable": True
        },
        "ship_name": {
          "type": "string",
          "description": "Nombre del barco.",
          "nullable": True
        },
        "ship_tons_capacity": {
          "type": "number",
          "description": "Capacidad de carga del buque en toneladas.",
          "nullable": True
        },
        "ship_tons_units": {
          "type": "string",
          "description": "Especifica las unidades en las que está expresado las dimensiones del buque",
          "nullable": True
        },
        "ship_flag": {
          "type": "string",
          "description": "País o nacionalidad bajo cuya bandera navega el barco. Ejemplo: 'oriental'",
          "nullable": True
        },
        "master_role": {
          "type": "string",
          "description": "Cargo del responsable a bordo.",
          "nullable": True
        },
        "master_name": {
          "type": "string",
          "description": "Nombre del responsable a bordo.",
          "nullable": True
        },
        "ship_agent_name": {
          "type": "string",
          "description": "null",
          "nullable": True
        },
        "crew_number": {
          "type": "string",
          "description": "null",
          "nullable": True
        },
        "cargo_list": {
          "type": "array",
          "description": "Lista de mercancías transportadas y sus propietarios.",
          "nullable": True,
          "items": {
            "type": "object",
            "properties": {
              "cargo_merchant_name": {
                "type": "string",
                "description": "Es el propietario de la carga o aquella persona a quien dicha carga va destinada.",
                "nullable": True
              },
              "cargo": {
                "type": "array",
                "description": "Lista de mercancías transportadas.",
                "nullable": True,
                "items": {
                  "type": "object",
                  "properties": {
                    "cargo_quantity": {
                      "type": "number",
                      "description": "Representa la cantidad total de la carga en forma numérica. Si el número es ilegible o no está presente, debe asignarse un valor de 0.",
                      "nullable": True
                    },
                    "cargo_unit": {
                      "type": "string",
                      "description": "Expresa las unidades en las que la carga aparece. Ejemplo: 'cargo_unit': 'cajones', 'cargo_unit': 'idem'",
                      "nullable": True
                    },
                    "cargo_commodity": {
                      "type": "string",
                      "description": "Expresa los distintos productos o tipos de mercancías que transporta el buque. Ejemplo: 'cargo_commodity': 'cristales', 'cargo_unit': 'idem'",
                      "nullable": True
                    }
                  },
                  "required": ["cargo_quantity", "cargo_unit", "cargo_commodity"],
                  "additionalProperties": False
                }
              }
            },
            "required": ["cargo_merchant_name", "cargo"],
            "additionalProperties": False
          }
        },
        "passengers": {
          "type": "number",
          "description": "Representa la cantidad total de pasajeros.",
          "nullable": True
        },
        "in_ballast": {
          "type": "boolean",
          "description": "Define se se mencion que la embarcación está 'en lastre' [True | False]",
          "nullable": True
        },
        "quarantine": {
          "type": "string",
          "description": "Información relativa a la existencia de condiciones especiales de la llegada motivadas por circunstancias sanitarias que imponen la cuarentena.",
          "nullable": True
        },
        "forced_arrival": {
          "type": "string",
          "description": "Información sobre la llegada al puerto debido a causas imprevistas, como un arribo forzoso por temporal, avería u otras emergencias.",
          "nullable": True
        },
        "obs": {
          "type": "string",
          "description": "Notas o comentarios adicionales que aborden aspectos no contemplados en las variables registradas, proporcionando información contextual o relevante sobre el evento.",
          "nullable": True
        }
      },
      "required": [
        "travel_departure_date", 
        "travel_arrival_date",
        "travel_duration_value", 
        "travel_duration_unit",
        "travel_arrival_moment",
        "travel_departure_port", 
        "travel_port_of_call_list", 
        "travel_arrival_port",
        "ship_type", 
        "ship_name", 
        "ship_tons_capacity", 
        "ship_tons_units",
        "ship_flag",
        "master_role", 
        "master_name", 
        "ship_agent_name",
        "crew_number",
        "cargo_list",
        "passengers",
        "in_ballast",
        "quarantine",
        "forced_arrival",
        "obs"
      ],
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
