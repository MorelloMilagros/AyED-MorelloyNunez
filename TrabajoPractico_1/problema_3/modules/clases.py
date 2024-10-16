import random
from modules.lista_doble_enlazada import ListaDobleEnlazada

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

class Mazo:
    def __init__(self):
        self.cartas = ListaDobleEnlazada()  # Usamos la lista doblemente enlazada para las cartas
        self.crear_mazo()

    def crear_mazo(self):
        cartas = [Carta(valor, palo) for valor in Carta.valores for palo in Carta.palos]
        random.shuffle(cartas)
        for carta in cartas:
            self.cartas.agregar_al_final(carta)  # Usamos el método de la LDE para agregar cartas al final

    def repartir(self):
        mitad = len(self.cartas) // 2
        mazo1 = ListaDobleEnlazada()
        mazo2 = ListaDobleEnlazada()

        for i in range(mitad):
            mazo1.agregar_al_final(self.cartas.extraer(0))  # Extraemos cartas de la LDE y las agregamos a mazo1
        for i in range(mitad, len(self.cartas)):
            mazo2.agregar_al_final(self.cartas.extraer(0))  # Extraemos el resto para mazo2

        return mazo1, mazo2

    def poner_carta_arriba(self, carta):
        self.cartas.agregar_al_inicio(carta)  # Usamos el método de la LDE para agregar al inicio

    def poner_carta_abajo(self, carta):
        self.cartas.agregar_al_final(carta)  # Usamos el método de la LDE para agregar al final

    def sacar_carta_arriba(self):
        return self.cartas.extraer(0)  # Usamos el método de la LDE para extraer desde el inicio

class DequeEmptyError(Exception):
    """Excepción lanzada cuando se intenta extraer de un deque vacío."""
    pass

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cartas = ListaDobleEnlazada()  # Usar ListaDobleEnlazada para las cartas del jugador

    def robar_carta(self):
        if len(self.cartas) == 0:
            raise DequeEmptyError("El jugador no tiene más cartas") 
        return self.cartas.extraer(0)  # Usar extraer para sacar la primera carta

    def agregar_cartas(self, nuevas_cartas):
        for carta in nuevas_cartas:
            self.cartas.agregar_al_final(carta)  # Usar agregar al final para las nuevas cartas

    def tiene_cartas(self):
        return len(self.cartas) > 0

class Juego:
    N_TURNOS = 10000

    def __init__(self):
        self.mazo = Mazo()  # Usamos la nueva clase Mazo con LDE
        cartas_j1, cartas_j2 = self.mazo.repartir()

        self.jugador_1 = Jugador("Jugador 1")
        self.jugador_1.agregar_cartas(cartas_j1)

        self.jugador_2 = Jugador("Jugador 2")
        self.jugador_2.agregar_cartas(cartas_j2)

        self.cartas_en_la_mesa = ListaDobleEnlazada()
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

        self.cartas_en_la_mesa.agregar_al_final(carta_1)
        self.cartas_en_la_mesa.agregar_al_final(carta_2)

        resultado = self.comparar_cartas(carta_1, carta_2)

        if resultado == 1:
            while len(self.cartas_en_la_mesa) > 0:
                self.jugador_1.agregar_cartas([self.cartas_en_la_mesa.extraer(0)])
        elif resultado == 2:
            while len(self.cartas_en_la_mesa) > 0:
                self.jugador_2.agregar_cartas([self.cartas_en_la_mesa.extraer(0)])
        else:
            resultado_guerra = self.guerra()
            if resultado_guerra == 1:
                while len(self.cartas_en_la_mesa) > 0:
                    self.jugador_1.agregar_cartas([self.cartas_en_la_mesa.extraer(0)])
            else:
                while len(self.cartas_en_la_mesa) > 0:
                    self.jugador_2.agregar_cartas([self.cartas_en_la_mesa.extraer(0)])

    def jugar(self):
        while self.jugador_1.tiene_cartas() and self.jugador_2.tiene_cartas() and self.turno < self.N_TURNOS:
            self.jugar_turno()

            if not self.jugador_1.tiene_cartas():
                return 2
            elif not self.jugador_2.tiene_cartas():
                return 1

        if self.turno == self.N_TURNOS:
            return 0
