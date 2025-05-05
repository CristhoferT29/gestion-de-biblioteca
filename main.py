from utils.mostrar_menu import menu
from utils.limpiar_consola import limpiar_consola
from utils.menu_libros import menu_libros
from utils.menu_usuarios import menu_usuarios
from utils.menu_prestamos import menu_prestamos
from controllers.prestamos import ControladorPrestamos, prestamos
from controllers.libros import ControladorLibros
from controllers.usuarios import ControladorUsuarios
from utils.persistencia import cargar_json, guardar_json
from models.libros import Libro
from models.usuarios import Usuario
from models.prestamos import Prestamo
import models.libros as libros_module
import models.usuarios as usuarios_module
import models.prestamos as prestamos_module

controladorUsuario = ControladorUsuarios()
controladorLibro = ControladorLibros()
controladorPrestamo = ControladorPrestamos()

libros_cargados = cargar_json("libros.json", Libro)
usuarios_cargados = cargar_json("usuarios.json", Usuario)
prestamos_cargados = cargar_json("prestamos.json", Prestamo)

for libro in libros_cargados:
    controladorLibro.arbol.insertar(libro)

for usuario in usuarios_cargados:
    controladorUsuario.arbol.insertar(usuario)

for prestamo in prestamos_cargados:
    controladorPrestamo.cargar_prestamos_del_json(prestamo)


if len(libros_cargados) != 0:
    #print("ANTES:", libros_module.id)
    libros_module.id = max(libro.id for libro in libros_cargados)
    #print("DESPUÉS:", libros_module.id)


if usuarios_cargados:
    usuarios_module.id = max(usuario.id for usuario in usuarios_cargados)

if prestamos_cargados:
    prestamos_module.id = max(prestamo.id for prestamo in prestamos_cargados)

def main():
    while True:
        limpiar_consola()
        menu()
        opcion = input("Ingrese una opción: ")
        if opcion == '1':
            limpiar_consola()
            menu_libros(controladorLibro)
            input("Presione Enter para continuar...")
        elif opcion == '2':
            menu_prestamos(controladorPrestamo, controladorLibro.arbol, controladorUsuario.arbol)
            input("Presione Enter para continuar...")
        elif opcion == '3':
            menu_usuarios(controladorUsuario)
            input("Presione Enter para continuar...")
        elif opcion == '4':
            print("Saliendo del programa...")
            guardar_json("libros.json", controladorLibro.arbol.recorrido_inorden())
            guardar_json("usuarios.json", controladorUsuario.arbol.recorrido_inorden())
            guardar_json("prestamos.json", prestamos)
            break
        else:   
            print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")
main()