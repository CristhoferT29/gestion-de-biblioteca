from utils.limpiar_consola import limpiar_consola

def menu_libros(controlador):
    while True:
        limpiar_consola()
        print('Gestionando libros...')
        print('1. Agregar libro')
        print('2. Eliminar libro')
        print('3. Buscar libro')
        print('4. Consultar libros')
        print('5. Salir')
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            controlador.agregar_libro()
            input("Presione Enter para continuar...")
        elif opcion == '2':
            controlador.eliminar_libro()
            input("Presione Enter para continuar...")
        elif opcion == '3':
            controlador.buscar_libro()
            input("Presione Enter para continuar...")
        elif opcion == '4':
            controlador.listar_libros()
            input("Presione Enter para continuar...")
        elif opcion == '5':
            print("Saliendo del menú de libros...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")
