from models.libros import libros
from utils.limpiar_consola import limpiar_consola
def consultar_libros(actualizarOEliminar=False):
    try:
        limpiar_consola()
        if not actualizarOEliminar:
            print("4. Consultar libros")
        if len(libros) == 0:
            print("No hay libros en la biblioteca.")
        else:
            print("Consultando libros...")
            print("Lista de libros:")
            for libro in libros:
                print(f"ID: {libro['id']}, Título: {libro['titulo']}, ISBN: {libro['isbn']}, Autor: {libro['autor']}, Año de publicación: {libro['aniopublicacion']}")
    except Exception as e:
        print(f"Error al consultar los libros: {e}")