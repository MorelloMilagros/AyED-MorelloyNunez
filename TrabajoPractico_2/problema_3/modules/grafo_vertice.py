class Vertice:
    def __init__(self, clave):
        self.__id = clave
        self.__conectado_a = {}
        self.__distancia = float('inf')
        self.__predecesor = None

    def agregar_vecino(self, vecino, ponderacion=0):
        self.__conectado_a[vecino] = ponderacion

    def obtener_id(self):
        return self.__id

    def obtener_conexiones(self):
        return self.__conectado_a.keys()

    def obtener_ponderacion(self, vecino):
        return self.__conectado_a[vecino]

    # Métodos para manejar la distancia
    def asignar_distancia(self, distancia):
        self.__distancia = distancia

    def obtener_distancia(self):
        return self.__distancia

    # Métodos para manejar el predecesor
    def asignar_predecesor(self, predecesor):
        self.__predecesor = predecesor

    def obtener_predecesor(self):
        return self.__predecesor

    def __lt__(self, other):
        return self.__distancia < other.obtener_distancia()

class Grafo:
    def __init__(self):
        self.__lista_vertices = {}
        self.__num_vertices = 0

    def agregar_vertice(self, clave):
        nuevo_vertice = Vertice(clave)
        self.__lista_vertices[clave] = nuevo_vertice
        self.__num_vertices += 1
        return nuevo_vertice

    def obtener_vertice(self, clave):
        return self.__lista_vertices.get(clave, None)

    def agregar_arista(self, de, a, costo=0):
        if de not in self.__lista_vertices:
            self.agregar_vertice(de)
        if a not in self.__lista_vertices:
            self.agregar_vertice(a)
        self.__lista_vertices[de].agregar_vecino(self.__lista_vertices[a], costo)
        self.__lista_vertices[a].agregar_vecino(self.__lista_vertices[de], costo)  # Para grafo no dirigido

    def obtener_vertices(self):
        return self.__lista_vertices.keys()

    def __iter__(self):
        return iter(self.__lista_vertices.values())