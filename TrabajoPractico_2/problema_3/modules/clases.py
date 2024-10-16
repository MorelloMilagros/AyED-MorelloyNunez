import heapq

class Aldea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinas = []

    def agregar_vecina(self, vecina, distancia):
        self.vecinas.append((distancia, vecina))

def leer_archivo(archivo):
    aldeas = {}
    try:
        with open(archivo, 'r') as f:
            for linea in f:
                datos = linea.strip().split(',')
                
                # Verificar que la línea tenga al menos 3 partes (inicio, final, distancia)
                if len(datos) < 3:
                    continue  # Si no es válida, la saltamos
                
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
    mst = []
    visitadas = set()
    total_distancia = 0
    min_heap = [(0, aldea_inicio.nombre, None)]  # (distancia, nombre_aldea_actual, nombre_aldea_anterior)

    while min_heap:
        distancia, nombre_aldea_actual, nombre_aldea_anterior = heapq.heappop(min_heap)

        if nombre_aldea_actual in visitadas:
            continue

        visitadas.add(nombre_aldea_actual)
        aldea_actual = aldeas[nombre_aldea_actual]

        if nombre_aldea_anterior:
            mst.append((nombre_aldea_anterior, nombre_aldea_actual, distancia))
            total_distancia += distancia

        for distancia_vecina, aldea_vecina in aldea_actual.vecinas:
            if aldea_vecina.nombre not in visitadas:
                # Inserta la distancia, nombre de la aldea vecina y nombre de la aldea actual
                heapq.heappush(min_heap, (distancia_vecina, aldea_vecina.nombre, nombre_aldea_actual))

    return mst, total_distancia
