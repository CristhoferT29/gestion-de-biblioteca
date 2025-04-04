
def valor_unico(libros, valor, campo, actulizar=False, id=None):
    for libro in libros:
        if actulizar:
            if libro[campo] == valor and libro['id'] != id:
                return False
        else:
            if libro[campo] == valor:
                return False
    return True
