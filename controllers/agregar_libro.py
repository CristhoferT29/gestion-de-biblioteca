from models.libros import id, libros
from utils.limpiar_consola import limpiar_consola
from utils.pedir_dato_obligatorio import pedir_dato

def agregar_libro():
    try:
        global id # USAR VARIBALE GLOBAL ID PARA QUE NO SE REPITA EL ID DEL LIBRO
        id = id + 1
        limpiar_consola()
        print("1. Agregar libro")
        print("Ingrese los datos del libro:")
        titulo = pedir_dato("Título: ",False,True,libros,'titulo')
        isbn = pedir_dato("ISBN: ",False,True,libros,'isbn')
        autor = pedir_dato("Autor: ")
        aniopublicacion = pedir_dato("Año de publicación: ")
        libro = {
            'id': id,
            'titulo': titulo,
            'isbn': isbn,
            'autor': autor,
            'aniopublicacion': aniopublicacion,
        }
        libros.append(libro)
        print("Libro agregado exitosamente.")
    except Exception as e:
        print(f"Error al agregar el libro: {e}")
    
        