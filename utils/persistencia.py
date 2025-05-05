import json

def guardar_json(archivo, lista_objetos):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump([obj.to_dict() for obj in lista_objetos], f, indent=4, ensure_ascii=False)

def cargar_json(archivo, clase):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [clase.from_dict(elemento) for elemento in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON: {archivo}. Asegúrate de que el formato sea correcto.")
        return []
