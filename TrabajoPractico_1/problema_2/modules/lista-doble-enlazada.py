class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def esta_vacia(self):
        return self.tamanio == 0

    def __len__(self):
        return self.tamanio

    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamanio += 1

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamanio += 1

    def copiar(self):
        """Realiza una copia profunda de la lista"""
        nueva_lista = ListaDobleEnlazada()  # Siempre devolvemos una lista válida
        nodo_actual = self.cabeza

        while nodo_actual is not None:
            nueva_lista.agregar_al_final(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente

        return nueva_lista

    def __iter__(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            yield nodo_actual.dato
            nodo_actual = nodo_actual.siguiente

    def insertar(self, dato, posicion=None):
        pass

    def extraer(self, posicion=None):
        pass

    def invertir(self):
        pass

    def concatenar(self):
        pass

    def __add__(self):
        pass
