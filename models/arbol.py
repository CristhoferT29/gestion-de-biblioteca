class Node:
    def __init__(self, valor):
        # Cada nodo guarda un valor y tiene referencias a sus hijos y padre
        self.valor = valor
        self.izq = None  # Hijo izquierdo
        self.der = None  # Hijo derecho
        self.padre = None  # Padre del nodo

class ArbolBB:
    def __init__(self):
        self.root = None  # Nodo raíz del árbol

    def insertar(self, valor):
        """Inserta un nuevo valor en el árbol."""
        if self.root is None:
            self.root = Node(valor)  # Si el árbol está vacío, se inserta en la raíz
        else:
            self._insertar_recursivamente(self.root, valor)

    def _insertar_recursivamente(self, node, valor):
        """Lógica recursiva para insertar un valor respetando la regla del ABB."""
        if valor < node.valor:
            if node.izq is None:
                node.izq = Node(valor)
                node.izq.padre = node
            else:
                self._insertar_recursivamente(node.izq, valor)
        else:
            if node.der is None:
                node.der = Node(valor)
                node.der.padre = node
            else:
                self._insertar_recursivamente(node.der, valor)

    def buscar(self, valor):
        """Busca un valor en el árbol y devuelve el nodo si existe, o None si no."""
        return self._buscar_recursivamente(self.root, valor)

    def _buscar_recursivamente(self, node, valor):
        """
        Búsqueda recursiva:
        - Si el nodo es None, no existe.
        - Si el nodo es igual al valor, se encontró.
        - Si el valor es menor, busca a la izquierda.
        - Si es mayor, busca a la derecha.
        """
        if node is None or node.valor == valor:
            return node
        if valor < node.valor:
            return self._buscar_recursivamente(node.izq, valor)
        else:
            return self._buscar_recursivamente(node.der, valor)

    def borrar(self, valor):
        """Elimina un nodo con el valor dado si existe."""
        self.root = self._borrar_recursivamente(self.root, valor)

    def _borrar_recursivamente(self, node, valor):
        """
        Elimina un nodo del árbol:
        - Caso 1: No se encuentra (retorna None).
        - Caso 2: Tiene 1 hijo (se reemplaza).
        - Caso 3: Tiene 2 hijos (se reemplaza con el menor del subárbol derecho).
        """
        if node is None:
            return node

        if valor < node.valor:
            node.izq = self._borrar_recursivamente(node.izq, valor)
        elif valor > node.valor:
            node.der = self._borrar_recursivamente(node.der, valor)
        else:
            # Nodo con solo un hijo o sin hijos
            if node.izq is None:
                return node.der
            elif node.der is None:
                return node.izq

            # Nodo con dos hijos: obtener el nodo más pequeño del subárbol derecho
            temp = self._min_value_node(node.der)
            node.valor = temp.valor  # Reemplaza el valor
            node.der = self._borrar_recursivamente(node.der, temp.valor)

        return node

    def _min_value_node(self, node):
        """Devuelve el nodo con el valor mínimo en un subárbol (el más a la izquierda)"""
        actual = node
        while actual.izq is not None:
            actual = actual.izq
        return actual

    def recorrido_inorden(self):
        """
        Devuelve una lista con los elementos del árbol en orden ascendente
        (según la comparación definida en los objetos).
        """
        elementos = []
        self._inorden(self.root, elementos)
        return elementos

    def _inorden(self, nodo, lista):
        if nodo is not None:
            self._inorden(nodo.izq, lista)
            lista.append(nodo.valor)
            self._inorden(nodo.der, lista)
