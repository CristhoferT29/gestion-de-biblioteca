def pedir_dato(mensaje, opcional=False, unico=False, arbol=None, clase=None, campo=None, actualizar=False, id=None):
    def construir_objeto_con_valor(valor):
        """
        Crea una instancia del objeto con solo el campo relevante lleno.
        Los demás campos se rellenan con valores vacíos o nulos.
        """
        if clase.__name__ == "Libro":
            if campo == "titulo":
                return clase(0, valor, "", "", "")
            elif campo == "isbn":
                return clase(0, "", valor, "", "")
            elif campo == "autor":
                return clase(0, "", "", valor, "")
            elif campo == "aniopublicacion":
                return clase(0, "", "", "", valor)
            elif campo == "id":
                return clase(int(valor), "", "", "", "")
        elif clase.__name__ == "Usuario":
            if campo == "nombre":
                return clase(0, valor)
            elif campo == "id":
                return clase(int(valor), "")
        
        raise ValueError(f"No se puede construir un objeto para la clase {clase.__name__} y campo {campo}")

    if opcional:
        valor = input(mensaje).strip()
        if valor == "":
            return None
        if actualizar and unico:
            if clase and arbol and campo:
                clase.modo_comparacion = campo
                objeto = construir_objeto_con_valor(valor)
                if arbol.buscar(objeto):
                    print(f"El {campo} '{valor}' ya fue registrado. Por favor, escriba uno diferente.")
                    return pedir_dato(mensaje, opcional, unico, arbol, clase, campo, actualizar, id)
                return valor
        return valor if valor else None

    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("Este campo es obligatorio. Por favor, ingrese un valor.")
        else:
            if unico and clase and arbol and campo:
                clase.modo_comparacion = campo
                objeto = construir_objeto_con_valor(valor)
                if arbol.buscar(objeto):
                    print(f"El {campo} '{valor}' ya fue registrado. Por favor, escriba uno diferente.")
                else:
                    return valor
            else:
                return valor