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
        if posicion is None:
            self.agregar_al_final(dato)
        elif posicion < 0 or posicion > self.tamanio:
            raise IndexError("Posición inválida")
        elif posicion == 0:
            self.agregar_al_inicio(dato)
        elif posicion == self.tamanio:
            self.agregar_al_final(dato)
        else:
            nuevo_nodo = Nodo(dato)
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual
            nuevo_nodo.anterior = actual.anterior
            actual.anterior.siguiente = nuevo_nodo
            actual.anterior = nuevo_nodo
            self.tamanio += 1

    def extraer(self, posicion=None):
        if self.esta_vacia():
            raise IndexError("Lista vacía")
        if posicion is None:
            posicion = self.tamanio - 1
        if posicion < 0:
            posicion += self.tamanio
        if posicion < 0 or posicion >= self.tamanio:
            raise IndexError("Posición inválida")

        if posicion == 0:
            valor = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None
        elif posicion == self.tamanio - 1:
            valor = self.cola.dato
            self.cola = self.cola.anterior
            if self.cola:
                self.cola.siguiente = None
            else:
                self.cabeza = None
        else:
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            valor = actual.dato
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
        self.tamanio -= 1
        return valor

    def invertir(self):
        actual = self.cabeza
        self.cabeza, self.cola = self.cola, self.cabeza
        while actual:
            actual.siguiente, actual.anterior = actual.anterior, actual.siguiente
            actual = actual.anterior

    def concatenar(self, otra_lista):
        if otra_lista.esta_vacia():
            return
        otra_lista_copia = otra_lista.copiar()  # Copia la lista para no modificar la original
        if self.esta_vacia():
            self.cabeza = otra_lista_copia.cabeza
            self.cola = otra_lista_copia.cola
        else:
            self.cola.siguiente = otra_lista_copia.cabeza
            otra_lista_copia.cabeza.anterior = self.cola
            self.cola = otra_lista_copia.cola
        self.tamanio += len(otra_lista_copia)

    def __add__(self, otra_lista):
        nueva_lista = self.copiar()
        nueva_lista.concatenar(otra_lista)
        return nueva_lista