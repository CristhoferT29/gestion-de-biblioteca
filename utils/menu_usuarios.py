from utils.limpiar_consola import limpiar_consola
def menu_usuarios(controlador):
    while True:
        limpiar_consola()
        print("Gestionando usuarios...")
        print("1. Agregar usuario")
        print("2. Eliminar usuario")
        print("3. Consultar usuarios")
        print("4. Buscar usuario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            controlador.agregar_usuario()
            input("Presione Enter para continuar...")
        elif opcion == '2':
            controlador.eliminar_usuario()
            input("Presione Enter para continuar...")
        elif opcion == '3':
            controlador.listar_usuarios()
            input("Presione Enter para continuar...")
        elif opcion == '4':
            controlador.buscar_usuario()
            input("Presione Enter para continuar...")
        elif opcion == '5':
            print("Saliendo del menú de usuarios...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")
    