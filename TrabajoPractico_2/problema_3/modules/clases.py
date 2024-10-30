import heapq

class Aldea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinas = []

    def agregar_vecina(self, vecina, distancia):
        self.vecinas.append((distancia, vecina))

class ArbolMST:
    def __init__(self):
        self.conexiones = []
        self.total_distancia = 0

    def agregar_conexion(self, origen, destino, distancia):
        self.conexiones.append((origen, destino, distancia))
        self.total_distancia += distancia

def leer_archivo(archivo):
    aldeas = {}
    try:
        with open(archivo, 'r') as f:
            for linea in f:
                datos = linea.strip().split(',')
                if len(datos) < 3:
                    continue
                
                inicio, final, distancia = datos[0].strip(), datos[1].strip(), int(datos[2].strip())

                if inicio not in aldeas:
                    aldeas[inicio] = Aldea(inicio)
                if final not in aldeas:
                    aldeas[final] = Aldea(final)

                aldeas[inicio].agregar_vecina(aldeas[final], distancia)
                aldeas[final].agregar_vecina(aldeas[inicio], distancia)
                
        return aldeas
    except FileNotFoundError:
        raise Exception("El archivo no fue encontrado.")
    except ValueError:
        raise Exception("Error en el formato del archivo.")

def mst_prim(aldeas, aldea_inicio):
    arbol = ArbolMST()
    visitadas = set()
    min_heap = [(0, aldea_inicio.nombre, None)]  # (distancia, nombre_aldea_actual, nombre_aldea_anterior)

    while min_heap:
        distancia, nombre_aldea_actual, nombre_aldea_anterior = heapq.heappop(min_heap)

        if nombre_aldea_actual in visitadas:
            continue

        visitadas.add(nombre_aldea_actual)

        if nombre_aldea_anterior:
            arbol.agregar_conexion(nombre_aldea_anterior, nombre_aldea_actual, distancia)

        for distancia_vecina, aldea_vecina in aldeas[nombre_aldea_actual].vecinas:
            if aldea_vecina.nombre not in visitadas:
                heapq.heappush(min_heap, (distancia_vecina, aldea_vecina.nombre, nombre_aldea_actual))

    return arbol