# Definición de la clase Libro
class Libro:
    modo_comparacion  = 'id'
    def __init__(self, id, titulo, isbn, autor, aniopublicacion):
        self.id = id
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor
        self.aniopublicacion = aniopublicacion
    
    # Método para representar el libro como una cadena
    def __str__(self):
        return f"ID: {self.id}, Título: {self.titulo}, ISBN: {self.isbn}, Autor: {self.autor}, Año de Publicación: {self.aniopublicacion}"
    
    def __lt__ (self, otro):
        #Método para comparar libros por su título.
        # Se utiliza lower() y strip() para asegurar que la comparación sea insensible a mayúsculas y espacios en blanco.
        if( Libro.modo_comparacion == 'titulo'):
            return self.titulo.lower().strip() < otro.titulo.lower().strip()
        elif( Libro.modo_comparacion == 'id'):
            return self.id < otro.id
        elif( Libro.modo_comparacion == 'isbn'):
            return self.isbn < otro.isbn
        elif( Libro.modo_comparacion == 'autor'):
            return self.autor.lower().strip() < otro.autor.lower().strip()
        elif( Libro.modo_comparacion == 'aniopublicacion'):
            return self.aniopublicacion < otro.aniopublicacion
    
    def __eq__(self, otro):
        if(Libro.modo_comparacion == 'titulo'):
            return self.titulo.strip().lower() == otro.titulo.strip().lower()
        elif( Libro.modo_comparacion == 'id'):
            return self.id == otro.id
        elif( Libro.modo_comparacion == 'isbn'):
            return self.isbn == otro.isbn
        elif( Libro.modo_comparacion == 'autor'):
            return self.autor.strip().lower() == otro.autor.strip().lower()
        elif( Libro.modo_comparacion == 'aniopublicacion'):
            return self.aniopublicacion == otro.aniopublicacion


    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "isbn": self.isbn,
            "autor": self.autor,
            "aniopublicacion": self.aniopublicacion
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["titulo"],
            data["isbn"],
            data["autor"],
            data["aniopublicacion"]
        )
    
    def get_id(self):
        return self.id
id = 0