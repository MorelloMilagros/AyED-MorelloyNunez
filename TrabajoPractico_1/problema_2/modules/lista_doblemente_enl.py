class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self._tamanio = 0

    def esta_vacia(self):
        # Devuelve True si la lista está vacía
        pass

    def __len__(self):
        # Devuelve el número de ítems de la lista
        pass

    def agregar_al_inicio(self, item):
        # Agrega un nuevo ítem al inicio de la lista
        pass

    def agregar_al_final(self, item):
        # Agrega un nuevo ítem al final de la lista
        pass

    def insertar(self, item, posicion=None):
        # Agrega un nuevo ítem a la lista en "posicion"
        pass

    def extraer(self, posicion=None):
        # Elimina y devuelve el ítem en "posición"
        pass

    def copiar(self):
        # Realiza una copia de la lista elemento a elemento
        pass

    def invertir(self):
        # Invierte el orden de los elementos de la lista
        pass

    def concatenar(self, otra_lista):
        # Concatenar la lista actual con la otra lista
        pass

    def __add__(self, otra_lista):
        # Sumar dos listas debe crear una nueva lista
        pass