import unittest

# Definición de la excepción personalizada
class DequeEmptyError(Exception):
    pass

# Nodo de la lista doblemente enlazada
class Nodo:
    def __init__(self, dato=None, siguiente=None, anterior=None):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior

# Implementación de la lista doblemente enlazada
class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def es_vacia(self):
        return self._size == 0
    
    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.es_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        self._size += 1
    
    def insertar_al_comienzo(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.es_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self._size += 1
    
    def quitar_del_comienzo(self):
        if self.es_vacia():
            raise DequeEmptyError("No se puede extraer de un mazo vacío.")
        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        if self.cabeza:
            self.cabeza.anterior = None
        else:
            self.cola = None
        self._size -= 1
        return dato
    
    def quitar_del_final(self):
        if self.es_vacia():
            raise DequeEmptyError("No se puede extraer de un mazo vacío.")
        dato = self.cola.dato
        self.cola = self.cola.anterior
        if self.cola:
            self.cola.siguiente = None
        else:
            self.cabeza = None
        self._size -= 1
        return dato

# Clase Mazo utilizando la lista doblemente enlazada
class Mazo:
    def __init__(self):
        self.mazo = ListaDoblementeEnlazada()

    def poner_carta_arriba(self, carta):
        self.mazo.insertar_al_comienzo(carta)

    def poner_carta_abajo(self, carta):
        self.mazo.insertar_al_final(carta)

    def sacar_carta_arriba(self, mostrar=False):
        if len(self.mazo) == 0:
            raise DequeEmptyError("No se puede sacar una carta de un mazo vacío.")
        carta = self.mazo.quitar_del_comienzo()
        if mostrar:
            carta.visible = True
        return carta

    def __len__(self):
        return len(self.mazo)

    def __str__(self):
        nodo_actual = self.mazo.cabeza
        cartas = []
        while nodo_actual:
            cartas.append(str(nodo_actual.dato))
            nodo_actual = nodo_actual.siguiente
        return ' '.join(cartas)

# Clase Carta que representa una carta individual
class Carta:
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    def __init__(self, valor='', palo=''):
        self.valor = valor
        self.palo = palo
        self.visible = False

    @property
    def valor_numerico(self):
        if self.valor in 'JQKA':
            return 11 + 'JQKA'.index(self.valor)
        return int(self.valor)

    def __gt__(self, otra):
        return self.valor_numerico > otra.valor_numerico

    def __str__(self):
        if self.visible:
            return f"{self.valor}{self.palo}"
        return "-X"

# Implementación del juego Guerra
class JuegoGuerra:
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    palos = ['♠', '♥', '♦', '♣']

    def __init__(self, random_seed=0):
        self.mazo_1 = Mazo()
        self.mazo_2 = Mazo()
        self._mazo_inicial = Mazo()
        self._guerra = False
        self._ganador = ''
        self._turno = 0
        self._cartas_en_la_mesa = []
        self._seed = random_seed
        self.empate = False
        self.turnos_jugados = 0

    def armar_mazo_inicial(self):
        import random
        random.seed(self._seed)
        cartas = [Carta(valor, palo) for valor in JuegoGuerra.valores for palo in JuegoGuerra.palos]
        random.shuffle(cartas)
        for carta in cartas:
            self._mazo_inicial.poner_carta_arriba(carta)
        return self._mazo_inicial

    def repartir_cartas(self):
        while len(self._mazo_inicial):
            self.mazo_1.poner_carta_arriba(self._mazo_inicial.sacar_carta_arriba())
            self.mazo_2.poner_carta_arriba(self._mazo_inicial.sacar_carta_arriba())

    def iniciar_juego(self, ver_partida=True):
        self.armar_mazo_inicial()
        self.repartir_cartas()
        self._cartas_en_la_mesa = []
        self._turno = 0

        while len(self.mazo_1) and len(self.mazo_2):
            try:
                if self._guerra:
                    for _ in range(3):
                        self._cartas_en_la_mesa.append(self.mazo_1.sacar_carta_arriba())
                        self._cartas_en_la_mesa.append(self.mazo_2.sacar_carta_arriba())
                self._cartas_en_la_mesa.append(self.mazo_1.sacar_carta_arriba(mostrar=True))
                self._cartas_en_la_mesa.append(self.mazo_2.sacar_carta_arriba(mostrar=True))

            except DequeEmptyError:
                self._ganador = 'jugador 1' if len(self.mazo_1) else 'jugador 2'
                self._guerra = False
                if ver_partida:
                    print(f'***** {self._ganador} gana la partida *****')
                break

            if ver_partida:
                self.mostrar_juego()

            if self._cartas_en_la_mesa[-2] > self._cartas_en_la_mesa[-1]:
                for carta in self._cartas_en_la_mesa:
                    self.mazo_1.poner_carta_abajo(carta)
                self._cartas_en_la_mesa = []
                self._guerra = False
            elif self._cartas_en_la_mesa[-1] > self._cartas_en_la_mesa[-2]:
                for carta in self._cartas_en_la_mesa:
                    self.mazo_2.poner_carta_abajo(carta)
                self._cartas_en_la_mesa = []
                self._guerra = False
            else:
                self._guerra = True
                if ver_partida:
                    print('**** Guerra!! ****')
            
            self.turnos_jugados += 1

    def mostrar_juego(self):
        print(f"Turno: {self._turno + 1}")
        print(f"Jugador 1: {self.mazo_1}")
        print(f"Jugador 2: {self.mazo_2}")
        print(f"Cartas en la mesa: {' '.join([str(carta) for carta in self._cartas_en_la_mesa])}")
        self._turno += 1

# Pruebas Unitarias


if __name__ == '__main__':
    unittest.main()
