from models.libros import libros
from utils.limpiar_consola import limpiar_consola
from utils.pedir_dato_obligatorio import pedir_dato
from controllers.consultar_libros import consultar_libros
def eliminar_libro():
    try:

        limpiar_consola()
        consultar_libros(True)
        print("")
        print("3. Eliminar libro")
        print("Ingrese el ID del libro que desea eliminar:")

        id_libro = pedir_dato("ID: ")

        # Verificar si el libro existe
        libro_encontrado = next((libro for libro in libros if libro['id'] == int(id_libro)), None)

        if libro_encontrado:
            print("Esta seguro que desea eliminar el libro? (s/n)")
            confirmacion = input("Confirmación: ").lower()
            if confirmacion != 's':
                print("Eliminación cancelada.")
                return
            libros.remove(libro_encontrado)
            print("Libro eliminado exitosamente.")
        else:
            print("No se encontró un libro con ese ID.")
    except Exception as e:
        print(f"Error al eliminar el libro: {e}")