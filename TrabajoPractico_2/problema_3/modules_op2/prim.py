import sys
from modules_op2.clases import Grafo, Vertice, Aldea
from modules_op2.cola import ColaPrioridad

import sys
from modules_op2.cola import ColaPrioridad

def prim(G, inicio):
    cp = ColaPrioridad()
    
    # Configura las distancias iniciales de los vértices
    for v in G:
        v.establecer_distancia(sys.maxsize)
        v.establecer_predecesor(None)
    
    # Configura la distancia del nodo inicial a 0 y lo añade al montículo
    inicio.establecer_distancia(0)
    cp.construirMonticulo([(v.obtener_distancia(), v) for v in G])
    
    while not cp.estaVacia():
        _, vertice_actual = cp.eliminarMin()
        
        for vecino in vertice_actual.obtener_conexiones():
            nuevo_costo = vertice_actual.obtener_ponderacion(vecino)
            
            # Utilizamos cp.contiene() para verificar la presencia en el montículo
            if cp.contiene(vecino) and nuevo_costo < vecino.obtener_distancia():
                vecino.establecer_predecesor(vertice_actual)
                vecino.establecer_distancia(nuevo_costo)
                cp.decrementarClave(vecino, nuevo_costo)

    # Mostrar el MST
    total_distancia = 0
    for vertice in G:
        predecesor = vertice.obtener_predecesor()
        if predecesor:
            distancia = vertice.obtener_distancia()
            total_distancia += distancia
            print(f"{predecesor.obtener_id()} - {vertice.obtener_id()} : {distancia}")
    
    print(f"Distancia total del MST: {total_distancia}")


def mostrar_resultados(grafo):
    nombres_aldeas = sorted(grafo.obtener_vertices())
    print("Lista de Aldeas en orden alfabético:")
    for nombre in nombres_aldeas:
        print(nombre)

    print("\nRutas de envío de noticias:")
    total_distancia = 0
    for vertice in grafo:
        predecesor = vertice.obtener_predecesor()
        if predecesor:
            distancia = vertice.obtener_distancia()
            total_distancia += distancia
            print(f"Desde {predecesor.obtener_id()} se envía a {vertice.obtener_id()} con distancia {distancia} leguas.")

    print(f"\nSuma total de distancias recorridas: {total_distancia} leguas.")

def leer_archivo(archivo):
    grafo = Grafo()
    try:
        with open(archivo, 'r') as f:
            for linea in f:
                datos = linea.strip().split(',')
                if len(datos) < 3:
                    continue
                inicio, final, distancia = datos[0].strip(), datos[1].strip(), int(datos[2].strip())
                
                # Agregar vértices y aristas en el grafo
                grafo.agregar_arista(inicio, final, distancia)
                
        return grafo
    except FileNotFoundError:
        raise Exception("El archivo no fue encontrado.")
    except ValueError:
        raise Exception("Error en el formato del archivo.")
