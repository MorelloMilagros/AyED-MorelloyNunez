import random

class Carta:
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    palos = ['trebol', 'corazones', 'diamantes', 'picas']

    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __repr__(self):
        return f"{self.valor} de {self.palo}"

    def obtener_valor(self):
        return Carta.valores.index(self.valor)

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class Mazo:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
        self.crear_mazo()
        self.mazo = self

    def crear_mazo(self):
        cartas = [Carta(valor, palo) for valor in Carta.valores for palo in Carta.palos]
        random.shuffle(cartas)
        for carta in cartas:
            self.agregar_al_final(carta)

    def esta_vacia(self):
        return self.tamanio == 0

    def agregar_al_final(self, carta):
        nuevo_nodo = Nodo(carta)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamanio += 1

    def agregar_al_inicio(self, carta):
        nuevo_nodo = Nodo(carta)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamanio += 1

    def extraer_primero(self):
        if self.esta_vacia():
            raise DequeEmptyError("El mazo no tiene más cartas")
        carta = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        if self.cabeza:
            self.cabeza.anterior = None
        else:
            self.cola = None
        self.tamanio -= 1
        return carta

    def repartir(self):
        mitad = self.tamanio // 2
        mazo1 = []
        mazo2 = []
        actual = self.cabeza
        for i in range(self.tamanio):
            if i < mitad:
                mazo1.append(actual.dato)
            else:
                mazo2.append(actual.dato)
            actual = actual.siguiente
        return mazo1, mazo2

    # Método __len__ para devolver el tamaño del mazo
    def __len__(self):
        return self.tamanio

    # Métodos necesarios para el test
    def poner_carta_arriba(self, carta):
        """Poner una carta en la parte superior (al inicio) del mazo."""
        self.agregar_al_inicio(carta)

    def poner_carta_abajo(self, carta):
        """Poner una carta en la parte inferior (al final) del mazo."""
        self.agregar_al_final(carta)

    def sacar_carta_arriba(self, mostrar=False):
        """Sacar una carta de la parte superior (al inicio) del mazo."""
        if self.esta_vacia():
            raise DequeEmptyError("El mazo no tiene más cartas")
        carta = self.extraer_primero()
        return carta

    

class DequeEmptyError(Exception):
    """Excepción lanzada cuando se intenta extraer de un deque vacío."""
    pass

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cartas = []

    def robar_carta(self):
        if not self.cartas:
            raise DequeEmptyError("El jugador no tiene más cartas") 
        return self.cartas.pop(0)

    def agregar_cartas(self, nuevas_cartas):
        self.cartas.extend(nuevas_cartas)

    def tiene_cartas(self):
        return len(self.cartas) > 0

class Juego:
    N_TURNOS = 10000

    def __init__(self):
        self.mazo = Mazo()
        cartas_j1, cartas_j2 = self.mazo.repartir()

        self.jugador_1 = Jugador("Jugador 1")
        self.jugador_1.agregar_cartas(cartas_j1)

        self.jugador_2 = Jugador("Jugador 2")
        self.jugador_2.agregar_cartas(cartas_j2)

        self.cartas_en_la_mesa = []
        self.turno = 0

    def comparar_cartas(self, carta_1, carta_2):
        if carta_1.obtener_valor() > carta_2.obtener_valor():
            return 1
        elif carta_1.obtener_valor() < carta_2.obtener_valor():
            return 2
        return 0

    def guerra(self):
        if len(self.jugador_1.cartas) < 4 or len(self.jugador_2.cartas) < 4:
            return 2 if len(self.jugador_1.cartas) < 4 else 1

        self.cartas_en_la_mesa += [self.jugador_1.robar_carta() for _ in range(4)]
        self.cartas_en_la_mesa += [self.jugador_2.robar_carta() for _ in range(4)]

        carta_guerra_1 = self.cartas_en_la_mesa[-2]
        carta_guerra_2 = self.cartas_en_la_mesa[-1]

        return self.comparar_cartas(carta_guerra_1, carta_guerra_2)

    def jugar_turno(self):
        self.turno += 1
        carta_1 = self.jugador_1.robar_carta()
        carta_2 = self.jugador_2.robar_carta()

        self.cartas_en_la_mesa.append(carta_1)
        self.cartas_en_la_mesa.append(carta_2)

        resultado = self.comparar_cartas(carta_1, carta_2)

        if resultado == 1:
            self.jugador_1.agregar_cartas(self.cartas_en_la_mesa)
            self.cartas_en_la_mesa = []
        elif resultado == 2:
            self.jugador_2.agregar_cartas(self.cartas_en_la_mesa)
            self.cartas_en_la_mesa = []
        else:
            resultado_guerra = self.guerra()
            if resultado_guerra == 1:
                self.jugador_1.agregar_cartas(self.cartas_en_la_mesa)
            else:
                self.jugador_2.agregar_cartas(self.cartas_en_la_mesa)

            self.cartas_en_la_mesa = []

    def jugar(self):
        while self.jugador_1.tiene_cartas() and self.jugador_2.tiene_cartas() and self.turno < self.N_TURNOS:
            self.jugar_turno()

            if not self.jugador_1.tiene_cartas():
                return 2
            elif not self.jugador_2.tiene_cartas():
                return 1

        if self.turno == self.N_TURNOS:
            return 0
