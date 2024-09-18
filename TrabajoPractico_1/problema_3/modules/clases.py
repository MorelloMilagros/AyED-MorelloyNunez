import random

class Carta:
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    palos = ['♠', '♥', '♦', '♣']

    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __repr__(self):
        return f"{self.valor}{self.palo}"

    def obtener_valor(self):
        return Carta.valores.index(self.valor)

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

    def extraer_del_inicio(self):
        if self.esta_vacia():
            raise IndexError("Lista vacía")
        valor = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        if self.cabeza:
            self.cabeza.anterior = None
        else:
            self.cola = None
        self.tamanio -= 1
        return valor

    def extraer_del_final(self):
        if self.esta_vacia():
            raise IndexError("Lista vacía")
        valor = self.cola.dato
        self.cola = self.cola.anterior
        if self.cola:
            self.cola.siguiente = None
        else:
            self.cabeza = None
        self.tamanio -= 1
        return valor

class Mazo:
    def __init__(self):
        self.mazo = ListaDobleEnlazada()

    def repartir(self):
        cartas = [Carta(valor, palo) for valor in Carta.valores for palo in Carta.palos]
        random.shuffle(cartas)
        mitad = len(cartas) // 2
        return cartas[:mitad], cartas[mitad:]

    def poner_carta_arriba(self, carta):
        self.mazo.agregar_al_inicio(carta)

    def poner_carta_abajo(self, carta):
        self.mazo.agregar_al_final(carta)

    def sacar_carta_arriba(self):
        return self.mazo.extraer_del_inicio()

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cartas = Mazo()

    def robar_carta(self):
        return self.cartas.sacar_carta_arriba()

    def agregar_cartas(self, nuevas_cartas):
        for carta in nuevas_cartas:
            self.cartas.poner_carta_abajo(carta)

    def tiene_cartas(self):
        return self.cartas.mazo.tamanio > 0

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
        if not (self.jugador_1.tiene_cartas() and self.jugador_2.tiene_cartas()):
            return 2 if not self.jugador_1.tiene_cartas() else 1

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
        else:
            return 0