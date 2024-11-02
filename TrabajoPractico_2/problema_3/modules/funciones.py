import networkx as nx
import matplotlib.pyplot as plt
from modules.grafo_vertice import Grafo

def mostrar_resultados(mst):
    # Obtener y mostrar los nombres de las aldeas en orden alfabético
    nombres_aldeas = sorted([v.obtener_id() for v in mst])
    print("Lista de Aldeas en orden alfabético:")
    for nombre in nombres_aldeas:
        print(nombre)

    # Mostrar las rutas de envío de noticias
    print("\nRutas de envío de noticias:")
    total_distancia = 0
    for vertice in mst:
        predecesor = vertice.obtener_predecesor()
        if predecesor:  # Verifica si el vértice tiene un predecesor asignado en el MST
            distancia = vertice.obtener_distancia()
            total_distancia += distancia
            print(f"Desde {predecesor.obtener_id()} se envía a {vertice.obtener_id()} con distancia {distancia} leguas.")

    # Imprimir la distancia total del MST
    print(f"\nSuma total de distancias recorridas para una noticia: {total_distancia} leguas.")


def cargar_grafo_desde_archivo(nombre_archivo):
    grafo = Grafo()
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            datos = linea.strip().split(',')
            if len(datos) == 3:
                # Datos de conexión: nodo1, nodo2, peso
                nodo1, nodo2, peso = datos[0].strip(), datos[1].strip(), int(datos[2].strip())
                grafo.agregar_arista(nodo1, nodo2, peso)
            elif len(datos) == 1 and datos[0].strip():
                # Nodo sin conexiones (para asegurarse de que está en el grafo)
                grafo.agregar_vertice(datos[0].strip())
    return grafo


def dibujar_mst_desde_prim(grafo):
    G_mst = nx.Graph()
    
    # Recorrer todos los vértices del grafo y agregar solo las conexiones que forman el MST
    for vertice in grafo:
        predecesor = vertice.obtener_predecesor()
        if predecesor is not None:  # Si tiene un predecesor, es parte del MST
            peso = vertice.obtener_distancia()  # La distancia al predecesor es el peso de la arista en el MST
            G_mst.add_edge(predecesor.obtener_id(), vertice.obtener_id(), weight=peso)

    # Disposición en círculo para diferenciar visualmente del grafo original
    pos = nx.circular_layout(G_mst)
    weights = nx.get_edge_attributes(G_mst, 'weight')
    
    # Dibujar el MST con colores distintos
    nx.draw(G_mst, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, edge_color="red", width=2)
    nx.draw_networkx_edge_labels(G_mst, pos, edge_labels=weights)
    plt.title("Árbol de Expansión Mínima (MST)")
    plt.show()


def dibujar_grafo_original(grafo):
    # Crear un objeto Graph de NetworkX
    G = nx.Graph()
    
    # Agregar todos los vértices y aristas del grafo original
    for vertice in grafo:
        for vecino in vertice.obtener_conexiones():
            peso = vertice.obtener_ponderacion(vecino)
            # Asegurarse de agregar cada arista solo una vez
            if not G.has_edge(vertice.obtener_id(), vecino.obtener_id()):
                G.add_edge(vertice.obtener_id(), vecino.obtener_id(), weight=peso)
    
    # Crear la disposición y obtener los pesos de las aristas
    pos = nx.spring_layout(G)  # Disposición de los nodos
    weights = nx.get_edge_attributes(G, 'weight')
    
    # Dibujar nodos, aristas y etiquetas de pesos
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=500, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    plt.title("Grafo Original de Aldeas y Rutas")
    plt.show()


