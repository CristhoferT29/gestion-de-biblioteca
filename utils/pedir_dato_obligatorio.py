from utils.valor_unico import valor_unico

def pedir_dato(mensaje, opcional=False, unico=False, libros=None, campo=None, actulizar=False, id=None):
    if opcional:
        valor = input(mensaje).strip()
        if valor == "":
            return None
        if actulizar and unico:
            if valor_unico(libros, valor, campo, actulizar, id):
                return valor
            else:
                print(f"El {campo} '{valor}' ya fue registrado. Por favor, escriba uno diferente.")
                return pedir_dato(mensaje, opcional, unico, libros, campo, actulizar, id)
        return valor if valor else None
    
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("Este campo es obligatorio. Por favor, ingrese un valor.")
        else:
            if unico:
                if valor_unico(libros, valor, campo ):
                    return valor
                else:
                    print(f"El {campo} '{valor}' ya fue registrado. Por favor, escriba uno diferente.")
            else:    
                return valor