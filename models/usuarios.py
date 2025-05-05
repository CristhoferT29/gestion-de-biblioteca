# Definición de la clase Usuario
class Usuario:
    modo_comparacion  = 'id'


    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    # Método para representar el usuario como una cadena
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}"
    
    # Método para obtener el id del usuario
    def get_id(self):
        return self.id
    
    def __lt__ (self, otro):
        #Método para comparar usuarios por su atributo modo_comparacion.
        # Se utiliza lower() y strip() para asegurar que la comparación sea insensible a mayúsculas y espacios en blanco.
        if( Usuario.modo_comparacion == 'nombre'):
            return self.nombre.lower().strip() < otro.nombre.lower().strip()
        elif( Usuario.modo_comparacion == 'id'):
            return self.id < otro.id
    
    def __eq__(self, otro):
        if( Usuario.modo_comparacion == 'nombre'):
            return self.nombre.strip().lower() == otro.nombre.strip().lower()
        elif( Usuario.modo_comparacion == 'id'):
            return self.id == otro.id
        
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["nombre"]
        )
id = 0
    