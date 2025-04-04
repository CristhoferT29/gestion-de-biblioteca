import os
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')
# Limpia la consola dependiendo del sistema operativo