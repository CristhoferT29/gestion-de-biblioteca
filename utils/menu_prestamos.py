from utils.limpiar_consola import limpiar_consola
def menu_prestamos(controlador, arbol_libros, arbol_usuarios):
    while True:
        limpiar_consola()
        print("Gestionando préstamos...")
        print("1. Agregar préstamo")
        print("2. Eliminar préstamo")
        print("3. Consultar préstamos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            controlador.agregar_prestamo(arbol_libros, arbol_usuarios)
            input("Presione Enter para continuar...")
        elif opcion == '2':
            controlador.eliminar_prestamo()
            input("Presione Enter para continuar...")
        elif opcion == '3':
            controlador.listar_prestamos()
            input("Presione Enter para continuar...")
        elif opcion == '4':
            print("Saliendo del menú de préstamos...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")