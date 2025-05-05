from models.libros import Libro
from models.usuarios import Usuario
from models.prestamos import Prestamo
import models.prestamos as prestamos_module
prestamos = []
id_prestamo = 0

class ControladorPrestamos:
    def agregar_prestamo(self, arbol_libros, arbol_usuarios):
        global id_prestamo
        print("Registrar nuevo préstamo")

        id_libro = input("ID del libro: ").strip()
        id_usuario = input("ID del usuario: ").strip()

        if not id_libro.isdigit() or not id_usuario.isdigit():
            print("Los IDs deben ser numéricos.")
            return

        id_libro = int(id_libro)
        id_usuario = int(id_usuario)

        # Validación: buscar en los árboles
        Libro.modo_comparacion = "id"
        Usuario.modo_comparacion = "id"
        libro = arbol_libros.buscar(Libro(id_libro,'','','',''))
        usuario = arbol_usuarios.buscar(Usuario(id_usuario,''))

        if not libro:
            print("Libro no encontrado.")
            return
        if not usuario:
            print("Usuario no encontrado.")
            return

        for prestamo in prestamos:
            if prestamo.libro == id_libro:
                print("Ese libro ya está prestado.")
                return
            if prestamo.usuario == id_usuario:
                print("Ese usuario ya tiene un préstamo activo.")
                return
        
        prestamos_module.id += 1
        id_prestamo = prestamos_module.id
        nuevo = Prestamo(id_prestamo, id_libro, id_usuario)
        prestamos.append(nuevo)
        print("Préstamo registrado con éxito.")

    def eliminar_prestamo(self):
        print("Eliminar préstamo")
        id_a_eliminar = input("ID del préstamo: ").strip()
        if not id_a_eliminar.isdigit():
            print("Debe ser un número.")
            return

        global prestamos
        id_a_eliminar = int(id_a_eliminar)
        original = len(prestamos)
        prestamos = [p for p in prestamos if p.id != id_a_eliminar]
        if len(prestamos) < original:
            print("Préstamo eliminado.")
        else:
            print("No se encontró el préstamo.")

    def listar_prestamos(self):
        if not prestamos:
            print("No hay préstamos.")
        else:
            for p in prestamos:
                print(f"ID: {p.id}, ID Libro: {p.libro}, ID Usuario: {p.usuario}")

    def cargar_prestamos_del_json(self, prestamo):
            prestamos.append(prestamo)