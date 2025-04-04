from utils.mostrar_menu import menu
from utils.limpiar_consola import limpiar_consola
from controllers.agregar_libro import agregar_libro
from controllers.modificar_libro import modificar_libro
from controllers.eliminar_libro import eliminar_libro
from controllers.consultar_libros import consultar_libros

def main():
    while True:
        limpiar_consola()
        menu()
        opcion = input("Ingrese una opción: ")
        if opcion == '1':
            agregar_libro()
            input("Presione Enter para continuar...")
        elif opcion == '2':
            modificar_libro()
            input("Presione Enter para continuar...")
        elif opcion == '3':
            eliminar_libro()
            input("Presione Enter para continuar...")
        elif opcion == '4':
            consultar_libros()
            input("Presione Enter para continuar...")
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:   
            print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")
main()