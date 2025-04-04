from models.libros import libros
from utils.limpiar_consola import limpiar_consola
from utils.pedir_dato_obligatorio import pedir_dato
from controllers.consultar_libros import consultar_libros
def modificar_libro():
    try:
        limpiar_consola()
        consultar_libros(True)
        print("2. Modificar libro")
        print("Ingrese el ID del libro que desea modificar:")
        
        id_libro = pedir_dato("ID: ")
        
        # Verificar si el libro existe
        # next devuelve el primer elemento que cumple la condición o None si no hay coincidencias
        libro_encontrado = next((libro for libro in libros if libro['id'] == int(id_libro)), None)
        
        if libro_encontrado:
            print("Ingrese los nuevos datos del libro (deje en blanco para no modificar):")
            nuevo_titulo = pedir_dato("Título: ", True, True, libros, 'titulo',True, int(id_libro))
            nuevo_isbn = pedir_dato("ISBN: ", True, True, libros, 'isbn',True, int(id_libro))
            nuevo_autor = pedir_dato("Autor: ", True)
            nuevo_aniopublicacion = pedir_dato("Año de publicación: ", True)
            
            # Actualizar los datos del libro
            if nuevo_titulo:
                libro_encontrado['titulo'] = nuevo_titulo
            if nuevo_isbn:
                libro_encontrado['isbn'] = nuevo_isbn
            if nuevo_autor:
                libro_encontrado['autor'] = nuevo_autor
            if nuevo_aniopublicacion:
                libro_encontrado['aniopublicacion'] = nuevo_aniopublicacion
            
            print("Libro modificado exitosamente.")
        else:
            print("No se encontró un libro con ese ID.")
    except Exception as e:
        print(f"Error al modificar el libro: {e}")