from models.usuarios import id, Usuario
from utils.limpiar_consola import limpiar_consola
from utils.pedir_dato_obligatorio import pedir_dato
from models.arbol import ArbolBB
import models.usuarios as usuarios_module

class ControladorUsuarios:
    def __init__(self):
        self.arbol = ArbolBB()

    def agregar_usuario(self):
        limpiar_consola()
        try:
            usuarios_module.id += 1  # ID autoincremental global
            id = usuarios_module.id
            limpiar_consola()
            print("Agregar usuario")
            print("Ingrese los datos del usuario:")

            nombre = pedir_dato("Nombre: ", unico=True, arbol=self.arbol, clase=Usuario, campo="nombre")

            usuario = Usuario(id, nombre)
            Usuario.modo_comparacion = "id"
            self.arbol.insertar(usuario)

            print("Usuario agregado exitosamente.")

        except Exception as e:
            print(f"Error al agregar el usuario: {e}")

    def eliminar_usuario(self):
        limpiar_consola()
        try:
            print("Eliminar usuario")
            print("Ingrese el ID del usuario que desea eliminar:")

            id_usuario = input("ID: ").strip()

            if not id_usuario.isdigit():
                print("El ID debe ser un número.")
                return

            Usuario.modo_comparacion = "id"
            usuario_a_eliminar = Usuario(int(id_usuario), "")

            encontrado = self.arbol.buscar(usuario_a_eliminar)

            if encontrado:
                self.arbol.borrar(usuario_a_eliminar)
                print("Usuario eliminado exitosamente.")
            else:
                print("No se encontró un usuario con ese ID.")

        except Exception as e:
            print(f"Error al eliminar el usuario: {e}")

    def buscar_usuario(self):
        limpiar_consola()
        print("Buscar usuario")
        print('¿Por qué atributo desea buscar el usuario?')
        print('1. Nombre')
        print('2. ID')

        opcion = input('Opción: ')

        campo = {
            '1': 'nombre',
            '2': 'id'
        }.get(opcion, 'id')

        dato = input(f"Ingrese el dato a buscar por {campo}: ").strip()

        if campo == 'id':
            if not dato.isdigit():
                print("El ID debe ser un número.")
                return None
            dato = int(dato)

        try:
            if campo == 'id':
                # Buscar por ID directamente usando ABB
                Usuario.modo_comparacion = "id"
                usuario_a_buscar = Usuario(dato, "")
                nodo = self.arbol.buscar(usuario_a_buscar)
                if nodo:
                    usuario = nodo.valor
                    print("Usuario encontrado:")
                    print(f"ID: {usuario.id}, Nombre: {usuario.nombre}")
                    return usuario
            else:
                # Buscar por campo con recorrido inorden
                coincidencias = [
                    usuario for usuario in self.arbol.recorrido_inorden()
                    if getattr(usuario, campo).lower() == dato.lower()
                ]
                if coincidencias:
                    usuario = coincidencias[0]  # solo mostramos el primero
                    print("Usuario encontrado:")
                    print(f"ID: {usuario.id}, Nombre: {usuario.nombre}")
                    return usuario

            print("No se encontró ningún usuario con ese dato.")
            return None

        except Exception as e:
            print(f"Error al buscar el usuario: {e}")
            return None


    def listar_usuarios(self):
        limpiar_consola()
        try:
            print("Consultar usuarios")
            if self.arbol.root is None:
                print("No hay usuarios registrados.")
            else:
                usuarios = self.arbol.recorrido_inorden()
                print("Lista de usuarios:")
                for usuario in usuarios:
                    print(f"ID: {usuario.id}, Nombre: {usuario.nombre}")
        except Exception as e:
            print(f"Error al consultar los usuarios: {e}")
