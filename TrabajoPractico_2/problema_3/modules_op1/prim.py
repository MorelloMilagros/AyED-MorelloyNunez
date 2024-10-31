# funciones.py
from modules_op1.clases import Aldea, ArbolMST
from modules_op1.cola import ColaPrioridad

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
    cola_prioridad = ColaPrioridad()
    visitadas = set()
    cola_prioridad.insertar(0, aldea_inicio)
    while not cola_prioridad.estaVacia():
        distancia, aldea_actual = cola_prioridad.eliminarMin()
        if aldea_actual in visitadas:
            continue
        visitadas.add(aldea_actual)
        if aldea_actual != aldea_inicio:
            arbol.agregar_conexion(aldea_actual.predecesor, aldea_actual.nombre, distancia)
        for distancia_vecina, aldea_vecina in aldeas[aldea_actual.nombre].vecinas:
            if aldea_vecina.nombre not in visitadas:
                if not cola_prioridad.contiene(aldea_vecina):
                    aldea_vecina.predecesor = aldea_actual.nombre
                    cola_prioridad.insertar(distancia_vecina, aldea_vecina)
                else:
                    cola_prioridad.decrementarClave(aldea_vecina, distancia_vecina)
    return arbol

def mostrar_resultados(arbol, aldeas):
    nombres_aldeas = sorted(aldeas.keys())
    print("Lista de Aldeas en orden alfabético:")
    for nombre in nombres_aldeas:
        print(nombre)

    print("\nRutas de envío de noticias:")
    for origen, destino, distancia in arbol.conexiones:
        print(f"Desde {origen} se envía a {destino} con distancia {distancia} leguas.")

    print(f"\nSuma total de distancias recorridas: {arbol.total_distancia} leguas.")
