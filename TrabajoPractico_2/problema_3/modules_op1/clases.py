class Aldea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinas = []
        self.predecesor = None

    def agregar_vecina(self, vecina, distancia):
        self.vecinas.append((distancia, vecina))

    def __lt__(self, other):
        return self.nombre < other.nombre

class ArbolMST:
    def __init__(self):
        self.conexiones = []
        self.total_distancia = 0

    def agregar_conexion(self, origen, destino, distancia):
        self.conexiones.append((origen, destino, distancia))
        self.total_distancia += distancia

    def es_conectado(self, total_aldeas):
        siono = len({origen for origen, _, _ in self.conexiones}.union(
                   {destino for _, destino, _ in self.conexiones}))
        if siono == total_aldeas: 
            return 1 
        return 2

    def distancia_promedio(self):
        if not self.conexiones:
            return 0
        return self.total_distancia / len(self.conexiones)

    def resumen_conexiones(self):
        resumen = {}
        for origen, destino, _ in self.conexiones:
            resumen[origen] = resumen.get(origen, 0) + 1
            resumen[destino] = resumen.get(destino, 0) + 1
        return resumen