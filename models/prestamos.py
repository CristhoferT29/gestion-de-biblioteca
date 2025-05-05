# Definición de la clase Prestamo
class Prestamo:
    def __init__(self, id, libro, usuario):
        self.id = id
        self.libro = libro  # Instancia de la clase Libro
        self.usuario = usuario  # Instancia de la clase Usuario
    
    # Método para representar el préstamo como una cadena
    def __str__(self):
        return f"ID: {self.id}, Libro: {self.libro.titulo}, Usuario: {self.usuario.nombre}"
    
    # Método para obtener el id del préstamo
    def get_id(self):
        return self.id
    
    def to_dict(self):
        return {
            "id": self.id,
            "usuario": self.usuario,
            "libro": self.libro
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["usuario"],
            data["libro"]
        )
id = 0