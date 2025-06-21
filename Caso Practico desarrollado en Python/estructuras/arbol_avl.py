class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1

class AVLTree:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if not nodo:
            return NodoAVL(valor)
        if valor < nodo.valor:
            nodo.izq = self._insertar(nodo.izq, valor)
        else:
            nodo.der = self._insertar(nodo.der, valor)
        return nodo

    def inorden(self):
        def _inorden(n):
            if n:
                _inorden(n.izq)
                print(n.valor, end=" ")
                _inorden(n.der)
        _inorden(self.raiz)
        print()