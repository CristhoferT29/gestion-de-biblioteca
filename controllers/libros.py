from models.libros import id, Libro
from utils.limpiar_consola import limpiar_consola
from utils.pedir_dato_obligatorio import pedir_dato
from models.arbol import ArbolBB
import models.libros as libros_module
class ControladorLibros:
    def __init__(self):
        self.arbol = ArbolBB()

    def agregar_libro(self):
        limpiar_consola()
        try:
            libros_module.id += 1
            id = libros_module.id
            limpiar_consola()
            print("Agregar libro")
            print("Ingrese los datos del libro:")

            titulo = pedir_dato("Título: ", unico=True, arbol=self.arbol, clase=Libro, campo="titulo")
            isbn = pedir_dato("ISBN: ", unico=True, arbol=self.arbol, clase=Libro, campo="isbn")
            autor = pedir_dato("Autor: ")
            aniopublicacion = pedir_dato("Año de publicación: ")

            libro = Libro(id, titulo, isbn, autor, aniopublicacion)
            self.arbol.insertar(libro)

            print("Libro agregado exitosamente.")

        except Exception as e:
            print(f"Error al agregar el libro: {e}")

    def eliminar_libro(self):
        limpiar_consola()
        try:
            print("Eliminar libro")
            print("Ingrese el ID del libro que desea eliminar:")

            id_libro = input("ID: ").strip()

            if not id_libro.isdigit():
                print("El ID debe ser un número.")
                return

            # Establecer el campo por el que se va a comparar
            Libro.modo_comparacion = "id"

            # Crear objeto temporal con el ID para buscar y eliminar
            libro_a_eliminar = Libro(int(id_libro), "", "", "", "")

            # Buscar el libro
            encontrado = self.arbol.buscar(libro_a_eliminar)

            if encontrado:
                self.arbol.borrar(libro_a_eliminar)
                print("Libro eliminado exitosamente.")
            else:
                print("No se encontró un libro con ese ID.")

        except Exception as e:
            print(f"Error al eliminar el libro: {e}")


    def buscar_libro(self):
        limpiar_consola()
        print("Buscar libro")
        print('¿Por qué atributo desea buscar el libro?')
        print('1. Título')
        print('2. ISBN')
        print('3. Autor')
        print('4. Año de publicación')
        print('5. ID')
        
        opcion = input('Opción: ')
        
        campo = {
            '1': 'titulo',
            '2': 'isbn',
            '3': 'autor',
            '4': 'aniopublicacion',
            '5': 'id'
        }.get(opcion, 'id')

        Libro.modo_comparacion = campo

        dato = input(f"Ingrese el dato a buscar por {campo}: ").strip()

        # Si busca por ID, validamos que sea entero
        if campo == 'id':
            if not dato.isdigit():
                print("El ID debe ser un número.")
                return None
            dato = int(dato)

        print(f'Buscando libro por {campo}...')

        try:

            coincidencias = [
                libro for libro in self.arbol.recorrido_inorden()
                if getattr(libro, campo) == dato
            ]

            if coincidencias:
                libro_encontrado = coincidencias[0]
                limpiar_consola()
                print("Libro encontrado:")
                print(f"ID: {libro_encontrado.id}")
                print(f"Título: {libro_encontrado.titulo}")
                print(f"ISBN: {libro_encontrado.isbn}")
                print(f"Autor: {libro_encontrado.autor}")
                print(f"Año de publicación: {libro_encontrado.aniopublicacion}")
                return libro_encontrado
            else:
                print("No se encontró ningún libro con ese dato.")
                return None
        except Exception as e:
            print(f"Error al buscar el libro: {e}")
            return None

        
    def listar_libros(self):
        limpiar_consola()
        try:
            limpiar_consola()
            print("Consultar libros")
            if self.arbol.root is None:
                print("No hay libros en la biblioteca.")
            else:
                print("Consultando libros...")
                libros = self.arbol.recorrido_inorden()
                print("Lista de libros:")
                for libro in libros:
                    print(f"ID: {libro.id}, Título: {libro.titulo}, ISBN: {libro.isbn}, Autor: {libro.autor}, Año de publicación: {libro.aniopublicacion}")
        except Exception as e:
            print(f"Error al consultar los libros: {e}")